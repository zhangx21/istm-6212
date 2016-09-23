

"""
A filter that split lines of text into one word per line.
"""

import fileinput
import a


def process(line):
    """split lines into one word per line."""
    line = a.findall(r'\w+',line)
    
    for word in line:
        print(word.strip())
            
for line in fileinput.input():
    process(line)
    