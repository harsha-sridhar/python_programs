#!/usr/bin/python
import sys
try:
    n=len(sys.argv)
    if n==2:
        fileObject = open(sys.argv[1], "r")
        str1=fileObject.readlines()
        num_lines=len(str1)
        num_char=0
        num_words=0
        for element in str1:
            str2=element.split()
            num_words+=len(str2)
            for item in str2:
                for n in item: 
                    if item.isdigit() or item.isalpha():
                        num_char+=1
        print('\nnumber of lines in given file is ',num_lines)
        print('\nnumber of words in given file is ',num_words)
        print('\nnumber of character given file is ',num_char)
    else:
        print('\ngive the filename in the input like below \n\npython3 word_count.py filename.extension\n')
except FileNotFoundError:
    print("File is not found in the directory")
