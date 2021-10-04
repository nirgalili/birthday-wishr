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
# year = now.year
month = now.month
day = now.day

df = pd.read_csv("birthdays.csv")
print(df)
df_mail_name_year = df.drop(columns=["month", "day"])

bool_df = df.isin([month, day])
print(bool_df)

bool_df_time_only = bool_df.drop(columns=["name", "email", "year"])

new_df = df_mail_name_year.join(bool_df_time_only)

row_index = None
for (index, row) in new_df.iterrows():
    if row.month and row.day:
        row_index = index

if row_index is None:
    pass
else:
    birthday_kid_email = df.iloc[row_index]["email"]
    birthday_kid_name = df.iloc[row_index]["name"]
    print(birthday_kid_email)
    print(birthday_kid_name)

    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    letters_list = [f"letter_{x+1}.txt" for x in range(3)]
    print(letters_list)

    picked_letter_file = rnd.choice(letters_list)
    print(picked_letter_file)

    with open(f"letter_templates/{picked_letter_file}", "r") as file:
        filedata = file.read()

    filedata =filedata.replace("[NAME]", birthday_kid_name)

    with open("letter_to_send.txt", "w") as file:
        file.write(filedata)

    # 4. Send the letter generated in step 3 to that person's email address.

    # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #     connection.starttls()
    #     connection.login(user=my_email, password=password)
    #     connection.sendmail(from_addr=my_email,
    #                         to_addrs="nirgalili1@gmail.com",
    #                         msg=f"Subject:Happy Birthday {birthday_kid_name}\n\n{filedata}")


