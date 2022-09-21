#!/usr/bin/env python3

import requests

# Download Romeo and Juliet
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# Raise and error if the download of the file failed
res.raise_for_status()

print(f'This is the status code of the download = {res.status_code}')

with open('requests.log', 'wb') as fn:
    for chunk in res.iter_content(100000):
        fn.write(chunk)

