import urllib.request

book_url = 'https://www.gutenberg.org/files/11/11-0.txt'

book = list(urllib.request.urlopen(book_url))

book = [line.decode('utf-8-sig').strip() for line in book]

para= ' '.join(book[58:63])

print(para)

# Let's lower-case it.
alice = para.lower()

# All letters and a space.
chars = 'abcdefghijklmnopqrstuvwxyz '

# And strip anything that is not a letter or space.
alice = ''.join([c for c in alice if c in chars])

# Show the paragraph now.
print(alice)

# For doing (pseudo-)random things in Python.
import random

# Print a random character, for example.
print(random.choice(chars))

# Get the length of alice.
N = len(alice)

# Generate N random characters from chars.
gener = random.choices(chars, k=N)

# Join them together in a string.
gener = ''.join(gener)

# Print.
print(gener)

# Get the whole book in one big string.
sbook = ''.join(book[26:]).lower()

# Create the weights - count the occurences of each character in the whole book.
weights = [sbook.count(c) for c in chars]

# Show the weights.
weights

# Generate a string using those weights.
wgenr = random.choices(chars, weights=weights, k=N)

# Join them together in a string.
wgenr = ''.join(wgenr)

# Print.
print(wgenr)


# Create the weights.
twoghts = {c: {d: sbook.count(c + d) for d in chars} for c in chars}

# Show the weights.
twoghts

# Loop through our character set.
for i in range(len(chars)):
    # Print the character and how many times it appears in Alice in Wonderland.
    print(f'{chars[i]}: {weights[i]}')

# Start with space.
pairs = ' '

# Do the following N-1 times.
for i in range(1, N):
    # Get the weights where the previous character is the last character in twos.
    wt = twoghts[pairs[-1]]
    # Turn wt into a list, ordered by chars.
    wt = [wt[c] for c in chars]
    # Randomly pick the next character using those weights.
    nextc = random.choices(chars, weights=wt, k=1)[0]
    # Append the character to twos.
    pairs = pairs + nextc
