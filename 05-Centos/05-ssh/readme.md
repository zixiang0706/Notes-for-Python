# ssh



## usefull notes
首先要安装openssh
开启ssh服务 /usr/sbin/sshd
　　// ubuntu系统
　　service ssh restart

　　// debian系统
　　/etc/init.d/ssh restart

ssh-keygen
chmod 600 ~/.ssh/authorized_keys
ssh-copy-id user@host

ssh user@host 'mkdir -p .ssh && cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub

in host1, run: ssh -fNgL 2121:$host2:22 $host3
in host2, run:  ssh -NfgR 10030:$host2:22 root@47.96.174.116
