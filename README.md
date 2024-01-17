# Project Documentation and instructions
EventHandler

This project is an Event Handler than can be used to store events and group them in buckets.
We can make interrogations about buckets and events for user purposes
The project was created using:
backend server: python django framework
database: django SQLite
APIs: FastAPI
frontend: Angular

Dependencies:

Docker and Docker Compose
Linux: install separately
Windows/MacOs: install Docker Desktop, which contains both

1) Start indications

If you are using Windows, I recommend using Git Bash and following linux instructions

To start the project, first step is clone the repository from github and open a local terminal to that repository

Run the following commands:
chmod +x run_now_linux.sh/run_now_macOS.sh
chmod +x aux_run_now.sh

This will give permissions to the scripts to be executed

Execute the script command(by case):
./run_now_macOS.sh
or
./run_now_linux.sh 

This will start the docker-compose , building and starting both backend and frontend containers
A 2nd terminal will pop up, which will be our controller, as the first terminal is kept for logs

In the 2nd terminal, there will be a few options, such as Create Superuser, Run Tests, Quit Server
Both are to be kept open while the project is running

Now the project is running!

2) Navigation indications
Open any browser, and in the URL bar type "localhost". 
There is the Welcome page, with 2 options:
a) Go to user access
b) Go to admin portal

I will approach case b) first as it is more complex

Access:
Go to admin portal button redirrects us towards the admin portal
Here, we will be prompted to enter User and Password
To optain these, we will go to the 2nd terminal(the one that poped out) and select option 1
After superuser is created, we can go back in the browser, enter the data and log in
A superuser has to be created just once, if you run the project later it can be reused and skip previous steps

Use:
Here we have an admin view of the items that we handle (users, events, buckets)
From here we can add and delete events, add and delete buckets, group events to buckets (None of this are possible from user access apart from "add event")
We have an add/change button next to each, and clicking the actual name(ex. Bucket) will do same as clicking Change buton next to it.
Here we have an overview of the existing items, and an action bar which allows us to delete items

When creating a bucket, we can create multiple events on the same page and they get automatically assigned to tha bucket.
To assign existing events to a bucket, we have to go to Change Events page, click the id of the event, and there we will have option where we can assign it to a bucket.

I did not misunderstood the task. ID field is the internal ID that keeps count of the events/buckets, created by default by django and unremovable. The id used for API communications is the event's uuid, as mentioned unique and unpredictable

case a)

Access: Not applicable
Use:
This is the user interface, to make the http requests mentioned in the task.
This has been made to avoid testing the APIs with external software such as postman, everything should be testable from here
Due to lack of time to customize the page even more, some request returns can be seen only in the console ( right click on the page -> inspect -> console )
There is a button to store event, and to fetch event uuids from selected bucket.
The displayed UUIDs are also buttons, and the event information appears on click of any of those.
To avoid errors, there is already a selected bucket at launch of page, which will always be the first bucket in our database

----------------------------------------------------------------------------

Technical Details:
* Because we are using Django, wich is ORM, and we are already using models, i did not use the pydantic models specific to FastAPI, I used the already existing ones ( I created one pydantic model as proof of implementation, but not needed with django )
* Inside the project, a utils.py file can be found with configuration settings ( this is minimalistic for now as we only fetch some text). This is a practice of mine so i do store default values, enpoints for other apps (ex. for messaging, emailing, etc) so we do not hardcode these everytime we need them. Also uses caching, which saves run time
* Try/except cases are all around the project for good event monitoring, but needs Sentry integration or something alike for all the errors to be displayed in the Sentry account 
* Regex Validator created in a different file for better organization and applied into the model, not into the form (explained why in code comment)

----------------------------------------------------------------------------

Further development notes:
Because of the lack of time, two evenings were not enough for me to create all the things I wanted.
For this, I will leave her further development than can be implemented as next steps onto growing this project

* Sentry integration: Error logging is set, sentry needs to be integrated into the project, linked with an account and everything should be good to go.
* Multiple languages: For now the whole project is in English. Django offers a really nice way of approaching translations using django.po files. Not hard to implement and very useful for applications with users from multiple nations
* Unit Testing: The option to run tests is available in terminal options, test files created, just did not have the time to write the tests
* PostgreSQL: For the moment I used SQLite as the data I worked with was not either numerous or complex. For further development, I totally recommend migrating to PostgreSQL as it is more stable and can process much more complex data

----------------------------------------------------------------------------

Thank you for reaching to this point, I hope everything is as you expected with the project and everyting works smoothly, but if it crashes, as any developer would say, "It worked on my machine" :D