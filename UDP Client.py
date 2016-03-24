"""import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
sock.sendto(data + "\n", (HOST, PORT))
received = sock.recv(1024)

print "Sent:     {}".format(data)
print "Received: {}".format(received)"""

import socket
import time

UDP_IP = "localhost"
UDP_PORT = 5454
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

Clientsocket = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

while 1:
    Clientsocket.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print "sent: "+MESSAGE
    time.sleep(1) # Delay to reduce overloading
