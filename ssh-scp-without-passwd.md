### ~/Documents/ubuntuMemo/ssh-scp-without-passwd.md

### 1. Generate public/private key with: ssh-keygen
    ssh-keygen (for SSHv1)
    ssh-keygen -t rsa (for SSHv2)

### 2. Copy .pub file to .ssh directory of remote host
       rename .pub as 'authorized_keys'  (for ssh1)
                      'authorized_keys2' (for ssh2)

       delete @xxxx at end.

### 3. ssh -i sshvi userName@ip
