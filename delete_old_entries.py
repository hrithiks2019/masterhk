# flask dashboard
import os
import pyrebase
from datetime import datetime
from flask import Flask, render_template, request

phone_idv = os.environ.get('phone_id')
if phone_idv is None:
    phone_idv = "OnePlus_OnePlus7_SKQ1211113001"
    os.environ['phone_id'] = phone_idv

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

app = Flask(__name__, static_folder='static',
            template_folder='templates')

username = ['hrithik', 'admin', 'user']
password = ['Hrithiksipad4', 'M8q913rd', 'M8q913rd@', 'M8q913rd@250599@', 'admin']
current_user = "Hrithik Sriram"

# phone_id = os.environ.get('phone_id')
phone_id = "realme_RE58A5L1_SP1A210812016"
firebase = pyrebase.initialize_app(config)
db = firebase.database()


# delete entries from db
# def delete_old_entries():
#     all_users = db.child("users").get()
#     for user in all_users.each():
#         user_id = user.key()
#         all_entries = db.child("users").child(user_id).child("entries").get()
#         for entry in all_entries.each():
#             entry_id = entry.key()
#             entry_date = entry.val()['date']
#             entry_date = datetime.strptime(entry_date, '%Y-%m-%d')
#             today = datetime.today()
#             if (today - entry_date).days > 30:
#                 db.child("users").child(user_id).child("entries").child(entry_id).remove()


amma_table = db.child('OPPO_OP5303_SP1A210812016').remove()
# mine_table = db.child('OnePlus_OnePlus7_SKQ1211113001').remove()
# sand_table = db.child('realme_RE58A5L1_SP1A210812016').remove()

# call_log_data = db.child(phone_id).child("call_logs").get()
# basic_info_data = db.child(phone_id).child("current_state").get()
# notification_data = db.child(phone_id).child("notification").get()
# notification_closed_data = db.child(phone_id).child("notification_rmv").get()
# contact_data = db.child(phone_id).child("contacts").get()



