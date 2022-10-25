#!/bin/bash
#先安裝可能缺少的東西
sudo apt-get install python3 -y
sudo apt-get install python3-tk -y
sudo apt-get install docker -y
sudo apt-get install docker-compose -y


#設定之後開機自動執行腳本
sudo touch /etc/systemd/system/start_connect.service
sudo chmod 644 /etc/systemd/system/start_connect.service

#寫進.service的內容：

sudo echo "[Unit]" >> /etc/systemd/system/start_connect.service
sudo echo "Description= connect to server when device starts every time" >> /etc/systemd/system/start_connect.service
sudo echo "[Service]" >>/etc/systemd/system/start_connect.service
sudo echo "WorkingDirectory=`pwd`" >> /etc/systemd/system/start_connect.service
sudo echo "ExecStart=/usr/bin/python3 `pwd`/client.py" >> /etc/systemd/system/start_connect.service
sudo echo "Restart=always" >> /etc/systemd/system/start_connect.service
sudo echo "RestartSec=3s" >> /etc/systemd/system/start_connect.service

#之後開機自動啟動服務
#sudo systemctl enable start_connect.service

#其餘指令：
#手動啟動服務：sudo systemctl start start_connect.service
#手動關閉服務：sudo systemctl stop start_connect.service
#查詢狀態：sudo systemctl status start_connect.service
#之後開機「停止」自動啟動服務：sudo systemctl disable start_connect.service

