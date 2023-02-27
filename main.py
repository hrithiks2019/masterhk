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


def get_updated_date_from_db():
    phone_id = os.environ.get('phone_id')
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    try:
        call_log_data = db.child(phone_id).child("call_logs").get()
        basic_info_data = db.child(phone_id).child("current_state").get()
        notification_data = db.child(phone_id).child("notification").get()
        notification_closed_data = db.child(phone_id).child("notification_rmv").get()
        contact_data = db.child(phone_id).child("contacts").get()
    except (Exception) as e:
        call_log_data = None
        basic_info_data = None
        notification_data = None
        notification_closed_data = None
        contact_data = None
        print("Error in getting data from firebase error:", e)
    return call_log_data, basic_info_data, notification_data, notification_closed_data, contact_data


def get_date_from_db(dbref):
    phone_id = os.environ.get('phone_id')
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    data = db.child(phone_id).child(dbref).get()
    return data


@app.route('/')
def home():
    firebase = pyrebase.initialize_app(config)
    db = firebase.database().get()
    x = [str(i.key()) for i in db.each()]
    return render_template('index_old.html', phone_ids=x)


@app.route("/allnot", methods=['GET', 'POST'])
def allnot():
    phone_id = os.environ.get('phone_id')
    notification = []
    notification_data = get_date_from_db("notification")
    sno = 1
    if notification_data.each is not None:
        for i in notification_data.each():
            temp_date = datetime.strptime(i.val()['date'], '%d-%m-%Y_%I:%M:%S_%p')
            conv_date = (temp_date.strftime('%d-%m-%Y_%H:%M:%S'))
            try:
                appname = i.val()['app_name']
            except KeyError as e:
                appname = "unknown"
            try:                
                title = i.val()['title(from)']
            except KeyError as e:
                title = "unknown"
            try:            
                boby = i.val()['boby']
            except KeyError as e:
                boby = "unknown"
            try:
                more_info = i.val()['more_info']
            except KeyError as e:
                more_info = "unknown"

            notification.append([sno, appname, conv_date, title, boby, more_info])

    notification.sort(key=lambda x: x[2], reverse=True)
    for i in notification:
        i[0] = sno
        sno += 1

    return render_template('allnot.html', notification=notification, total_count=sno,
                           today_count="20",
                           current_battery="20",
                           last_sync_time="10:30 PM", user_name=current_user,
                           user_type="Master Blaster")


@app.route("/watnot", methods=['GET', 'POST'])
def watnot():
    phone_id = os.environ.get('phone_id')
    notification = []
    notification_data = get_date_from_db("notification")
    sno = 1
    if notification_data.each is not None:
        for i in notification_data.each():
            if i.val()['app_name'] == 'whatsapp':
                temp_date = datetime.strptime(i.val()['date'], '%d-%m-%Y_%I:%M:%S_%p')
                conv_date = (temp_date.strftime('%d-%m-%Y_%H:%M:%S'))
                try:
                    appname = i.val()['app_name']
                except KeyError as e:
                    appname = "unknown"
                try:
                    title = i.val()['title(from)']
                except KeyError as e:
                    title = "unknown"
                try:
                    boby = i.val()['boby']
                except KeyError as e:
                    boby = "unknown"
                try:
                    more_info = i.val()['more_info']
                except KeyError as e:
                    more_info = "unknown"

                notification.append([sno, appname, conv_date, title, boby, more_info])

    notification.sort(key=lambda x: x[2], reverse=True)
    for i in notification:
        i[0] = sno
        sno += 1
    return render_template('watnot.html', notification=notification, total_count=sno,
                           today_count="20",
                           current_battery="20",
                           last_sync_time="10:30 PM", user_name=current_user,
                           user_type="Master Blaster")


@app.route("/insnot", methods=['GET', 'POST'])
def insnot():
    phone_id = os.environ.get('phone_id')
    notification = []
    notification_data = get_date_from_db("notification")
    sno = 1
    if notification_data.each is not None:
        for i in notification_data.each():
            if i.val()['app_name'] != 'whatsapp':
                temp_date = datetime.strptime(i.val()['date'], '%d-%m-%Y_%I:%M:%S_%p')
                conv_date = (temp_date.strftime('%d-%m-%Y_%H:%M:%S'))
                try:
                    appname = i.val()['app_name']
                except KeyError as e:
                    appname = "unknown"
                try:
                    title = i.val()['title(from)']
                except KeyError as e:
                    title = "unknown"
                try:
                    boby = i.val()['boby']
                except KeyError as e:
                    boby = "unknown"
                try:
                    more_info = i.val()['more_info']
                except KeyError as e:
                    more_info = "unknown"

                notification.append([sno, appname, conv_date, title, boby, more_info])

    notification.sort(key=lambda x: x[2], reverse=True)
    for i in notification:
        i[0] = sno
        sno += 1
    return render_template('insnot.html', notification=notification, total_count=sno,
                           today_count="20",
                           current_battery="20",
                           last_sync_time="10:30 PM", user_name=current_user,
                           user_type="Master Blaster")


