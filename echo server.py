import socket
import sys

# Create a TCP/IP socket
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 11000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
ServerSocket.bind(server_address)
while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = ServerSocket.recvfrom(4096)
    
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data
    
    if data:
        sent = ServerSocket.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
