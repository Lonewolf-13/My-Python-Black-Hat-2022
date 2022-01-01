from socket import *

target_host = '127.0.0.1'       # Server IP or Hostname
target_port = 8989              # Server Port

# create a socket object
client = socket(AF_INET, SOCK_DGRAM)        # AF_INET = IPv4  | SOCK_DGRAM = UDP Protocol

#send some data
client.sendto(b'AAAABBBBC',(target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
