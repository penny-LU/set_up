# -*- coding: utf-8 -*-
import sys
import os
#得到github網址跟名稱，打包成image
#create docker file
# docker build

if __name__ == '__main__':
	#system owner_name image_name github 
	system = sys.argv[1]
	owner_name = sys.argv[2] 
	image_name = sys.argv[3] 
	github = sys.argv[4] 

	outName = "dockerfile"
	outText = "FROM " + system + "\nLABEL maintainer=\"" + owner_name + "\"\n"
	outText = outText + "RUN  git clone " + github

	f = open(outName, 'w') 
	f.write(outText) 
	f.close()
	command = "docker build -t rosalabtest/" + image_name + " ."
	os.system(command)
	command = "docker login -u rosalabtest -p ROSaLabTest"
	os.system(command)
	command = "docker push rosalabtest/" + image_name
	os.system(command)
	command = "docker logout"
	os.system(command)