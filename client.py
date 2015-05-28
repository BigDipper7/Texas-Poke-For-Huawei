# -*- coding: utf-8 -*-
import socket, sys, chardet

if len(sys.argv) != 3:
    print 'Parameter not mate, notice must use like this:'
    print '\rpython client.py [ip] [port]'
    # print '\rpython client.py [ip] [port] [member_name]'
    sys.exit(0)

ip = sys.argv[1]
port = sys.argv[2]
# member = sys.argv[3]

# print chardet.detect(member)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_addr = (ip, 45567)
client.bind(client_addr)


# addr = ('192.168.56.1', 12234)
addr = (ip, int(port))

client.connect(addr)
# member ='许铭淏'
member = '第一组'
client.send(member)

data = client.recv(1024)
print 'data: ',data.decode('utf-8')

client.close()
