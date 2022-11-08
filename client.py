# -*- coding: utf-8 -*-
from dis import Instruction
import socket
import os
import io
import sys
from os import lseek


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 48331

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
            print('recv1: ' + indata.decode())
            indata = "python3 execute.py "+ indata.decode()
            os.system(indata) #pull
            outdata="done!"

    exit(0) #end client.py
