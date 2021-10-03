import smtplib
import datetime as dt
import random as rnd

my_email = "pvcnya@gmail.com"
password = "pvcnya2013"

now = dt.datetime.now()
year = now.year
day_of_the_week = now.weekday()
print(day_of_the_week)

with open("quotes.txt", "r") as file:
    quotes = file.readlines()
    # print(len(quotes))
rand_line = rnd.choice(quotes)
print(rand_line)


if day_of_the_week == 6:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="nirgalili1@gmail.com",
                            msg=f"Subject:Happy Monday\n\n{rand_line}")




