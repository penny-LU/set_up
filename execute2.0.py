# -*- coding: utf-8 -*-
from dis import Instruction
import socket
import os
import io
import sys
from os import lseek


################################    class YAML  ################################
class YAML:

    def __init__(self, image, video, real_time):
        self.image = image
        self.video = video
        self.real_time = real_time

    def service_basic_setting(self,service_text,image_tag, volume) :
        text = ""
        text = text + "    image: " + image_tag + "\n"
        if (volume == True) :
            text = text + "    volumes:\n"
            text = text + "      - .:/source"
        
        service_text = text
    # service_basic_setting()

    def OutFile( self,outName, yaml_text ):
        f = open(outName, 'w') 
        f.write(yaml_text) 
        f.close()
    # OutFile()

    def YAML_main(self):

        outName = "yaml.txt"
        yaml_text = "version: \"3.8\"\n\nservices:\n"

        if ( self.image == "1" ) :
            service_text = ""
            yaml_text = yaml_text + "  picture:\n"
            self.service_basic_setting(service_text,"chiz0943/image_output_path:latest", True)
            yaml_text = yaml_text + service_text + "\n"
            self.service_basic_setting(service_text,"chiz0943/image_only_input:latest", True)
            yaml_text = yaml_text + service_text + "\n"

        if ( self.video == "1" ) :
            service_text = ""
            yaml_text = yaml_text + "  video:\n"
            self.service_basic_setting(service_text,"chiz0943/video_output_path:latest", True)
            yaml_text = yaml_text + service_text + "\n"
            self.service_basic_setting(service_text,"chiz0943/video_only_input:latest", False)
            yaml_text = yaml_text + service_text + "\n"

        if ( self.real_time == "1" ) :
            service_text = ""
            yaml_text = yaml_text + "  real_time:\n"
            self.service_basic_setting(service_text,"chiz0943/real_time:latest", False)
            yaml_text = yaml_text + service_text + "\n"

        self.OutFile( outName, yaml_text )
    # YAML_main()

################################    class YAML  ################################
################################################################################
################################    class pull  ################################
class pull:
    def __init__(self, image,video,real_time, img_output_path, video_output_path,turtle):
        self.image = image
        self.video = video
        self.real_time = real_time
        self.img_output_path = img_output_path
        self.video_output_path = video_output_path
        self.turtle = turtle


    def execute(self):
        count = int(self.image) + int(self.video) + int(self.real_time)+int(self.turtle)
        if ( count == 1) :# 單個image
            out = "sudo docker pull "
            if (image == True or image == "1") :
                if ( image_output_path != "") :
                    out = out + "chiz0943/image_output_path:latest"
                else:
                    out = out + "chiz0943/image_only_input:latest"
            if (video == True or video == "1") :
                if ( video_output_path != "") :
                    out = out + "chiz0943/video_output_path:latest"
                else:
                    out = out + "chiz0943/video_only_input:latest"
            if (real_time == True or real_time == "1") :
                out = out + "chiz0943/real_time:latest"
            if (turtle == True or turtle == "1") :
                out = out + "chiz0943/ros_noetic"

            os.system(out) #pull command
        else :
            os.system("docker-compose up ")
    # compose up

    def pull_main(self):
        self.execute()

################################    class pull  ################################
################################################################################
################################    class start  ################################
class start:
    def __init__(self, image,video,real_time,image_path, image_output_path,video_path, video_output_path, camera_path,turtle):
        self.image = image
        self.video = video
        self.real_time = real_time
        self.image_path = image_path
        self.image_output_path = image_output_path
        self.video_path = video_path
        self.video_output_path = video_output_path
        self.camera_path = camera_path
        self.turtle = turtle

    def doingImage(self):
        if( self.image_output_path !="0" ):
            command = "sudo docker run -v " + self.image_path + ":/temp -v " + self.image_output_path + ":/output chiz0943/image_output_path"
        else :
            command = "sudo docker run -v " + self.image_path + ":/temp chiz0943/image_only_input"

        os.system(command)
        print(command)
        print("========== Image detection ==========")

    def doingVideo(self):
        if( self.video_output_path !="0" ):
            command = "sudo docker run -v " + self.video_path + ":/temp -v " + self.video_output_path + ":/output chiz0943/video_output_path"
        else :
            command = "sudo docker run -v " + self.video_path + ":/temp chiz0943/video_only_input"
        os.system(command)
        print(command)
        print("========== Video detection ==========")

    def doingRealTime(self): #還需掛載camera的device

        command = "echo -n \"sudo docker run --device="
        command = command + self.camera_path+" -e DISPLAY=\$DISPLAY -v \$XSOCK:\$XSOCK -v \$XAUTH:\$XAUTH -e XAUTHORITY=\$XAUTH  chiz0943/real_time \">> ./real_time.sh"
        os.system(command)
        command = "./real_time.sh"
        os.system(command)
        print(command)
        print("========== RealTime detection ==========")

    def doingTurtle(self):
        command = "./turtle.sh"
        os.system(command)
        print(command)
        print("========== Turtlesim ==========")

    def start_main(self):
        if(self.image == "1" and self.image_path != "0" ) :
            self.doingImage()
        if(self.video == "1" and self.video_path != "0" ) :
            self.doingVideo()
        if(self.real_time=="1" and self.camera_path != "0") :
            self.doingRealTime()
        if(self.turtle=="1") :
            self.doingTurtle()
################################    class start  ################################
################################################################################

if __name__ == '__main__':
    #rcv1 = python3 execute.py 1 0 0 /home/chiz/shareeee 0 0 99.jpg 0
    image = sys.argv[1]
    video = sys.argv[2]
    real_time = sys.argv[3]
    image_path = sys.argv[4]
    image_output_path = sys.argv[5]
    video_path = sys.argv[6]
    video_output_path = sys.argv[7]
    camera_path = sys.argv[8]
    turtle = sys.argv[9]
    #print(image,video,real_time,image_path, video_path, camera_path, pic_name)


    createYaml = YAML(image,video,real_time)
    doingPull = pull(image,video,real_time, image_output_path, video_output_path,turtle)
    doingALL = start(image,video,real_time,image_path, image_output_path,video_path, video_output_path, camera_path,turtle)

    if( int(image)+int(video)+int(real_time)+int(turtle) > 1) :
        createYaml.YAML_main()
    doingPull.pull_main()
    doingALL.start_main()
