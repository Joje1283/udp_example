import socket
from time import sleep

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 소켓을 생성한다
    for i in range(10):
        sock.sendto(f"Hello {i}".encode(), ('127.0.0.1', 1700))
        data, addr = sock.recvfrom(200)
        print("client send and received data: ", data.decode())
        print("data from IP: ", addr[0])
        print("data from PORT: ", addr[1])
        sleep(1)
