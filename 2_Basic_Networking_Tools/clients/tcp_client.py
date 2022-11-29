import socket

target_host = "0.0.0.0"
target_port = 6969 

#create a socket object 
# 1-> IPv4
# 2-> TCP will be used
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send some data
client.send(b"Hemlo :)")

#receive some data
response = client.recv(4096)
print(response.decode())
client.close()
