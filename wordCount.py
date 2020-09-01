import os  # check if file exists
import sys # command line arguments

inputFilename = sys.argv[1]  # save name of input file
outputFileName = sys.argv[2] # save name of output file
words = {}                   # python dictionary - where words & counts will be stored

# check to make sure the input file exists
if not os.path.exists(inputFilename):
    print("The file %s does not exist!" % inputFilename);
    exit()

