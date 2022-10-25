# -*- coding: utf-8 -*-
import socket
import numpy as np

HOST = '127.0.0.1'
PORT = 48331

#建立socket 設定使用的通訊協定
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#綁定ip & port
s.bind((HOST, PORT))
#開始監聽 監聽上限為5
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')
output_instr=""
ability_list = ["0" for i in range(8)]
while True:
    #TCP建立後收到的回應 conn是新的socket類型 addr是client的
    conn, addr = s.accept()
    print('connected by ' + str(addr))

    while True:
        #接收client傳來的資料
        indata = conn.recv(1024)
        if len(indata) == 0: # connection closed
            conn.close()
            print('client closed connection.')
            break
        else :
            instr = input("請輸入client需擁有的功能\n")
            instr_list = instr.split(' ')
            i = 0
            while( i < len(instr_list)):
                if( instr_list[i] == "image"):
                    ability_list[0] = "1"
                elif( instr_list[i] == "video"):
                    ability_list[1] = "1"
                elif( instr_list[i] == "real_time"):
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
        #只會傳送 0 1 1 這種 前面不需要了
        #後面需接 image辨識掛載目錄 / video辨識掛載目錄 / real_time掛載的camera
        print('send to client : ' + output_instr)

        outdata = output_instr
        conn.send(outdata.encode())
        ability_list = ["0" for i in range(8)]
        output_instr=""

# py3接收的資料型別為byte 所以要用decode()把str轉換byte(反之亦然)
