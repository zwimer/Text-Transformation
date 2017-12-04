"""
A program to fix repeated errors in each output file
"""

import os

for (dirpath, dirnames, filenames) in os.walk('.'):
    print("At directory:", dirpath, dirnames, filenames)
    for filename in filenames:
        if filename == 'output.txt':

            # Open output files and read in text
            f = open(dirpath + '/' + filename, 'r')
            text = f.read()
            f.close()

            # Replace errors
            text = text.replace('indicies', 'indices')
            text = text.replace('Null', 'null,')

            text = text.replace('1 :', '"1" :')
            text = text.replace('2 :', '"2" :')
            text = text.replace('3 :', '"3" :')

            # Overwrite file
            f = open(dirpath + '/' + filename, 'w')
            f.write(text)
            f.close()
