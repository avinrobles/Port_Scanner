# PYTHON GENERIC PORT SCANNER
# Goal:
# 1. Learn the fundamentals of socket programming in Python
# 2. Create a simple port scanner that can check for open ports on a target host
# 3. Understand how to handle exceptions and errors in Python

# import modules and libraries in Python
from concurrent.futures import ThreadPoolExecutor
import socket

#  Add ports and label them in a dict
ports = {
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    80: "http",
    110: "pop3",
    143: "imap",
    443: "https",
    587: "smtp",
    993: "imaps",
    995: "pop3s",
    3306: "mysql",
    5432: "postgresql",
    6379: "redis",
    27017: "mongodb",
}

# Create a function to perform port scanning. It will allow parameters host & port range
def scan(host,port):
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    if result == 0:
        return True
    return False

# Add threading to speed up the scanning process
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(lambda p: scan(host, p), range(1, 1025))

# legal host to test against
host = "scanme.nmap.org"

for port in range(1, 1025):
    if scan(host, port):
        service = ports.get(port, "Unknown")
        print(f"Port {port} open — {service}")

# # Create a function for service banner grabbing
# def grab_banner(host, port):
#     try:
#         s = socket.socket()
#         s.settimeout(2)
#         s.connect((host, port))
#         banner = s.recv(1024).decode().strip()
#         return banner
#     except Exception as e:
#         print(f"Error occurred while grabbing banner from {host}:{port} - {e}")
#         return None

# If port is open, check if it's in the map and display service name through a services database.

# For CLI:
# python scanner.py --host scanme.nmap.org --ports 1-1024 --timeout 1