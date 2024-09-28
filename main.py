#Project: Sent myself a motivational quote on Mondays
import smtplib
import datetime as dt
import random

#check thoroughly for typos before running the code
#Modify the security settings for all accounts
#Get an app password from both gmail and Yahoo or Outlook
#Check in spam folder for the email
MY_EMAIL = "webtestdays@gmail.com"
MY_PASSWORD = "fuzohjlewztegsaq"
#Will retry setting up this test account in 1 hour
OTHER_EMAIL = "webtestdays@outlook.com"
OTHER_PASSWORD = "dozezydwweozradj"

#This gives a highly accurate representation of the time RIGHT NOW
now = dt.datetime.now()
#Gives an int, not a day
weekday = now.weekday()
#def get_day():
    #To test code, set it for today's day of the week
    #For the Monday file, this should be 0
if weekday == 3:
        # open the quotes.text file to obtain a list of quotes
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        # Use the random module to pick a random quote
        quote = random.choice(all_quotes)
    #print(quote)<--TEST

    # Use smtplib to send the email to yourself
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{quote}."
        )















