#!/usr/bin/env python3

import webbrowser
import argparse

# Open the default web browser with the url you want
parser = argparse.ArgumentParser(description='Open any web address you want!')
parser.add_argument('address', help='Web address you want to open')
parser.add_argument('-s', '--subdomain', default='www', help='Which subdomain has your web address')
parser.add_argument('-d', '--domain', default='com', help='Which domain has your web address')
args = parser.parse_args()

# Open any address you want
webbrowser.open('https://' + args.subdomain + '.' + args.address + '.' + args.domain + '/')
