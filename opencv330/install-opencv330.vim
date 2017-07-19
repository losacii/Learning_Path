[compiler]
sudo apt-get install build-essential

[required]
sudo apt-get install cmake
git
sudo apt-get install libgtk2.0-dev
sudo apt-get install pkg-config
sudo apt-get install libavcodec-dev
sudo apt-get install libavformat-dev
sudo apt-get install libswscale-dev

[optional]
sudo apt-get install python-dev
sudo apt-get install python-numpy
sudo apt-get install libtbb2
sudo apt-get install libtbb-dev
sudo apt-get install libjpeg-dev
sudo apt-get install libpng-dev
sudo apt-get install libtiff-dev
sudo apt-get install libdc1394-22-dev

>>>>>>>>>>
install libjasper-dev:
  https://www.ubuntuupdates.org/package/core/xenial/main/updates/libjasper-dev

cd 
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git

cd opencv

mkdir build
cd build

losa@pc:~/opencv/build$
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
(1 min)

make -j7
(9:31 ~ 9:47)

sudo make install
(25 sec)


[optional] Building documents.
	cd ~/opencv/build/doc/
	make -j7 doxygen

###################################

install opencv3.3.0:
  http://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html

http://blog.csdn.net/alphaPii/article/details/72764917?locationNum=11&fps=1
http://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html
http://www.cnblogs.com/arkenstone/p/6490017.html

