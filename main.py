import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day = now.weekday()
with open("quotes.txt") as quotes:
    list_q = [item for item in quotes]
# you need to enter your mail and password if you want this to work
my_email = "mail"
password = "pass"


def send_m():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
# instead rec.mail you need to write the receiving email address
    connection.sendmail(from_addr=my_email, to_addrs="rec.mail",
                        msg=f"Subject:Motivation \n\n {list_q[random.randint(0, len(list_q))]}")
    connection.close()


if day == 0:
    send_m()
