# Title: "Adapt the code above to generate a 1000 character long string with weights based on the previous two characters."
# Lecturer: Dr Ian Mc Loughlin
# Author: Sean Elliott 

# We start by importing the text file from our source using the built-in import function.

import urllib.request
import random 

# The URL of a text version of Alice in Wonderland.
url = 'https://www.gutenberg.org/files/11/11-0.txt'

# We then convert the file to a list.
book = list(urllib.request.urlopen(url))

# Decode the lines and strip the line endings.
book = [line.decode('utf-8-sig').strip() for line in book]

# I then hand pick a paragraph (avoiding the preamble at the start, index, table fo contents etc).
paragraph = ' '.join(book[85:89])

# Define parameters with which we want to form the 1000 character long string.
chars = 'abcdefghijklmnopqrstuvwxyz '

# Tidy text file by ensuring everythign lowercase
alice = paragraph.lower() 

# Strip punctuation 
alice = ''.join([c for c in alice if c in chars])

#test print
print (alice) 
