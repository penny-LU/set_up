# set_up

set up 步驟
1. 下載 https://github.com/chiz0943/set_up.git
2. 更改server ip (目前是127.0.0.1)
3. sudo chmod u+x setup.sh
4. sudo ./setup.sh
5. python3 server.py
6. 測試功能

(此為測試步驟，之後會有完整的步驟）

// 確認有無連接camera及其掛載位置：

更改docker dir：

1. 確保docker已停止
systemctl stop docker.service

2. 修改/etc/docker/daemon.json文件，文件不存在需手动创建
vim /etc/docker/daemon.json

並新增以下：
{
"data_root": "path_to_store_docker"
}

3. 啟動服務
systemctl start docker.service

4.確認Docker Root Dir是否更改成功
docker info
