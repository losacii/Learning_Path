### SSH without a password

" 生成秘钥，传输到远端
ssh-keygen -t rsa -b 4096
scp /home/vi/.ssh/id_rsa.pub pi@192.168.20.15:/home/pi/.ssh/uploaded_key.pub

" 远端更新
cd .ssh
cat uploaded_key.pub >> authorized_keys2
chmod 700 ~/.ssh/
chmod 600 ~/.ssh/*

" 备份 /etc/ssh/sshd_config.bak
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak

" 修改
sudo vi /etc/ssh/sshd_config
		PasswordAuthentication no

sudo serice ssh restart
