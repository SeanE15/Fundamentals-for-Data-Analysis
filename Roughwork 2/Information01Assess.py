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

# get length of paragraph
N = len(alice)

# create below the weights for the 
weights = [alice.count(c) for c in chars] 
twoghts = {c: {d: alice.count(c + d) for d in chars} for c in chars} 

pairs = ' '

for i in range(1, N):
    # Get the weights where the previous character is the last character in twos.
    wt = twoghts[pairs[-1]]
    # turn wt to a list , ordered by chars 
    wt =[wt[c] for c in chars]
    # Randomly pick the next character using those weights.
    nextc = random.choices(chars, weights=wt, k=1000)[-2]
    # Append the character to twos.
    pairs = pairs + nextc

# generate random characters from chars and set string length to 1000 letters.
# = random.choices(chars, weights=weights, k=1000)

# join letters into a string
#gener = ''.join(gener)

print(pairs)
