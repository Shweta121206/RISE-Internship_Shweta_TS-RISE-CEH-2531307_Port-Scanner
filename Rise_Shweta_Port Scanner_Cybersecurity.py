import socket
import threading

print("\n=== Simple Python Port Scanner ===")

target = input("Enter IP address to scan: ")

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        s.connect((target, port))
        print(f"[OPEN] Port {port}")
    except:
        pass
    finally:
        s.close()


print("\nScanning ports 1–1024...\n")

threads = []

for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\n--Scan Complete--")
