import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 1700))

if __name__ == '__main__':
    while True:
        data, addr = sock.recvfrom(200)
        sock.sendto(data, addr)
        print(" Server is received data : ", data.decode())
        print(" Send Client IP : ", addr[0])
        print(" Send Client Port : ", addr[1])
        print(" Server return data to ", addr[0])