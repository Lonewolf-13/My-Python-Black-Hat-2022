from socket import *

target_host = "www.google.com"   # Server ip or Hostname
target_port = 80                 # Server Port

# creat a socket object
client = socket(AF_INET, SOCK_STREAM)      # AF_INET = IPv4   | SOCK_STREAM = TCP Protocol

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n')
# receive some data
response = client.recv(4096)

print(response.decode())
client.close()
