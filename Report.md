<u><h2 align="center">REPORT</h1></u>

***Author :***
- *<u>Name</u>*- Shaifali Vashistha
- *<u>Roll number</u>*- 21f1003257
- *<u>Student email</u>*- 21f1001231@student.onlinedegree.iitm.ac.in. 
- *<u>Details</u>*- I am a degree level student in this Online BS degree program. I have a keen interest in exploring the different realms of Technology and thus I wish to accomplish this degree with utmost dedication and hard work. I am very thankful to the **IIT Madras** for providing me this opportunity to develop such an interesting web application and making my journey interesting! 

**Description :**

In this project I have designed Self Tracker Application with 2 kinds of tracker- Numeric, Boolean which will track progress over time and shows graphs (wherever applicable). Each tracker has its unique ID, description and displays the log in time, value (based on the corresponding tracker type) and accordingly a note entered by the user. User can add, delete or update the tracker according to his/her will.

**Technologies used :**
1. *<u>Flask</u>*- used for developing web applications using python.
2. *<u>Flask-SQLAlchemy</u>*- used to create database schema and tables using SQLAlchemy with Flask by providing defaults and helpers.
3. *<u>Flask-Security</u>*- Flask extension used to add basic security, password hashing, user verification and authentication features to the application.
4. *<u>Flask-CORS</u>*-Flask extension used for handling Cross Origin Resourse Sharing(CORS), making cross origin AJAX possible. 
5. *<u>Flask-RESTful</u>*- used to create backend RESTful API.
6. *<u>Flask-Caching-</u>* Flask extension supports Server-side session to our application.
7. *<u>Celery-</u>* Open source python library used to run the tasks asynchronously. 
8. *<u>Vue js</u>*- Vue framework used as single file components to build user interface.
9. *<u>smtplib-</u>* Used to define an SMTP client session object that can be used to send mail to the client.
10. *<u>Redis-</u>* it is an in-memory data store that can be used for a high-performance key-value store or Caching.
11. *<u>Datetime</u>*- a python module which supplies classes to work with date and time. Here, datetime module to create timestamp in the application.
12. *<u>matplotlib.figure</u>*- a python module is used to create dynamic figures based on the information provided by the user.

***Database Schema :***

1. *<u>Relation-</u>* A user can have several trackers and thus we have one-to-many relationship between User and Tracker table and are connected to eachother with uid and tid as foreign keys in UserTracker table. Similarly, a Tracker can have multiple logs, so we have one-to-many relationship between Tracker and Log table and are connected to eachother with tid and lid as foreign keys in TrackerLog table. 

2. *<u>ER Diagram</u>* - [ER Diagram Link](https://drive.google.com/file/d/1CHUrNcF2NQWyeif_3OdIlI0T6Yga4LKC/view?usp=sharing)

<br>

***Architecture and Features:***

The project code is organised based on its utility in different files. I have named my project Self Tracker Application. Inside this folder there are 2 folders i.e., backend and frontend containing all the required files for the application, a README.md file that covers all the information about the application in detail and a project Report pdf. The backend folder contains 2 folders, application that have all the required python backend files, template that contains HTML template files to be used to send emails to the client, a python file main.py and sqlite database for the user data storage. The frontend folder contains the myapp folder that is the main vue app for the client side. It contains 2 folders, public containing file a html file, index.html and src containing files, App.vue, main.js and 3 folders i.e, components, views and router containing vue components, component views and index.js containing all router paths respectively.

***Fetch Request Routes***

- @app.route('/register', methods=["GET", "POST"])
- @app.route('/login_page', methods=["GET", "POST"])
- @app.route("/dashboard/< string:username>", methods=["GET"])
- @app.route("/logout_page", methods=["GET"])
- @app.route("/dashboard/< string:username>/create_tracker", methods=["POST", "GET"])
- @app.route("/< string:username>/< int:trackerID>/update", methods=["POST"])
- @app.route("/< string:username>/< int:trackerID>/logs", methods=["GET", "POST"])
- @app.route("/< string:username>/< int:trackerID>/delete", methods=["GET"])
- @app.route("/< string:username>/< int:trackerID>/< int:logID>/delete", methods=["GET"])
- @app.route("/< string:username>/< int:trackerID>/< int:logID>/update", methods=["POST"])
- @app.route("/< string:username>/export_trackers", methods=["GET", "POST"]) 
- @app.route("/< string:username>/< int:trackerID>/export_events", methods=["GET", "POST"])


***Video link:*** [Video Link]()