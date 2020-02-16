# Here we will follow these steps for our member dues remainder through Email
'''
•	 Read data from an Excel spreadsheet.
•	 Find all members who have not paid dues for the latest month.
•	 Find their email addresses and send them personalized reminders
'''

import sys, smtplib, openpyxl

wb = openpyxl.load_workbook("duesrecords.xlsx")
sheet = wb.get_sheet_by_name('Sheet1')

lastcol = sheet.get_highest_column()
latestmonth = sheet.cell(row= 1, column =lastcol).value

# Extract name and email of the people having dues this latest month
unpaidMembers = {}
for r in range(2, sheet.get_highest_row()+1):
    payment = sheet.cell(row= r, column = lastcol).value
    if payment != 'paid':
        name= sheet.cell(row= r, column = 1).value
        email = sheet.cell(row=r, column = 2).value
        unpaidMembers[name] = email

# Log into Email Account (587 is the port number)
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
# Enter the password as a command line argument each time you run the program 
# to avoid saving your password in the source code.
smtpObj.login('my_gmail_address@gmail.com', sys.argv[1])

#Send out remainder emails
for name, email in unpaidMembers.items():
    body = "Subject: %s dues unpaid. \nDear %s,\nRecords shows that you have not paid dues for %s. Please make payment as soon as possible. Thank you!" % (latestmonth, name, latestmonth)
    sendmailstatus= smtpObj.sendmail('myemailaddress@gmail.com', email, body)

    if sendmailstatus != {}:
        print("There was a problem sending email to %s: %s" % (email, sendmailstatus))

smtpObj.quit()