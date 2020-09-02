#!y /usr/bin/env python3

# Author: Bryan Ramos
# Course: Theory of Operating Systems
# Instructors: Eric Freudenthal and David Pruitt
# Assignment: Lab Python Introduction
# Assignment Description: Count the number of words in a file. The program takes to file names as input
# (arguments), reads the first, and then writes all word and the amount of times they occur to second file.

import os  # check if file exists
import re  # for regular expression
import sys # command line arguments

# set input and output files and check if input is valid, if not terminate program
# 3 args necessary from system
if len(sys.argv) != 3: 
    print("Incorrect input. Correct input usage for this program: wordCount.py <input file> <output file> ")
    exit()

inputFilename = sys.argv[1]  # save name of input file
outputFileName = sys.argv[2] # save name of output file
words = {}                   # python dictionary - where words & counts will be stored

# check to make sure the input file exists
if not os.path.exists(inputFilename):
    print("The file %s does not exist!" % inputFilename);
    exit()

with open(inputFilename, 'r') as thisFile:
    for line in thisFile:                             # for every line in file
        line = line.strip()                           # remove newline characters
        for word in re.split("[\"'\s\t.,-;:]", line): # split at spaces, punctuation
            if word.lower() == "":
                continue
            if word.lower() in words:                 # if word is already in words dict, add 1 to count for that
                words[word.lower()] += 1
            else:                                   
                words[word.lower()] = 1 

# write to output file
# w+ will overwrite the existing file if it exists
file = open(outputFileName, "w+")

# sort word dict and then start writing to file
for word, index in sorted(words.items()):
    file.write(word + " " + str(index) + "\n") 

file.close() # close the output file when done