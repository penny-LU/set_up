# -*- coding: utf-8 -*-
from dis import Instruction
import socket
import os
import io
import sys
from os import lseek


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8081

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    outdata = 'new connecting !'

    while True:
        print('send: ' + outdata)
        s.send(outdata.encode())

        indata = s.recv(1024)
        if len(indata) == 0: # connection closed
            s.close()
            print('server closed connection.')
            break
        else:
            temp = indata.decode()
            print('recv: ' + indata.decode())
            if (temp[0] == "g" and temp[1] == "i" and temp[2] == "t"):
                temp = temp[4:]
                instr = "python3 git_hub.py " + temp
                print('recv0: ' + instr)
                os.system(instr)
            else:
                print('recv1: ' + indata.decode())
                indata = "python3 execute.py "+ indata.decode()
                os.system(indata) #pull
            
            outdata="done!"

    exit(0) #end client.py