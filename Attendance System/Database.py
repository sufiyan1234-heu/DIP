import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://face-recognition-attenda-3d688-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')#reference path of database

data = {
    "963852":
        {
           "name" : "Elon Musk",
           "major" : "SpaceX",
           "starting_year" : "2020",
           "total_attendance" : 7,
           "standing" : "G",
           "year" : 3,
           "last_attendance_time":"2022-12-11 00:54:34"
        },
        "456739":
        {
           "name" : "Sufiyan",
           "major" : "DIP",
           "starting_year" : "2020",
           "total_attendance" : 2,
           "standing" : "G",
           "year" : 3,
           "last_attendance_time":"2022-12-11 00:14:34"
        },
         "345678":
        {
           "name" : "Rida Usman",
           "major" : "AI",
           "starting_year" : "2020",
           "total_attendance" : 0,
           "standing" : "B",
           "year" : 3,
           "last_attendance_time":"2022-12-11 00:14:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)