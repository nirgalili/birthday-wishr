##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random as rnd
import pandas as pd

my_email = "pvcnya@gmail.com"
password = "pvcnya2013"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

df = pd.read_csv("birthdays.csv")

df_mail_name = df.drop(columns=["year", "month", "day"])

bool_df = df.isin([year, month, day])


bool_df_time_only = bool_df.drop(columns=["name", "email"])

new_df = df_mail_name.join(bool_df_time_only)


for (index, row) in new_df.iterrows():
    if row.year == True and row.month == True and row.day == True:
        row_index = index


birthday_kid_email = df.iloc[row_index]["email"]
birthday_kid_name = df.iloc[row_index]["name"]
print(birthday_kid_email)
print(birthday_kid_name)




# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




