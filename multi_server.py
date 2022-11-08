# -*- coding: utf-8 -*-
import socket
import os 
import numpy as np
import sys
from _thread import *
from multiprocessing import Process
import threading
import queue

global ip_list,sock_list
ip_list = list()
sock_list=list()

def check_ip_list( addr ):
	index_num = ip_list.index(str(addr))
	return index_num


def execute(client_sock,target_ip):
	output_instr = ""
	#ability_list = ["0" for i in range(8)]
	while True:
		"""
		instr = input("請輸入該client需擁有的功能\n")
		instr_list = instr.split(' ')
		i = 0
		while(i < len(instr_list)):
			if(instr_list[i] == "image"):
				ability_list[0] = "1"
			elif(instr_list[i] == "video"):
				ability_list[1] = "1"
			elif(instr_list[i] == "real_time"):
				ability_list[2] = "1"
			i = i + 1

		if( ability_list[0] == "1" ) : #image
			ability_list[3] = input("image掛載目錄的路徑，若無則輸入0\n")
			ability_list[4] = input("image存放結果的路徑，若無則輸入0\n")
				
		if( ability_list[1] == "1") : #video
			ability_list[5] = input("video掛載目錄的路徑，若無則輸入0\n")
			ability_list[6] = input("video存放結果的路徑，若無則輸入0\n")
			
		if( ability_list[2] == "1") : #real_time
			ability_list[7] = input("請輸入camera的路徑，若無則輸入0\n")

		i = 0
		while(i < len(ability_list)):
			output_instr = output_instr + ability_list[i] + " "
			i = i + 1
		# 只會傳送 0 1 1 這種 前面不需要了
		# 後面需接 image辨識掛載目錄 / video辨識掛載目錄 / real_time掛載的camera

		"""
		output_instr = "1 0 0 /home/chiz/shareeee/image /home/chiz/shareeee/image_result 0 0 0"
		print('send to client : ' + output_instr)
		main_process.set()

		outdata = output_instr
		client_sock.send(outdata.encode())
		#ability_list = ["0" for i in range(8)]
		output_instr=""
		indata = client_sock.recv(1024)
		if( indata.decode() == "done!"):
			break
		elif(len(indata) == 0):
			index_num = check_ip_list(target_ip)
			ip_list.pop(int(index_num))
			sock_list.pop(int(index_num))
			break

		

	
def new_connect(client_sock): #先完成連線
	indata = client_sock.recv(1024)
	print_connected_ip()
	

def print_connected_ip():
	print("===已連線的ip===")
	for i in range(len(ip_list)):
		print("[",i,"]",ip_list[i])
	
	print("================")

def update_connected_ip():
	refresh=""
	refresh = input("若需重新整理連線清單請輸入0，其餘選項將進行任務分配\n")
	while( refresh == "0"):
		print_connected_ip()
		refresh=""
		refresh = input("若需重新整理連線清單請輸入0，其餘選項將進行任務分配\n")



def already_connect(): #等待連線
	while True :
		update_connected_ip()
		index = input("請選擇欲指定的client(輸入序號即可)\n")
		while( len(index) != 1 or int(index) > len(ip_list) or int(index) < 0 ):
			#print(type(index))
			index = input("請選擇欲指定的client(輸入序號即可)\n")
		target_ip = ip_list[int(index)]
		client_sock = sock_list[int(index)]
		doing_now=threading.Thread(target=execute, args=[client_sock,target_ip])
		doing_now.start()
		#execute(client_sock,target_ip)
		main_process.wait()


if __name__ == '__main__':
	HOST = '127.0.0.1'
	PORT = 48331

	# 建立socket 設定使用的通訊協定
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# 綁定ip & port
	server.bind((HOST, PORT))
	# 開始監聽 監聽上限為5
	server.listen(5)

	print('server start at: %s:%s' % (HOST, PORT))
	print('wait for connection...')
	index_num="-1"
	main_process = threading.Event()
	first = threading.Thread(target=already_connect)
	first.start()
	while True:
		# TCP建立後收到的回應 conn是新的socket類型 addr是client的
		client_sock, client_addr = server.accept()
		print('connected by ' + str(client_addr))

		ip_list.append(str(client_addr))
		sock_list.append(client_sock)
		new_connect(client_sock)
			
			
# py3接收的資料型別為byte 所以要用decode()把str轉換byte(反之亦然)

