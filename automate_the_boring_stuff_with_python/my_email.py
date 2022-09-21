#!/usr/bin/env python3
# Send email
import smtplib
import imapclient
import pyzmail
from datetime import date

conn = smtplib.SMTP("smtp.gmail.com", 587)

# You need to call this function to start the connection
conn.ehlo()

# Start the tls encryption
conn.starttls()

# Login, You can try ;) but the password was changed after I finish o.O
# You need to activate the less secure apps login to this to work
conn.login("botmantis@gmail.com", "JRe5q2egmhUrVsh")

# Send an email
conn.sendmail(
    "botmantis@gmail.com",
    "botmantis@gmail.com",
    "Subject: Hey pops whats up... \n\nWell I would like to say Hi to you, \
    this is fully automated pops, Hell Yeah!!!!\n\nBest Regards!!!\nSalvador \
    Gudino",
)

# Close connection
conn.quit()

# Manage botmantis inbox

conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)
conn.login("botmantis@gmail.com", "JRe5q2egmhUrVsh")

conn.select_folder("INBOX", readonly=True)

# This unique IDs represents an email
UIDS = conn.search(["SINCE", date(2020, 1, 1)])
print(f"List of emails = {UIDS}")

# Get the data from a single email
raw_message = conn.fetch([UIDS[0]], ["BODY[]", "FLAGS"])
message = pyzmail.PyzMessage.factory(raw_message[UIDS[0]][b"BODY[]"])

# Get the subject
print(f"Subject of the first email = {message.get_subject()}")

# Get addresses
print(f'This meesage is from {message.get_addresses("from")}')
print(f'This meesage is to {message.get_addresses("to")}')

# Get email body
print(message.text_part.get_payload().decode("UTF-8"))

# The charset of the message is here, but sometimes is just None
print(f"The charset of the message is {message.text_part.charset}")

# The email can be just text or html
print(f"This email has html part? = {message.html_part}")

# List all the available folders
print("List all the available folders")
print(conn.list_folders())

# Delete emails
conn.select_folder("INBOX", readonly=False)
UIDS_2 = conn.search(["SINCE", date(2020, 1, 1)])
conn.delete_messages([UIDS_2[0]])

# Show that the first element of the emails was deleted
conn.select_folder("INBOX", readonly=True)
UIDS_3 = conn.search(["SINCE", date(2020, 1, 1)])
print(f"List of remaining emails = {UIDS_3}")
