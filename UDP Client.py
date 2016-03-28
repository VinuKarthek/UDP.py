import socket
import time

UDP_IP = "localhost"
UDP_PORT = 5454
MESSAGE = "Hello, World!"

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

Clientsocket = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

while 1:
    Clientsocket.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
    print ("sent: "+MESSAGE)
    time.sleep(1) # Delay to reduce overloading
