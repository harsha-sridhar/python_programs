#!/usr/bin/python
import subprocess
import os
import sys
try:
    n=len(sys.argv)
    if n==2:
        filename=sys.argv[1]
        cmd="wc "+filename
        li=str(subprocess.check_output(cmd, shell=True)).split()
        print('number of lines in given file is ',li[1])
        print('number of words in given file is ',li[2])
        print('number of character given file is ',li[3])
    else:
        print('\ngive the filename in the input like below \n\npython3 word_count.py filename.extension\n')
except FileNotFoundError:
    print("File is not found in the directory")
except Exception:
    print("Some error has occured give the correct filename with path")