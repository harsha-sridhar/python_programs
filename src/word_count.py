#!/usr/bin/python
import sys
try:
    n=len(sys.argv)
    if n==2:
        fileObject = open(sys.argv[1], "r")
        str1=fileObject.read()
        num_lines=0
        num_char=0
        num_words=len(str1.split())
        for i in str1:
            if i=='\n':
                num_lines+=1
            if i.isdigit() or i.isalpha():
                num_char+=1
        print('\nnumber of lines in given file is ',num_lines)
        print('\nnumber of words in given file is ',num_words)
        print('\nnumber of character given file is ',num_char)
    else:
        print('\ngive the filename in the input like below \n\npython3 word_count.py filename.extension\n')
except FileNotFoundError:
    print("File is not found in the directory")