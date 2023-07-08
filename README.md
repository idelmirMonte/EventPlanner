# Event Planner

Welcome to the Event Planner!

The Event Planner is an intuitive and user-friendly application that will help you organize your events efficiently. With this tool, you can schedule events, receive reminders, and automatically add them to your Google Calendar. Never forget an important event again!

## Key Features
- **User-Friendly Interface:** Our intuitive and appealing design makes it easy to navigate and use all the application's functions.
- **Event Registration:** Enter the event name, date, location, and time in the user interface.
- **Custom Reminders:** Receive notifications for each scheduled event, helping you stay on top of your commitments.
- **Google Calendar Integration:** Saved events are automatically synchronized with your Google Calendar, allowing you to access them from any device.
- **Custom Color Settings:** Personalize the appearance of the application by adjusting the background and text colors according to your preferences.

## How to Use the Event Planner
1. Open the application and locate the section to add a new event.
2. Enter the event details, such as the name, date, location, and time.
3. Click the "Save" button to store the event and add it to your Google Calendar.
4. That's it! You will receive reminders for your events and can view them in your calendar.

Don't waste any more time and start organizing your events efficiently with the Event Planner. Download it now and start planning your upcoming events!

## License
This project is licensed under the [MIT License](LICENSE).




### Things to know about the project


### Adding Events to Google Calendar

To see the event added to your Google Calendar, follow these steps:

1. Ensure that the JSON key file provided (`json_key_file`) is associated with a Google Cloud project that has the Calendar API enabled. You can check this by going to the [Google Cloud Console](https://console.cloud.google.com/), selecting your project, and verifying that the Calendar API is enabled under the "APIs & Services" section.

2. Make sure the email associated with the service account in the JSON key file has proper access to add events to your Google Calendar. The email address can be found in the JSON key file under the `"client_email"` field. Share your calendar with this email address and grant it appropriate permissions (e.g., "Make changes to events" or "Make changes and manage sharing").

3. Verify that you're using the correct `calendarId` when calling the `insert` method in the `add_event_to_gmail` function. The code currently uses `"primary"` as the calendar ID, which refers to the primary calendar of the authenticated user. If you want to add the event to a different calendar, provide the correct calendar ID.

#### Granting Access to Service Account Email

To grant proper access to the service account email in order to add events to your Google Calendar, follow these steps:

1. Open your Google Calendar in a web browser.
2. On the left side panel, click on the "+" button next to "Add a friend's calendar" to expand the "Other calendars" section.
3. Select "Browse calendars of interest".
4. In the left-hand sidebar, click on the "+" button next to "Add calendar" and select "New calendar".
5. Provide a name and other details for the new calendar, and click on the "Create calendar" button.
6. Once the calendar is created, locate it in the left-hand sidebar under "Other calendars".
7. Hover over the calendar name and click on the three vertical dots (more options).
8. Select "Settings and sharing" from the menu.
9. In the "Share with specific people" section, enter the email address associated with the service account (found in the JSON key file under the `"client_email"` field).
10. Set the desired access level for the service account. For adding events, you can choose "Make changes to events" or "Make changes and manage sharing".
11. Click on the "Send" button to send the invitation.

By completing these steps, you should grant the service account the necessary access to add events to your Google Calendar. Remember to adjust the `calendarId` in the code to match the ID of the calendar you just created or the one you want to add events to.

#### Adjusting the `calendarId` in Your Code

To adjust the `calendarId` in your code, follow these steps to retrieve the `calendarId`:

1. Open your Google Calendar in a web browser.
2. On the left side panel, locate the calendar you want to use or create a new calendar.
3. Hover over the calendar name and click on the three vertical dots (more options).
4. Select "Settings and sharing" from the menu.
5. In the "Integrate calendar" section, you will find the "Calendar ID" field. Copy the ID.
6. Replace the `"primary"` value in the `calendar_service.events().insert()` method with the copied `calendarId` value.


self.calendar_service.events().insert(calendarId="your_calendar_id", body=event).execute()

Make sure to replace "your_calendar_id" with the actual ID of your desired calendar.

By adjusting the calendarId to match your calendar, the events will be added to the specified calendar.






