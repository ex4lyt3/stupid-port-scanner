#!/bin/python3

import sys
import os
import socket
import datetime


def Error():
    print("Welcome to the OK Python Port Scanner. Valid arguments include \n -m: Scanning for multiple ports \n -p: Single port \n \n" + str(datetime.datetime.now()) )
    exit()
    
if len(sys.argv) < 3:
    Error()

def Single():

    if int(sys.argv[3]) > 65535:
       print("Invalid port number")

    try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            status = s.connect_ex( (socket.gethostbyname(sys.argv[1]),int(sys.argv[3])) )
            
            if status != 0:
                print("Port "+sys.argv[3]+" is Closed")

            else:
                 print("Port "+sys.argv[3]+" can be communicated with.")
                 
    except False:
            print("a")
            
def Multiple():

    delimiter = sys.argv[3].index("-")
    print(str(delimiter))
    startport = (sys.argv[3])[0:(delimiter)]
    endport = (sys.argv[3])[(delimiter)+1:]
    
    if int(startport) < int(endport):
        for port in range(int(startport),int(endport)):
                try:
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    status = s.connect_ex( (socket.gethostbyname(sys.argv[1]),port))
        
                    if status != 0:
                        print("Port "+str(port)+" is Closed")

                    else:
                        print("Port "+str(port)+" can be communicated with.")
                except False:
                     print("  ")
    

if sys.argv[1] =="-m" or "-p":
    print("Starting...")
    if sys.argv[2] == "-p" and (sys.argv[3]).isdigit():
        Single()
    if sys.argv[2] == "-m":
        Multiple()
    
else:
    Error()
