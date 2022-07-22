#!/usr/bin/python
import subprocess,sys
from subprocess import PIPE
try:
    command=input("enter the shell command to execute: ")
    n=int(input("enter the number of seconds: "))
    cmd=f"watch -n {n} {command}"
    myfile=open("out.txt",'wt')
    process=subprocess.run(cmd,stdout=PIPE,shell=True)
    while True:
        line = process.stdout.readline()
        if not line:
            break
        myfile.write(line)
    #print (process.stderr.decode())
    #print(process.returncode)
    #pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #out, err = pr.communicate() 
    # check the return code
    #if pr.returncode != 0:
    #    sys.stderr.write("oh no")
    #else: 
    #    print(out)
except subprocess.CalledProcessError as ex:
    print ("Error from the subprocess")
except ValueError:
    print("enter the valid number of seconds")
except Exception as e:
    print(f"enter the valid command {e}")
except:
    print("enter the valid command")