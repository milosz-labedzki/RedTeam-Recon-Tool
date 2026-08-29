import socket
import sys

if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    target = "127.0.0.1"

target_ip = socket.gethostbyname(target)
print(f"Target IP: {target_ip}\n")

ports = [21,22,25,80]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)

    try:
        s.connect((target_ip, port))
        banner = s.recv(1024)
        print(f"[+] Port {port} OPEN | Banner: {banner.decode().strip()}")
    except:
        print(f"[-] Port {port} CLOSED | pr NO BANNER")

    s.close()