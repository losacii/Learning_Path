### could not get lock /var/lib/dpkg/lock:
	sudo rm /var/cache/apt/archives/lock
	sudo rm /var/lib/dpkg/lock

### install chrome:

  sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/
  wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
  sudo apt-get update
  sudo apt-get install google-chrome-stable


### remove firefox:

  sudo apt-get autoremove firefox firefox-locale-en


### set wallpapers;


### Git, Gighub

  cd <dir>
  git init
  git config --global user.name 'losacii'
  git config --global user.email 'losacii5@gmail.com'

  Jump git passwd:
    cd /
    git config --global credential.helper store

  git: add, commit, push
    git add .
    git commit -m '<changeLog>'
    git push

vimrc:
vim /etc/vim/vimrc
set number
set relativenumber
set autoindent
set ttyfast
set tabstop=2
set hlsearch
nnoremap <F2> :set nonumber!<CR>:set foldcolumn=0<CR>

remote-desktop-copy-paste(copy below line by line):
  sudo apt-add-repository ppa:remmina-ppa-team/remmina-next
  sudo apt-get update
  sudo apt-get install remmina remmina-plugin-rdp


search: language support:
  click 'install'
  search 'input method', fcitx
  go top-right, keyboard picture, configure;
  add 'Shuangpin'


### samba:
  sudo apt-get install samba

  (on windows):
  computer, manage, users, add
  share a disk, set user


### install opencv3.3.0:
  http://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html


### for vim: Completely Swap 'Caps Lok' and "ESC":
  Drop this file in your home directory:
    ! Swap caps lock and escape
    remove Lock = Caps_Lock
    keysym Escape = Caps_Lock
    keysym Caps_Lock = Escape
    add Lock = Caps_Lock
  and call it ".speedswapper". Then open a terminal and type:
    xmodmap ~/.speedswapper

  Then swap MIDLE with RIGHT for mouse:
    xmodmap -e 'pointer = 1 3 2'
  Done! you'll be twice as efficient in Vim. Who needs caps lock anyway?
  * this is from: http://vim.wikia.com/wiki/VimTip166

### how to move folder:
    mv foldera/* folderb/
