### nmap : Scan local network

➤ sudo nmap -sP 192.168.20.0/24 | grep Rasp -C 5
  -C 5    : 前后5行
  -B 5    : 前5行
  -A 5    : 后5行

➤ sudo nmap -sP 192.168.20.0/24 > ip_scan_result.txt

➤ cat ip_scan_result.txt | grep -B 2 Rasp
Nmap scan report for 192.168.20.76
Host is up (0.00092s latency).
MAC Address: B8:27:EB:5F:C3:39 (Raspberry Pi Foundation)
