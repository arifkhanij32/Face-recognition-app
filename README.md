Face Recognition System

Overview

This is a Face Recognition System built using Flask, OpenCV, dlib, face-recognition, and PostgreSQL. The system allows users to:

Upload an image with a name, which is stored in a PostgreSQL database.

Upload a video, where the system detects faces and compares them with the stored faces.

If a match is found, the system displays the name and the corresponding image.

Features

✅ Face detection using OpenCV & dlib✅ Face recognition using face-recognition module✅ Video input processing✅ Store face encodings in PostgreSQL using Pickle✅ Flask-based frontend for easy interaction✅ Automatic database migrations using Flask-Migrate

Technologies Used

Backend: Flask, SQLAlchemy, OpenCV, dlib, face-recognition, Pickle

Database: PostgreSQL

Frontend: HTML, CSS (Bootstrap)

Server: Flask

Installation Guide

Prerequisites

Ensure you have Python 3.7+ installed along with PostgreSQL.

Step 1: Clone the Repository

git clone https://github.com/your-repo/face_recognition_project.git
cd face_recognition_project

Step 2: Create a Virtual Environment

python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate    # For Windows

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Configure PostgreSQL Database

Open PostgreSQL and create a new database:

CREATE DATABASE face_recognition_db;

Update database.py with your PostgreSQL credentials:

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://username:password@localhost/face_recognition_db"

Step 5: Run Database Migrations

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Step 6: Run the Application

python app.py

The app will run on http://127.0.0.1:5000/.

Usage Guide

1️⃣ Upload an Image

Go to http://127.0.0.1:5000/

Enter a name and upload an image.

Click Upload. This stores the image and its encoding in the database.

2️⃣ Upload a Video for Recognition

Go to the same page.

Upload a video file.

The system detects faces and compares them with stored faces.

If a match is found, the matched name and image are displayed.

Project Structure

face_recognition_project/
│── app.py              # Main application file
│── database.py         # Database configuration & models
│── face_recognition.py # Face detection & comparison logic
│── templates/          # HTML templates
│   ├── index.html      # Main upload form
│   ├── result.html     # Result display page
│── static/             # CSS & JavaScript
│   ├── styles.css      # Styling file
│── migrations/         # Flask-Migrate migration files (Auto-created)
│── requirements.txt    # Required packages
│── README.md           # Project documentation

Troubleshooting

1. Flask App Not Running

Check if Flask is installed:

pip install flask

Ensure you have set up the database correctly.

2. Face Not Detected in Video

Ensure good lighting conditions.

Try using a high-resolution image for better recognition.

3. Database Connection Issues

Verify your PostgreSQL service is running.

Double-check your database credentials in database.py.




# dlib
Hi Friends, there is all dlib wheel files for python version 7 to 11.. For more versions contact me!!!
Friends, Today i'm gona show you how to install dlib and face-recognition python library (pakages) without any errors just in 3 steps. Faild to build dlib OR Failed building wheel for dlib problems solved.

This covers following topis:
Failed to build dlib | failed building wheel for dlib | face recognition installation error solved | pip install dlib error | pip install cmake error | pip install face-recognition error | dlib library install problem solved | face recognition python library install problem solved | How to install dlib | How to install face recognition library | how to install cmake library | error legacy install failure | not supported wheel for dlib

***You can also fix all type of Problems related to dlib***

Solutions: Just Follow these three Steps

Step-1
pip install cmake

Step-2 
pip install  dlib

***if any error try this***

Download the Files from here... Then Open command prompt (cmd) in the same folder where the file is located. Type in cmd...

pip install (copy file name and paste here) 

Step-3 
pip install face-recognition

***Note: the whl dlib files cp37 means CPython 3.7,  cp38 means CPython 3.8 and so on.***
