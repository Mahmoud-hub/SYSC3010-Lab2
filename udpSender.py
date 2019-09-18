# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
number = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

while 1:
    print ("Enter data to transmit: ENTER to quit")
    data = sys.stdin.readline().strip()
    if not len(data):
        break
#    s.sendall(data.encode('utf-8'))
    newMessage = "";
    message = "Message"
    for(int i = 1;i < int(number);i++):
        newMessage = message + str(i)
        s.sendto(newMessage.encode('utf-8'), server_address)
s.shutdown(1)

