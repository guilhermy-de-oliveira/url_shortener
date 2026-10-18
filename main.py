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

def shortening():
    # Create Shortener Object
    shortener = pyshorteners.Shortener()
    # Use the shortener to shorten the URL
    shortened_url = shortener.tinyurl.short(url)

    # Clean past line
    print('\033[1A' + '\x1b[2K', end='')

    # Message containing the URL submitted by the user and its shortened version.
    print("Original URL: ", url)
    print("Shortened URL: ", shortened_url)

try:
    shortening()
except Exception as e:
    # Clean past line
    print('\033[1A' + '\x1b[2K', end='')
    print(f"The shortener hasn't worked correctly ['{url}']: {e}")