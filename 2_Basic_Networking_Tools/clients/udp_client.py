import socket

target_host = "www.google.com"
target_port = 80

#create a socket object 
# 1-> IPv4
# 2-> TCP will be used
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send some data
client.sendto(b"HeheBoi",(target_host,target_port))

#receive some data
data,addr = client.recvfrom(4096)
print(data.decode())
client.close()
