# apt-get update
# apt-get install ssh


# systemctl enable ssh
# service ssh start

option A is to create a new non-privileged user and use its credentials to log in. 

option B: Enable root login:

/etc/ssh/sshd_config
FROM:
#PermitRootLogin prohibit-password
TO:
PermitRootLogin yes

