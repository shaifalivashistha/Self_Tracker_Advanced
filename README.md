<h1 align="center">

![LOGO](https://drive.google.com/file/d/1-Nh1P78eSMXxQ7b8VUESfHcbt-iKs3XR/view?usp=sharing)

**<u>Self Tracker</u>**
</h1>


<p align="center">
Self Tracker is a website that gives the user analytical results of its habits, health, mood, work, exersice data and helps the user to manage its daily routine on the base of that analysis. Learn more about working of Self Tracker by reading the documentation below.
</p>

## What's included

Within the application folder you'll find the following directories and files. You'll see something like this:

```text
project/
│
├── backend/
│   │
│   ├── application/
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── config.py
│   │   ├── controllers.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── security.py
│   │   ├── send_mail.py
│   │   ├── task.py
│   │   └── workers.py
│   │
│   ├── templates/
│   │   ├── mail_template.html
│   │   └── reminder_template.html
│   │   
│   ├── trackerdb.sqlite3
│   └── main.py
│
│
├── frontend/myapp/
│   │
│   ├── public/
│   │   ├── index.html
│   │   └── img/icons
│   │
│   ├── src/
│   │   ├── assets/
│   │   │   ├── main.css
│   │   │   └── Others*
│   │   │   
│   │   ├── components/
│   │   │   ├── AboutPage.vue
│   │   │   ├── DashboardPage.vue
│   │   │   ├── HomePage.vue
│   │   │   ├── LoginPage.vue
│   │   │   ├── RegisterPage.vue
│   │   │   ├── addBoolLogPage.vue
│   │   │   ├── addNumLogPage.vue 
│   │   │   ├── createTrackerPage.vue
│   │   │   ├── forgetPassword.vue 
│   │   │   ├── updateLogPage.vue
│   │   │   └── updateTrackerPage.vue
│   │   │  
│   │   │  
│   │   ├── router/
│   │   │   └── index.js
│   │   │  
│   │   ├── views/
│   │   │   ├── AboutView.vue 
│   │   │   ├── DashboardView.vue
│   │   │   ├── HomeView.vue
│   │   │   ├── LoginView.vue
│   │   │   ├── PasswordView.vue 
│   │   │   ├── RegisterView.vue
│   │   │   ├── addBoolLogView.vue 
│   │   │   ├── addNumLogView.vue
│   │   │   ├── createTrackerView.vue 
│   │   │   ├── updateLogView.vue
│   │   │   └── updateTrackerView.vue 
│   │   │ 
│   │   ├── App.vue/
│   │   │ 
│   │   │ 
│   │   └── main.js/
│   │ 
│   ├── babel.config.js
│   ├── jsconfig.json
│   ├── package-lock.json
│   ├── package.json
│   ├── vue.config.js
│   └── main.py   
│
├── Report.pdf
│
├── tracker.sqlite3
│
└── README.md  
```

## How To Run "Self-Tracker":
One can run Run "Self-tracker" using localhost command by running .  Below is the general command to run the application:

	http://127.0.0.1:5000/

We can run Run "Self-tracker" using online IDE Replit. Below is the general command to run the application on online IDE Replit:

    https://project.shaifalivashis.repl.co/

## Backend Application contents
Below are the contents of the Backend Application code-

- [Python Libraries](#python-libraries)
- [Database Tables](#database-tables)

#### Python Libraries

1. **<u>Flask:</u>**
    Flask is used for developing web applications using python, implemented on Jinja2. We used diffrent flask decorators and functions in the application for better handling here we used  **route,before_first_request decorator, redirect and render_template functions, Flask class and request, session, flash as others objects.**
    Here, *route* is used to to bind a function with a specific url where in some function we used route with variable section also and *before_app_request( )* registers a function that runs before the view function, no matter what URL is requested. *redirect( )* fuction is used to redirect a user to another endpoint. *render_template( )* function is used to render html templates stored in templates folder. *Request* is a flask object used to retrieve the data at the server side using its attributes. *Flask* is class used to create class instance in which __ __name__ __ is passed as argument which represents the name of the application package. *Flask-Session* is an extension for Flask that support Server-side Session to the application. The Session is the time between the client logs in to the server and logs out of the server. *flash( )* method of the flask module passes the message to the next request which is an HTML template.

2. <u>**Flask SqlAlchemy:**</u>
    Flask-SQLAlchemy is an extension to Flask that aims to simplify using SQLAlchemy with Flask by providing defaults and helpers to accomplish common tasks. One of the most sought after helpers being the handling of a database connection across the app. In Self Tracker, We used flask-sqlalchemy to create database schema and tables.

3. <u>**Flask Security:**</u>
    Flask-Security is an extension to Flask which adds basic security and authentication features to your Flask apps quickly and easily. In the self tracker application the flask security is used for hashing password, user vreification and authentication.

4. <u>**Flask CORS:**</u>
    Flask-CORS is an extension to Flask for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible. In Self Tracker application this module is used to allow fetch requests from Vue js frontend and send back data in response of the request.

5. <u>**Flask Caching:**</u>
    Flask-Caching is an extension to Flask that adds caching support for backends to any Flask application. In our application it is used to cache the user data such as tracker details, events and graphs logged by the user under any tracker.

6. <u>**Celery:**</u>
    Celery is an open-source Python library which is used to run the tasks asynchronously. It is a task queue that holds the tasks and distributes them to the workers in a proper manner. In the self tracker appliation the jobs handled by celery are: to export trackers list and logged events to a CSV file, to send monthly pdf reports by emails to the client that uses crontab for a scheduled event of celery, and send Daily reminders by emailing the user only if the user has not logged during the daytime.

7. <u>**Redis:**</u>
    Redis is an in-memory data store that can be used as either a high-performance key-value store or as a caching storage database. In our application the user data, tracker details along with logged events and trendline graphs are stored in the database as cache.

8. <u>**Datetime:**</u>
    Datetime is a python module which supplies classes to work with date and time. These classes provide a number of functions to deal with dates, times and time intervals. In the Self Tracker, we used datetime module to get timestamp in the application.

9. **<u>matplotlib.pyplot:</u>**
    **matplotlib.pyplot** is a collection of functions. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc. In matplotlib.


#### Database Tables

1. **<u>User:</u>**
    User table created in sqlite database by using Flask-sqlalchemy. It stores user data in rows i.e., **id, username, email, password and trackers.** Here, all except user id and trackers are taken from user during sign up. User id is an autogenerated primary key of the User table and is unique to every user, name is name of the user, username is also unique to every user it is used for login everytime by the user and tracker stores the trackers created by the user.


2. **<u>Tracker:</u>**
    Tracker table created in sqlite database by using Flask-sqlalchemy. It stores data of trackers created by any user in rows i.e.,**id, name, description, tracker type, date created and logs.** Here, user will decide the tracker name, description and tracker type while creating tracker. Id is an autogenerated primary key of the Tracker table and is unique to every user, name is name of the tracker, description is a description about the tracker by the user, tracker type a dropdown to select the type of tracker user wants, date created is the date when the tracker is created using datetime module of python and log stores the logged events under the corresponding tracker.

3. **<u>Logs:</u>**
    Logs table created in sqlite database by using Flask-sqlalchemy. It stores log data of trackers created by any user in rows i.e., **id, name, description, tracker type, date created and logs.** Here, user will decide the tracker name, description and tracker type while creating tracker. Id is an autogenerated primary key of the Tracker table and is unique to every user, name is name of the tracker, description is a description about the tracker by the user, tracker type to select the type of tracker user wants and log defines relationship between the tracker table and the log table.

3. **<u>UserTracker:</u>**
    UserTracker table created in sqlite database by using Flask-sqlalchemy. It is a Relationship table that stores information of trackers created by users by using ID from user table and ID from tracker table as foreign keys i.e., **UserTrackerID, uID and tID.**  Here, the table has UserTrackerID as its primary key with autoincreament enabled, uID is the foreign key from the user table that is the ID of the user, Similarly tID is the foreign key from the tracker table that us the ID of the tracker. Thus, the table keeps track of relation between trackers and their corresponding users. 

3. **<u>TrackerLogs:</u>**
    TrackerLogs table created in sqlite database by using Flask-sqlalchemy. It is a Relationship table that stores information of events logged under the trackers by using ID from tracker table and ID from log table as foreign keys i.e., **TrackerLogsID, tID and lID.**  Here, the table has TrackerLogsID as its primary key with autoincreament enabled, tID is the foreign key from the tracker table that is the unique ID of the tracker, Similarly lID is the foreign key from the logs table that is the ID of the tracker. Thus, the table keeps track of relation between logged events and their corresponding trackers.





## Application contents
Below are the route and fuctions of the main application code-

- [Application Libraries](#application-libraries)
- [Index](#index)
- [Sign Up](#sign-up)
- [Login](#login)
- [Dashboard](#dashboard)
- [Create Tracker](#create-tracker)
- [Log Tracker](#log-tracker)
- [Update Tracker](#update-tracker)
- [Delete Tracker](#delete-tracker)
- [Update Log](#update-log)
- [Delete Log](#delete-log)
- [About Us](#about-us)
- [Contact](#contact)
- [Creators](#creators)
- [Thanks](#thanks)


#### Application Libraries



#### Index

With the release of localhost to run the application as the application begins to work index function will direct you to the index.html i.e., the home page of the application. The index page will direct user to any page of his/her choice. The url for index page is **'/'**.

#### Sign Up

From index page if user selects signup, the user is directed to the Sign Up page with url **'/sign_up'**. In the sign up route two methods are allowed i.e., GET and POST. When the request method to server is GET the html page for sign up is rendered to the user using render_template function. Where user have to fill the required fields and using submit button will send a POST request to the server after which the filled data will be extracted from the html form and a query is sent to the db to check if the user with same username already exists or not if not the provided userdata is stored in User table of database and user is redirected to the dashboard.

#### Login

From index page if user selects login, the user is directed to the Login page with url **'/login'**. In the sign up route two methods are allowed i.e., GET and POST. When the request method to server is GET the html page for login is rendered to the user using render_template function. Where user have to fill the required fields using submit button which will send a POST request to the server after which the filled data will be extracted from the html form and we will wirte query to check if user exist or not and if the userdata exists in database user is redirected to the dashboard, else will display error message using flash.

#### Dashboard

Login and signup will send a POST request to the server to redirect user to route url **'/< string:username>/dashboard'** (username is the application username of user) which will then render the dashboard html page to the user. In dashboard, user can create new trackers and if there are any previously created trackers present, they are displayed in the dashboard everytime to the user in a tabular form.

#### Create Tracker

In dashboard if user selects Add tracker button i.e., url for route **'/< string:username>/create_tracker'** it will send a GET request to the server in response of it creater_tracker page is rendered to the user where user have to fill required fields to create a new tracker. Submitting the form provided to the user will send a POST reuqest to the server and the filled data is extracted from the html form and a query is sent to the db to check if the tracker with same trackername already exists or not, if it does not exist, the provided trackerdata is stored in Tracker table of database and user is redirected to the dashboard displaying the newly created table on the dashboard and a relation between user_id and tracker id is created in secondary table user_tracker.

#### Log Tracker

In dashboard if user selects Add log button present in tracker table url for route **'/< string:username>/<int:id >/logs'**(id is tracker id) will send a GET request to the server in reponse of it log tracker page for the tracker type is rendered to the user where user have to fill required fields to log his/her tracker. Submitting the form provided to the user will send a POST reuqest to the server and the filled data is extracted from the html form and a query is sent to the db to extract all preiviously created logs for the respective tracker and display all the logs on the log page in form of a table along with a graph(if applicable) the provided log data for respective tracker is stored in Log table of database and user is redirected back to the log page displaying the newly created table on the lag page.

#### Update Tracker

In dashboard if user selects update button present in the tracker table displayed on the dashboard will send a GET request to the server with route url **'/< string:username>/update/<int:id >'** in response of it update page for trackers is rendered to the user where user have to fill required fields to update the tracker. Submitting the form provided to the user will send a POST reuqest to the server and the filled data is extracted from the html form and a query is sent to the db to delete the existing information for the tracker and to store newly updated data for the tracker in the Tracker table of db and user is redirected to the dashboard displaying the updated table on the dashboard. 

#### Delete Tracker

In dashboard if user selects delete button present in the tracker table displayed on the dashboard will send a GET request to the server with route url **'/< string:username>/<int:id >/delete'** in response of which a query is sent to the db to delete the information for the tracker from thr Tracker table of db and user is redirected to the dashboard displaying the updated table on the dashboard.

#### Update Log

In log tracker page for the repective tracker type if user selects update button present in the log table displayed on the log page will send a GET request to the server with route url **'/< string:username>/<int:tracker_id >/<int:log_id >/update'** in response of it update page for logs is rendered to the user where user have to fill required fields to update the tracker. Submitting the form provided to the user will send a POST reuqest to the server and the filled data is extracted from the html form and a query is sent to the db to delete the existing stored information for the teracker and add new log information for the respective tracker in the log table of db and user is redirected to the log page displaying the updated table on the log page. 

#### Delete Log

In log tracker page for the repective tracker type if user selects delete button present in the log table displayed on the log page will send a GET request to the server with route url **'/< string:username>/<int:tracker_id >/< int:log_id>/delete'** in response of which a query is sent to the db to delete the information for the log present from thr Log table of db and user is redirected to the Log page displaying the updated table on the Log page.

#### About Us

From dashboard if user selects About us button, a GET request is sent to the server with url **'/about_us'** which in response will display about us page to the user that has information regarding website application.

#### Contact

From dashboard if user selects Contact button, a GET request is sent to the server with url **'/contact'** which in response will display Contact page to the user that has information regarding contact to the developer of website application.


#### Creator

- **Name : Shaifali Vashistha**
- **Roll Number : 21f1003257**
- **Student Email : 21f1003257@student.onlinedegree.iitm.ac.in**

####  Thanks

I am thankful to IIT Madras for giving me the opportunity to develop such an interesting web application!
