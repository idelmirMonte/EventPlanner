import csv
from datetime import datetime, timedelta
from plyer import notification
from google.oauth2 import service_account
from googleapiclient.discovery import build
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from google.oauth2.service_account import Credentials

# Specify the path to your JSON key file
json_key_file = ""

# Create credentials from the JSON key file
credentials = Credentials.from_service_account_file(json_key_file)

class EventOrganizer(QtWidgets.QMainWindow):
    def __init__(self):
        super(EventOrganizer, self).__init__()
        self.setWindowTitle("Event Planner")
        self.resize(600, 500)
        
        self.setStyleSheet("background-color: #14213d;")

        self.setup_ui()

        credentials = service_account.Credentials.from_service_account_file(json_key_file)
        self.calendar_service = build("calendar", "v3", credentials=credentials)

    def setup_ui(self):
        self.title_label = QtWidgets.QLabel("Event Planner", self)
        self.title_label.setGeometry(QtCore.QRect(50, 50, 500, 50))
        self.title_label.setFont(QtGui.QFont("Poppins", 24, QtGui.QFont.Bold))
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setStyleSheet("color: #fca311;")

        self.event_name_label = QtWidgets.QLabel("Event Name:", self)
        self.event_name_label.setGeometry(QtCore.QRect(100, 150, 150, 30))
        self.event_name_label.setStyleSheet("color: #fca311;")
        self.event_name_input = QtWidgets.QLineEdit(self)
        self.event_name_input.setGeometry(QtCore.QRect(250, 150, 200, 30))
        self.event_name_input.setStyleSheet("color: #fca311;")
        

        self.event_date_label = QtWidgets.QLabel("Event Date:", self)
        self.event_date_label.setGeometry(QtCore.QRect(100, 200, 150, 30))
        self.event_date_label.setStyleSheet("color: #fca311;")
        self.event_date_input = QtWidgets.QLineEdit(self)
        self.event_date_input.setGeometry(QtCore.QRect(250, 200, 200, 30))
        self.event_date_input.setStyleSheet("color: #fca311;")
        

        self.event_location_label = QtWidgets.QLabel("Location Event:", self)
        self.event_location_label.setGeometry(QtCore.QRect(100, 250, 150, 30))
        self.event_location_label.setStyleSheet("color: #fca311;")
        self.event_location_input = QtWidgets.QLineEdit(self)
        self.event_location_input.setGeometry(QtCore.QRect(250, 250, 200, 30))
        self.event_location_input.setStyleSheet("color: #fca311;")

        self.event_time_label = QtWidgets.QLabel("Time of Event (HH:MM):", self)
        self.event_time_label.setGeometry(QtCore.QRect(100, 300, 250, 30))
        self.event_time_label.setStyleSheet("color: #fca311;")
        self.event_time_input = QtWidgets.QLineEdit(self)
        self.event_time_input.setGeometry(QtCore.QRect(350, 300, 100, 30))
        self.event_time_input.setStyleSheet("color: #fca311;")
        
        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.setGeometry(QtCore.QRect(200, 350, 100, 30))
        self.save_button.setStyleSheet("background-color: #fca311; color: #14213d;")
        self.save_button.clicked.connect(self.save_event)

    def save_event(self):
        event_name = self.event_name_input.text()
        event_date = self.event_date_input.text()
        event_location = self.event_location_input.text()
        event_time = self.event_time_input.text()

        with open("event.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([event_name, event_date, event_location, event_time])

        event_datetime = datetime.strptime(event_date + " " + event_time, "%Y-%m-%d %H:%M")
        event_datetime_utc = event_datetime.astimezone(datetime.now().astimezone().tzinfo)

        now = datetime.now(event_datetime_utc.tzinfo)
        time_delta = event_datetime_utc - now
        notification_delay = time_delta.total_seconds()

        if notification_delay > 0:
            QtCore.QTimer.singleShot(int(notification_delay) * 1000, self.show_notification)

        self.add_event_to_gmail(event_name, event_datetime_utc, event_location)

        self.clear_input_fields()

    def add_event_to_gmail(self, event_name, event_datetime, event_location):
        event = {
            "summary": event_name,
            "start": {
                "dateTime": event_datetime.isoformat(),
                "timeZone": "America/Bogota"  #You can change it to your timezone
            },
            "end": {
                "dateTime": (event_datetime + timedelta(hours=1)).isoformat(),
                "timeZone": "America/Bogota" #You can change it to your timezone
            },
            "location": event_location,
            "reminders": {
                "useDefault": True
            }
        }

        self.calendar_service.events().insert(calendarId="your_calendar_id", body=event).execute()

    def show_notification(self):
        event_name = self.event_name_input.text()
        event_date = self.event_date_input.text()
        event_location = self.event_location_input.text()

        notification_title = "Reminder: " + event_name
        notification_message = f"Date: {event_date}\nLocation: {event_location}"

        notification.notify(
            title=notification_title,
            message=notification_message,
            app_icon=None,
            timeout=10
        )

    def clear_input_fields(self):
        self.event_name_input.clear()
        self.event_date_input.clear()
        self.event_location_input.clear()
        self.event_time_input.clear()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = EventOrganizer()
    window.show()
    sys.exit(app.exec_())