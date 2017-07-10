[compiler] 
sudo apt-get install build-essential

[required] 
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

[optional] 
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev

>>>>>>>>>>
sudo apt-get install libjasper-dev

losa@pc:~$ 
cd opencv

losa@pc:~/opencv$ 
mkdir build && cd build

losa@pc:~/opencv/build$ 
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
(1 min)

make -j7
(9:31 ~ )

sudo make install

[optional] Building documents.
	cd ~/opencv/build/doc/
	make -j7 doxygen

