### Appearance
    vim ~/.bashrc
    (add this line below)
    PS1='\n\t\[\033[4;31;1m\]\u\[\033[00m\]@\h:\[\033[37;1m\]\w\[\033[32;1m\]\n\$ \[\033[34;0m\]'
    
    source ~/.bashrc

### Record Terminal with ttyrec
    sudo apt install ttyrec

    ttyrec <rec.Title>
    <C-d> to stop

    ttyplay -s 4.0 <rec.Title>

### apt install terminator
    putty style paste
    copy on select
