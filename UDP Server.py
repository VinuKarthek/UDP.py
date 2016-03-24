"""import SocketServer

class MyUDPHandler(SocketServer.BaseRequestHandler):
   def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print data
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()"""

import socket

UDP_IP = "localhost"
UDP_PORT = 5454

ServerSocket = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
ServerSocket.bind((UDP_IP, UDP_PORT))

while 1:
    print "Waiting for data:"
    print "Received: "+ServerSocket.recv(30) # buffer size is 30 bytes
    
