#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def get_sortname(image):
  """
  Returns a string with the correct filename of the image that we want to use
  to sort.
  File structure is as x-x-x-filename.jpg where the 'x-' can be 1 or n.
  """
  return image.split('-')[-1]


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  protocol = 'http://'
  hostname = filename[filename.index('_') + 1:]
  with open(filename, 'r') as fn:
    images_pathnames = re.findall(r'.+GET (.+\.jpg)', fn.read())
  path = os.path.dirname(images_pathnames[0])

  # Remove the basename of the url, remove dupplicates and sort the list in
  # increasing order
  images = list(set(map(os.path.basename, images_pathnames)))
  images = sorted(images, key=get_sortname)

  urls = [protocol + hostname + os.path.join(path, image) for image in images]
  return urls


def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

  index = file(os.path.join(dest_dir, 'index.html'), 'w')
  index.write('<html>\n')
  index.write('\t<body>\n')

  filename = 'img'
  for i, url in enumerate(img_urls):
    print 'Retrieving url %s ...' % url
    fn = filename + str(i)
    pathname = os.path.join(dest_dir, fn)
    urllib.urlretrieve(url, pathname)
    index.write('<img src=%s>' % fn)

  index.write('\n\t</body>\n')
  index.write('</html>')
  index.close()


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
