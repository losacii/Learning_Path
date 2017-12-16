## BASHRC
  PS1='${debian_chroot:+($debian_chroot)}**\n[\t]**\[\033[01;32m\]**\u**\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$\n➤ '

## Linux, SpaceVim, ~/ .SpaceVim.d/init.vim
  备份：
  mv .SpaceVim.d/init.vim .SpaceVim.d/init.vim.bak
  下载保存：
  wget -O .SpaceVim.d/init.vim \
  https://raw.githubusercontent.com/losacii/ubuntuMemo/master/vimDoc/configs/init_for_Spacevim.vim
  

## Win7, Visual Studio, VsVimrc:
  wget -O _vsvimrc \
  https://raw.githubusercontent.com/losacii/ubuntuMemo/master/vimDoc/configs/vsVimrc
  
## alias: Windows
    alias reboot=shutdown -r -t 0
    alias godown=shutdown -s -t 0

    alias shpi=ssh pi@raspberrypi
    alias unalias=alias /d $1
    alias vi=vim $*

## alias: Linux
    alias ip='ifconfig | grep inet'
    alias cdg='cd ~/Documents/gitDocs'
