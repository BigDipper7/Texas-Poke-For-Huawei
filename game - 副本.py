# -*- coding: utf-8 -*-
import socket, sys, chardet

if len(sys.argv) != 6:
    print 'Parameter not mate, notice must use like this:'
    print '\rpython client.py [ip] [port]'
    sys.exit(0)

#获得的相关信息
server_ip = sys.argv[1]
server_port = int(sys.argv[2])
client_ip = sys.argv[3]
client_port = int(sys.argv[4])
pid = sys.argv[5]

#链接程序
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = (server_ip, server_port)
client_addr = (client_ip, client_port)

#bind client_addr
client_socket.bind(client_addr)

#connect server_addr
client_socket.connect(server_addr)

while 1:
    # member = '第一组'
    client_socket.send('reg: '+pid+' Neo \n')

    data = client_socket.recv(1024)
    print 'data: ',data.decode('utf-8')
    break

client_socket.close()
sys.exit(0)
