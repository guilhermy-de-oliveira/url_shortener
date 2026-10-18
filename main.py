# First of all, thanks to Leandro Hirt! He created the tutorial I used to build this application!
# Link to the tutorial: https://www.youtube.com/watch?v=5uflDBAEDFs

# DEPENDÊNCIES
#
# Python 3.15.0
# pip install pyshorteners
#

# TinyUrl Shortener Library
import pyshorteners

# Title
print("URL SHORTENER")

# User input
url = input("Insert a URL: ")

# Clean past line
print('\033[1A' + '\x1b[2K', end='')
# Process message
print("Shortening...")

# Create Shortener Object
shortener = pyshorteners.Shortener()
# Use the shortener to shorten the URL
shortened_url = shortener.tinyurl.short(url)

# Clean past line
print('\033[1A' + '\x1b[2K', end='')

# Message containing the URL submitted by the user and its shortened version.
print("Original URL: ", url)
print("Shortened URL: ", shortened_url)