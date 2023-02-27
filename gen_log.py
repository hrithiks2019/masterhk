# read data from firebase and write to log file
import time
from datetime import datetime

import pyrebase

phone_id = "OnePlus_OnePlus7_SKQ1211113001"


def get_updated_date_from_db(phone_id):
    config = {
        "apiKey": "AIzaSyB86sJehpBuSWywuE69AowDqzjV2gHuH2w",
        "authDomain": "point-fd22d.firebaseapp.com",
        "databaseURL": "https://point-fd22d-default-rtdb.firebaseio.com",
        "projectId": "point-fd22d",
        "storageBucket": "point-fd22d.appspot.com",
        "messagingSenderId": "953623608984",
        "appId": "1:953623608984:web:849473199a4750b18cdaed",
        "measurementId": "G-3GG6EKS3VE"
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    x = db.get()
    for i in x.each():
        print(i.key())
    # call_log_data = db.child(phone_id).child("call_logs").get()
    # basic_info_data = db.child(phone_id).child("current_state").get()
    # notification_data = db.child(phone_id).child("notification").get()
    # notification_closed_data = db.child(phone_id).child("notification_rmv").get()
    # contact_data = db.child(phone_id).child("contacts").get()


#get_updated_date_from_db(phone_id)
#call_log_data, basic_info_data, notification_data, notification_closed_data, contact_data = get_updated_date_from_db(phone_id)


# datetime_str = '09/19/22 13:55:26'
# datetime_str = '18-02-2023_11:55:45_pm'
# datetime_object = datetime.strptime(datetime_str, '%d-%m-%Y_%I:%M:%S_%p')
# print(datetime_object.strftime('%d-%m-%Y_%H:%M:%S'))
# for i in call_log_data.each():
#     print(i.val())

import os
database_url = os.environ.get('DATABASE_URL')
if database_url is None:
    database_url = "https://point-fd22d-default-rtdb.firebaseio.com"
print(database_url)