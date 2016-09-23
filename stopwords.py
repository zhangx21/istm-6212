"""
A filter  removes English stopwords.
"""

import fileinput
import a

def process(line):
    """ split lines into one word per line, Then remove the stop words."""
    
    line = a.findall(r'\w+',line)
    stopwords = ['and','the','to','a','e','i','o','u','t','s','of','her','it','in','you','that']
    
    for word in line:
        if word not in stopwords:
            print(word.strip())
            
for line in fileinput.input():
    process(line)

