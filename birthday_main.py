##################### Normal Starting Project ######################
#This program sends emails to friends and family
#on their birthday
import smtplib
from datetime import datetime
import pandas as pd
import random

#Constants of my email and app password
MY_EMAIL = "webtestdays@gmail.com"
MY_PASSWORD = "fuzohjlewztegsaq"
# 1. Update the birthdays.csv with your friends & family's details.
# Done: Test information only using today's date

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

# HINT 2: Use pandas to read the birthdays.csv
data = pd.read_csv("birthdays.csv")
# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
#test
#print(birthdays_dict)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    #Randomly choosing among 3 letters so they are not all the same
    file_path = f".\letter_templates\letter{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addr=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}."
        )

