# -*- coding: utf-8 -*-
import socket
import os 
import numpy as np
import sys
from _thread import *
from multiprocessing import Process
import threading
import queue

if __name__ == '__main__':
	#傳送進來的str: python3 server.py 1 0 0 /home/chiz/shareeee/image /home/chiz/shareeee/image_result 0 0 0
	#還要有client_sock
	client_sock = argv[2]
	i = 3
	while(i < argc):
		output_instr = output_instr + argv[i] + " "
		i = i + 1

	print('send to client : ' + output_instr)
	main_process.set()

	outdata = output_instr
	client_sock.send(outdata.encode())
	output_instr=""
	indata = client_sock.recv(1024)


			
			
# py3接收的資料型別為byte 所以要用decode()把str轉換byte(反之亦然)