@app.route("/calllog", methods=['GET', 'POST'])
def call_log():
    phone_id = os.environ.get('phone_id')
    recent_call = []
    call_log_data = get_date_from_db("call_logs")
    no_of_call_logs = len(list(call_log_data.each()))
    sno = 1
    total_incoming = 0
    total_outgoing = 0
    total_missed = 0
    if call_log_data.each is not None:
        for i in call_log_data.each():
            temp_date = datetime.strptime(i.val()['date'], '%d-%m-%Y_%I:%M:%S_%p')
            conv_date = (temp_date.strftime('%d-%m-%Y_%H:%M:%S'))
            try:
                name = i.val()['name']
            except KeyError as e:
                name = "<check from contacts>"
            try:
                number = i.val()['number']
            except KeyError as e:
                number = ""
            try:
                typex = i.val()['type']
            except KeyError as e:
                typex = ""
            try:
                duration = i.val()['duration']
            except KeyError as e:
                duration = "0"

            recent_call.append([sno, conv_date, name, number, typex, duration])
            if i.val()['type'] == 'Incoming':
                total_incoming += 1
            elif i.val()['type'] == 'Outgoing':
                total_outgoing += 1
            elif i.val()['type'] == 'Missed':
                total_missed += 1
            elif i.val()['type'] == 'Outgoing' and i.val()['duration'] == '0':
                total_missed += 1

    recent_call.sort(key=lambda x: x[1], reverse=True)
    sno = 1
    for i in recent_call:
        i[0] = sno
        sno += 1

    return render_template('call_logs.html', recent_call=recent_call, total_count=str(no_of_call_logs),
                           total_incoming=total_incoming,
                           total_outgoing=total_outgoing,
                           total_missed=total_missed, user_name=current_user,
                           user_type="Master Blaster")


@app.route("/contacts", methods=['GET', 'POST'])
def contacts():
    contacts = []
    phone_id = os.environ.get('phone_id')
    contact_data = get_date_from_db("contacts")
    sno = 1
    if contact_data.each() is not None:
        for i in contact_data.each():
            name, number = i.key(), i.val()
            contacts.append([sno, name, number])
            sno += 1

    return render_template('contacts.html', contacts=contacts, user_name=current_user,
                           user_type="Master Blaster")


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    recent_call = []
    recent_notification = []
    phone_id = os.environ.get('phone_id')
    dash_call_time = 0
    me_call_time = 0
    oth_call_time = 0
    call_log_data, basic_info_data, notification_data, notification_closed_data, contact_data = \
        get_updated_date_from_db()
    sno = 1
    if call_log_data.each is not None:
        for i in call_log_data.each():
            temp_date = datetime.strptime(i.val()['date'], '%d-%m-%Y_%I:%M:%S_%p')
            conv_date = (temp_date.strftime('%d-%m-%Y_%H:%M:%S'))
            try:
                name = i.val()['name']
            except KeyError as e:
                name = "<check from contacts>"
            try:
                number = i.val()['number']
            except KeyError as e:
                number = ""
            try:
                typex = i.val()['type']
            except KeyError as e:
                typex = ""
            try:
                duration = i.val()['duration']
            except KeyError as e:
                duration = "0"

            recent_call.append([sno, conv_date, name, number, typex, duration])
            if ('kesa' in str(name).lower()) or ('ganesh' in str(name).lower() or
                                                            ('7904100689' in str(i.val()['number']).lower()) or
                                                            ('9629472386' in str(i.val()['number']).lower())):
                dash_call_time += 1
            elif (('hrit' in str(name).lower()) or ('6381746332' in str(i.val()['number']).lower()) or (
                    '7904170564' in str(i.val()['number']).lower())):
                me_call_time += 1
            else:
                oth_call_time += 1

    # notification data
    sno = 1
    if notification_data.each is not None:
        for i in notification_data.each():
            temp_date = datetime.strptime(i.val()['date'], '%d-%m-%Y_%I:%M:%S_%p')
            conv_date = (temp_date.strftime('%d-%m-%Y_%H:%M:%S'))
            try:
                appname = i.val()['app_name']
            except KeyError as e:
                appname = "unknown"
            try:                
                title = i.val()['title(from)']
            except KeyError as e:
                title = "unknown"
            try:            
                boby = i.val()['boby']
            except KeyError as e:
                boby = "unknown"
            try:
                more_info = i.val()['more_info']
            except KeyError as e:
                more_info = "unknown"
            recent_notification.append([sno, appname, conv_date, title, boby, more_info])            
            sno += 1
    if basic_info_data.each is not None:
        for i in basic_info_data.each():
            if i.key() == "BATTERY":
                current_battery = i.val()
            elif i.key() == "LAST_UPDATE_EPOCH":
                temp_date = datetime.strptime(i.val(), '%d-%m-%Y_%I:%M:%S_%p')
                last_active_time = (temp_date.strftime('%D-%M-%Y %H:%M:%S'))

            elif i.key() == 'DEVICE_IP':
                device_ip = i.val()
            elif i.key() == 'DEVICE_NW':
                device_nw = i.val()

    # sort the recent call and notification list based on date
    recent_call.sort(key=lambda x: x[1], reverse=True)
    recent_notification.sort(key=lambda x: x[2], reverse=True)
    # manual Serial num change
    sno = 1
    for i in recent_call:
        i[0] = sno
        sno += 1

    sno = 1
    for i in recent_notification:
        i[0] = sno
        sno += 1
    x = len(recent_call) + len(recent_notification)
    last_call_time = recent_call[0][1]
    return render_template('index.html', user_name=current_user,
                           user_type="Master Blaster",
                           recent_call=recent_call[:5],
                           recent_notification=recent_notification[:5],
                           current_battery=current_battery,
                           last_active_time=last_active_time,
                           last_call_time=last_call_time,
                           device_ip=device_ip,
                           device_nw=device_nw,
                           today_count=x, me_call_time=me_call_time,
                           other_call_time=oth_call_time,
                           dash_call_time=dash_call_time)


