import os
from DataRetrieval import AutoDataRetrieval
import smtplib, ssl
from email.mime.text import MIMEText
import time
from tkinter import *
import threading

root = Tk()

clock_lbl = Label(root, text='Clock Loading')
clock_lbl.pack()
msg_lbl = Label(root, text='No messages have been sent.')
msg_lbl.pack()
adr = AutoDataRetrieval()
print("Enter email")
email = input()


def start():
    print("NHL Team Standing Updater Is Running")
    while True:

        time.sleep(1)
        time_now = time.strftime("%H:%M:%S")
        clock_lbl.config(text=time_now)
        if int(time.strftime("%H")) % 4 == 0 and int(time.strftime("%M")) % 60 == 0 and int(time.strftime("%S")) % 60 == 0:
            send_standing()
            msg_lbl.config(text=f"Last message sent at {time_now}")


def send_standing():
    i = 0
    teams = adr.get_team_order()
    points = adr.get_points()
    my_rank = ''
    my_team = ''
    my_points = ''
    body_of_email = f"<p><br>NHL League Standings<br> </p> "
    team_msg = f''
    for team in teams:
        team_msg = f"\n<p>{team} is ranked # {i + 1} with {points[i]} points.</p>"
        if team == "Tampa Bay Lightning":
            team_msg = f"\n<p style='background-color: #149bf5; color:white; font-size:16px;'>{team} is ranked # {i + 1} with {points[i]} points.</p> "
        if team == "Philadelphia Flyers":
            team_msg = f"\n<p style='background-color: #f5a700; color:white; font-size:16px;'>{team} is ranked # {i + 1} with {points[i]} points.</p>"
        body_of_email += team_msg
        i += 1

    teams.clear()
    points.clear()
    receivers = ["dmobley0608@gmail.com", "4707682068@txt.att.net"]

    msg = MIMEText(body_of_email, 'html')
    msg['Subject'] = "Your Team Standings"
    msg['From'] = ''
    msg['To'] = ','.join(receivers)

    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)

    s.login(user=email, password="lajhqdigmtjjiyhx")
    s.sendmail(email, receivers, msg.as_string())
    s.quit()


time.sleep(5)
thread2 = threading.Thread(target=start)
thread2.daemon = True
thread2.start()

root.mainloop()
