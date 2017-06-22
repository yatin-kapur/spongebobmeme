import string
import numpy as np

punc = string.punctuation
punc += ' '         # adding space to punctuation so that it doesn't have two consecutive things

def memeit(phrase):
    meme = ''             # the memeable prase to return
    for i in phrase:   # going through the string and changing it to caps
        if np.random.randint(0,2): # choose either true or false (1 or 0)
            meme += i.lower()     # append the uppercase letter to return value
        else:
            meme += i.upper()     # append the lowercase letter to return value

    return meme

phrase = input("Enter the meme-able phrase:\n")       # asking for meme phrase
phrase = phrase.lower()             # convert the phrase to all lower for consistency

meme = memeit(phrase)           # passing value to function

tweet = open("tweet.txt", "w")          # create tweet file
tweet.write(phrase + "\n")
tweet.write("\n" + meme)                # writing initial phrase and then meme in it




