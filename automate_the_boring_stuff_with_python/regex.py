#!/usr/bin/env python3

import re

# For using pyperclip you need to install xclip and xsel, this just for
# GNU/Linux
import pyperclip

print("\nTest 1")
sentence = "Hi my phone numbers are 555-453-1546, 666-548-5410 and \
987-562-5465"

match = re.findall(r"\d\d\d-\d\d\d-\d\d\d\d", sentence)
print(match)

print("\nGreedy")
regex = re.compile(r"(\d){1,3}")
print(regex.search(sentence))

print("\nNon Greedy")
regex = re.compile(r"(\d){1,3}?")
print(regex.search(sentence))

# Create a regex for phone numbers
phone_regex = re.compile(r'''
# 123-1233, 555-123-1234, (123) 213-1234, 123-123-1234 ext 1324 or ext. 2134 or
# x 1234
((\d\d\d|\(\d\d\d\)\s)?      # Area code
(-|\s)                      # Dash or space
(\d\d\d)                    # First three digits
(-)                         # Dash
(\d\d\d\d)                  # Last four digits
(\s(ext|ext.|x)\s\d{2,5})?)  # Extension (optional)
''', re.VERBOSE)

# Create a regex for email addresses
email_regex = re.compile(r'''
# stuff@stuff
[a-zA-Z0-9._+]+ # email
@               # @ symbol
[a-zA-Z0-9._+]+ # domain
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
phone_numbers = phone_regex.findall(text)
emails = email_regex.findall(text)

phones = []

for phone in phone_numbers:
    phones.append(phone[0])

# Copy the extracted email/phone to the clipboard

pyperclip.copy("\n".join(phones) + "\n".join(emails))
