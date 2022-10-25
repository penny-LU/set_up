# -*- coding: utf-8 -*-
import socket
import numpy as np
from _thread import *
import threading


def check_ip_list(ip_list, addr, index_num):
	try:
		index_num = ip_list.index(str(addr))
	except ValueError:
		ip_list.append(str(addr))


def threaded(conn,target_ip):
	output_instr = ""
	ability_list = ["0" for i in range(8)]
	while True:
		indata = conn.recv(1024)
		if len(indata) == 0: # connection closed
			conn.close()
			print('client closed connection.')
			break

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

		print('send to client : ' + output_instr)
		outdata = output_instr
		conn.sendto(outdata.encode(),eval(target_ip))
		ability_list = ["0" for i in range(8)]
		output_instr=""
		conn.close()

if __name__ == '__main__':
	HOST = '127.0.0.1'
	PORT = 48331

	# server接收到要指定出戰的ip跟指令碼
	# 所以Server需要紀錄所有已連線&&空閒的的client-ip
	# 然後選擇要出去的是誰


	# 建立socket 設定使用的通訊協定
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# 綁定ip & port
	server.bind((HOST, PORT))
	# 開始監聽 監聽上限為5
	server.listen(5)

	print('server start at: %s:%s' % (HOST, PORT))
	print('wait for connection...')
	ip_list=list()
	index_num="-1"

	while True:
		# TCP建立後收到的回應 conn是新的socket類型 addr是client的
		client_sock, client_addr = server.accept()
		print('connected by ' + str(client_addr))
		
		# 確認這個ip有沒有出現過，有的話就是做完回來的
		check_ip_list(ip_list, client_addr, index_num )
		print("===已連線的ip===")
		for i in range(len(ip_list)):
			print("[",i,"]",ip_list[i])
		refresh = input("若需重新整理連線清單請輸入0，其餘選項將進行任務分配\n")
		
		if(refresh != "0"):
			index = input("請選擇欲指定的client(輸入序號即可)")
			target_ip = ip_list[int(index)]
			ip_list.remove(target_ip)
			start_new_thread(threaded, (client_sock,target_ip,))
		
		refresh=""

	server.close()

# py3接收的資料型別為byte 所以要用decode()把str轉換byte(反之亦然)




