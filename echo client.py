import socket
import sys

# Create a UDP socket
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 11000)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = ClientSocket.sendto(message, server_address)

    # Receive response
    print >>sys.stderr, 'waiting to receive'
    data, server = ClientSocket.recvfrom(4096)
    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    ClientSocket.close()
