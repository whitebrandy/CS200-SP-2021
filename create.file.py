#!/usr/bin/env python
import sys
from os import path
from datetime import datetime


def usage():
    print ("Usage: " + sys.argv[0] + " \"Your first name\"")
    print ("Eg: " + sys.argv[0] + " Bandan")

    if name != "":
        filename = name + ".txt"
        print ("Remove " + filename + " if it exists and try again")
    sys.exit(0)    
    
if __name__ == "__main__":
    count = len(sys.argv)
    name = ""
    if count != 2:
        usage()

    name = sys.argv[1]
    filename = name + ".txt"
    if path.exists(filename):
        usage()
        
    file = open(filename, "w+")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file.write(dt_string)
    file.write("\n")    
    file.close()



    
        




    
