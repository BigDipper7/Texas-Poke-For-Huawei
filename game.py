# -*- coding: utf-8 -*-
import socket, sys
import re

#----------LOGIC PART-----------------
user_pid = []
user_jetton = []
user_money = []
user_order = [0,0,0,0,0,0,0,0,0,0]
match_number = 1
blind_number = 0
total_number = 0

def processAllMsg(msg):
    #identify msg ...
    re.findall(r"(\w+?/\ \n.+?\n/\w+?\ \n)",str,re.S)#解决粘包问题
    msg_arr = msg=.split('\n')
    if msg_arr[0] == 'seat/ ':

    elif msg_arr[0] == 'blind/ ':

    elif msg_arr[0] == 'hold/ ':

    elif msg_arr[0] == 'hold/ ':

    elif msg_arr[0] == 'inquire/ ':

    elif msg_arr[0] == 'flop/ ':

    elif msg_arr[0] == 'turn/ ':

    elif msg_arr[0] == 'river/ ':




#----------LOGIC PART-----------------


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
    else:
        processAllMsg(data)

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
