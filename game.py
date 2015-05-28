# -*- coding: utf-8 -*-
import socket, sys

#define msg
MSG_GAME_OVER='game-over \n'
#define msg end


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

# client_socket.settimeout(2000)

#register on server...
client_socket.send('reg: '+pid+' Neo \n')

buf_len=4096
# buf = ''
# has_in = False
while 1:
    data = client_socket.recv(buf_len)
    print 'data: ['+data+']'
    if data== MSG_GAME_OVER:
        break
    # if len(data) == buf_len: #It mey casue a bug, if the msg len is exactly buf_len, it will wait for the next msg to recv..Ugly!
    #     if has_in==False:
    #         buf =''
    #         has_in=True
    #     buf += data
    # else:
    #     if has_in==True:
    #         buf += data
    #         has_in = False
    #     else:
    #         buf = data
    #
    # print 'data: ['+data+']'
    # if has_in==False:
    #     print 'buf: ['+buf+']'

client_socket.close()
sys.exit(0)
