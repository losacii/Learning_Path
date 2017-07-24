### init
sudo su
apt-get update

### sudo-with-no-passwd:

	sudo visudo
	losa ALL=(ALL) NOPASSWD: ALL
	(write into /etc/sudoer.tmp)

### installs
sudo apt-get instll net-tools
sudo apt-get install openssh-server
sudo /etc/init.d/ssh start

### terminator
sudo apt-get install terminator
    global: PuTTY style paste
    Profile: Copy on selection

terminator:

	alt + Q: broadcast off
	alt + A: broadcast All
	alt + G: broadcast Group
	PuTTy style Paste


### git-core
sudo aapt-get install git-core

### Brightness
setting: Brightness&Lock;
    

### Git stuff:
    cd ~/Documents
    git clone https://github.com/losacii/ubuntuMemo.git
    git init
    git config --global user.name 'losacii'
    git config --global user.email 'losacii5@gmail.com'

    (Jump git passwd)
    cd /
    git config --global credential.helper store

    git add .
    git commit -m 'update'
    git push
    (git pull)

    git remote rm origin
    git remote add origin git@github.com:username/repository.git
    git push -u origin master

    cd ubuntuMemo/
    git remote -v (see infos)

### swap Esc with CapsLock:

	xmodmap .speedswapper

sudo apt install python-pip

pip install jedi


install chrome:

  sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/
  wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
  sudo apt-get update
  sudo apt-get install google-chrome-stable

### System Settings:

    C-A-T: terminal
        W: web_browser
        H: home_Folder

    A-o  : take a screenshot of an area [to clipboard]
    A-p  : take a screenshot of an area

    C-1  : Volume Down
    C-2  : volume Up
    C-3  : mute

    C-A-L: log out
    Super+L : Lock Screen

    Super + 1/2/3/4: go to Workspace

for opencv330:

	sudo apt-get install build-essential

	sudo apt-get install cmake
	sudo apt-get install git
	sudo apt-get install libgtk2.0-dev
	sudo apt-get install pkg-config
	sudo apt-get install libavcodec-dev
	sudo apt-get install libavformat-dev
	sudo apt-get install libswscale-dev

	sudo apt-get install python-dev
	sudo apt-get install python-numpy
	sudo apt-get install libtbb2
	sudo apt-get install libtbb-dev
	sudo apt-get install libjpeg-dev
	sudo apt-get install libpng-dev
	sudo apt-get install libtiff-dev
	sudo apt-get install libdc1394-22-dev

	git clone https://github.com/opencv/opencv.git
	git clone https://github.com/opencv/opencv_contrib.git

	( tar zxvf FileName.tar
	  tar czvf FileName.tar DirName )

	cd ~/opencv
	mkdir build
	cd build
	cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..

	(after 35 secs)
	sudo make -j7

	(after 5 minutes)
	sudo make install
	(this takes 1 min)

	python
	import cv2
	cv2.__version__

Compile vim8.0:

	sudo apt-get install libncurses5-dev
	git clone https://github.com/vim/vim.git
	cd vim
	git pull

	sudo apt-get install libncurses5-dev libgnome2-dev libgnomeui-dev \
	libgtk2.0-dev libatk1.0-dev libbonoboui2-dev \
	libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev \
	python3-dev

	./configure --with-features=huge \
		    --enable-multibyte \
		    --enable-pythoninterp \
		    --with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu \
		    --enable-gui=gtk2 --enable-cscope --prefix=/usr

	make VIMRUNTIMEDIR=/usr/share/vim/vim80

	sudo make install

	make distclean

cd ~/
wget https://raw.githubusercontent.com/losacii/ubuntuMemo/master/vim-config/vimrc-back
mv vimr	.vimrc

mkdir .vim && cd .vim
mkdir autoload bundle colors ftplugin

cd autoload
wget https://raw.githubusercontent.com/tpope/vim-pathogen/master/autoload/pathogen.vim

cd ../bundle
git clone https://github.com/tpope/vim-sensible.git
git clone https://github.com/kien/ctrlp.vim.git
git clone https://github.com/scrooloose/nerdtree
git clone https://github.com/Lokaltog/vim-powerline.git
git clone https://github.com/jistr/vim-nerdtree-tabs.git

cd ../colors
wget https://raw.githubusercontent.com/thesheff17/youtube/master/vim/wombat256mod.vim

cd ../ftplugin
wget https://raw.githubusercontent.com/thesheff17/youtube/master/vim/python_editing.vim

cd ../bundle/
git clone https://github.com/Valloric/YouCompleteMe.git
cd YouCompleteMe/
git submodule update --init --recursive

( cd ..
  tar czvf YoucompletemeDown.tar YouCompleteMe/ )

sudo apt-get install clang-4.0

./install.py --clang-completer
(##




https://github.com/ets-labs/python-vimrc
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ets-labs/python-vimrc/master/setup.sh)"
~/.vim/bundle/YouCompleteMe/install.py --clang-completer

(Change appearance of terminal!)
sudo vim ~/.bashrc (go to bottom line, add this line)
PS1='\t\[\033[4;31;1m\]\u\[\033[00m\]@\h:\[\033[37;1m\]\w\[\033[32;1m\]\$ \[\033[34;0m\]'
source ~/.bashrc
(then restart terminal, set the difference!!)
