sudo sslocal -c /etc/shadowsocks.json
proxychains chromium-browser &

* use 'nohub' or 'screen' to run command backgroudly

=====================================

Step 1: sudo apt-get install shadowsocks

Step 2: nohub sudo sslocal -c /etc/shadowsocks.json &

    {
      "server":"xx.xx.xxx.xxx",
      "server_port":8388,
      "password":"<password>",
      "local_address":"127.0.0.1",
      "local_port":1080,
      "timeout":600,
      "method":"aes-256-cfb"
    }

Step 3: sudo apt-get install proxychains
        mkdir ~/.proxychains/
        cd ~/.proxychains/
        vi proxychains.conf

            strict_chain
            proxy_dns
            remote_dns_subnet 224
            tcp_read_time_out 15000
            tcp_connect_time_out 8000
            localnet 127.0.0.0/255.0.0.0
            quiet_mode

            [ProxyList]
            socks5 127.0.0.1 1080

Step 4: Go!
    proxychains google-chrome
    nohub proxychains chromium-browser %url%
