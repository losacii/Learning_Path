" This is for vimrc on Windows:
" READ FILE FROM: "-1read c:\screencast\Vim\_vimrc"

## Cmder Vimrc
    Download and Apply: 
    wget -O c:/screencast/Vim/_vimrc https://raw.githubusercontent.com/losacii/ubuntuMemo/master/vimDoc/vimConfigs/windowsVimrc.vim

## Local Altering Sync:
    cp c:/screencast/Vim/_vimrc Documents\gitDoc\ubuntuMemo\vimDoc\vimConfigs\windowsVimrc.vim

## Visual Studio vimrc file is in HomeFolder: "C:\Users\Administrator"
    cp vimrc Documents\gitDoc\ubuntuMemo\vimDoc\vimConfigs\vsVimrc.vim
    
## VsVimrc: Pull and Apply Vsvimrc

    (C:\Users\Administrator)
    cd Documents\gitDoc\ubuntuMemo
    git pull
    cp vimDoc\configs\vsVimrc.vim C:\Users\Administrator\vimrc

    or

    wget -O C:\Users\Administrator\vimrc 

