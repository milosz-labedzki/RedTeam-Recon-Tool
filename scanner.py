import socket
import sys
if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    target = "127.0.0.1"
target_ip = socket.gethostbyname(target)
print(f"Target IP: {target_ip}")

ports = [21,22,53,80,443,445,3389]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)

    result = s.connect_ex((target_ip,port))

    if result == 0:
        print(f"[+] Port {port} IS OPEN!")
    else:
        print(f"[+] PORT {port} IS CLOSED")

    s.close()
