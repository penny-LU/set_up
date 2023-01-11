# set_up
本範例教程用於設置系統之設備端(client)所需之檔案

set up 步驟
1. git clone https://github.com/penny-LU/set_up.git
2. cd set_up

**安裝設備端連線至系統所需檔案**
1. sudo chmod u+x setup.sh
2. sudo ./setup.sh

**設置設備端使用GUI介面執行容器內功能之設定 (X11 ; yolov3即時影像辨識)**
1. sudo chmod u+x real_time.sh
2. sudo ./real_time.sh

**設置設備端使用GUI介面執行容器內功能之設定 (X11 ; ROS turtlesim)**
1. sudo chmod u+x turtle.sh
2. sudo ./turtle.sh
(本功能只用於測試ros環境)