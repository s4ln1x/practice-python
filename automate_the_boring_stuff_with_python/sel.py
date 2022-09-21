#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/bin/firefox')
browser = webdriver.Firefox(firefox_binary=binary)

# Open web pages
browser.get('https://www.amazon.com.mx')

# Find de element you want
# You can use elements if you want or need browser.find_elements_by_css_selector('stuff of css selectors')
elem = browser.find_element_by_css_selector('stuff of css selectors')

# Click the element
elem.click()

# Send keys to the text box
elem.send_keys()

# Give submit to a form
elem.submit()

# Control the browser itself
browser.back()
browser.forward()
browser.refresh()
browser.quit()