@app.route('/login', methods=['GET', 'POST'])
def shortenurl():
    op = "Login Failed, please Try Again"
    firebase = pyrebase.initialize_app(config)
    db = firebase.database().get()
    x = [str(i.key()) for i in db.each()]
    if request.method == 'POST':
        user = request.form['username']
        passwd = request.form['password']
        phone = request.form['phone']
        os.environ['phone_id'] = phone
        phone_id = os.environ.get('phone_id')
        if (user in username) and (passwd in password):
            op = "Login Successful"
            recent_call = []
            recent_notification = []
            dash_call_time = 0
            me_call_time = 0
            oth_call_time = 0
            call_log_data, basic_info_data, notification_data, notification_closed_data, contact_data = \
                get_updated_date_from_db()
            sno = 1
            if call_log_data.each is not None:
                for i in call_log_data.each():
                    temp_date = datetime.strptime(i.val()['date'], '%d-%m-%Y_%I:%M:%S_%p')
                    conv_date = (temp_date.strftime('%d-%m-%Y_%H:%M:%S'))
                    try:
                        name = i.val()['name']
                    except KeyError as e:
                        name = "<check from contacts>"
                    try:
                        number = i.val()['number']
                    except KeyError as e:
                        number = ""
                    try:
                        typex = i.val()['type']
                    except KeyError as e:
                        typex = ""
                    try:
                        duration = i.val()['duration']
                    except KeyError as e:
                        duration = "0"

                    recent_call.append([sno, conv_date, name, number, typex, duration])
                    if ('kesa' in str(name).lower()) or ('ganesh' in str(name).lower() or
                                                                    ('7904100689' in str(i.val()['number']).lower()) or
                                                                    ('9629472386' in str(i.val()['number']).lower())):
                        dash_call_time += 1
                    elif ('hrit' in str(name).lower()) or ('6381746332' in str(i.val()['number']).lower()) or (
                            '7904170564' in str(i.val()['number']).lower()):
                        me_call_time += 1
                    else:
                        oth_call_time += 1

            # notification data
            sno = 1
            if notification_data.each is not None:
                for i in notification_data.each():
                    temp_date = datetime.strptime(i.val()['date'], '%d-%m-%Y_%I:%M:%S_%p')
                    conv_date = (temp_date.strftime('%d-%m-%Y_%H:%M:%S'))
                    recent_notification.append(
                        [sno, i.val()['app_name'], conv_date, i.val()['title(from)'], i.val()['boby'],
                         i.val()['more_info']])
                    sno += 1
            if basic_info_data.each is not None:
                for i in basic_info_data.each():
                    if i.key() == "BATTERY":
                        current_battery = i.val()
                    elif i.key() == "LAST_UPDATE_EPOCH":
                        temp_date = datetime.strptime(i.val(), '%d-%m-%Y_%I:%M:%S_%p')
                        last_active_time = (temp_date.strftime('%D-%M-%Y %H:%M:%S'))

                    elif i.key() == 'DEVICE_IP':
                        device_ip = i.val()
                    elif i.key() == 'DEVICE_NW':
                        device_nw = i.val()

            # manual Serial num change
            sno = 1
            for i in recent_call:
                i[0] = sno
                sno += 1

            sno = 1
            for i in recent_notification:
                i[0] = sno
                sno += 1

            # sort the recent call and notification list based on date
            recent_call.sort(key=lambda x: x[1], reverse=True)
            recent_notification.sort(key=lambda x: x[2], reverse=True)
            x = len(recent_call) + len(recent_notification)
            last_call_time = recent_call[0][1]
            return render_template('index.html', user_name=current_user,
                                   user_type="Master Blaster",
                                   recent_call=recent_call[:5],
                                   recent_notification=recent_notification[:5],
                                   current_battery=current_battery,
                                   last_active_time=last_active_time,
                                   last_call_time=last_call_time,
                                   device_ip=device_ip,
                                   device_nw=device_nw,
                                   today_count=x, me_call_time=me_call_time,
                                   other_call_time=oth_call_time,
                                   dash_call_time=dash_call_time)

        else:
            return render_template('index_old.html',error=op, phone_ids=x)
    else:
        return render_template('index_old.html', phone_ids=x)


app.run(host='0.0.0.0',debug=True, port=5200)
