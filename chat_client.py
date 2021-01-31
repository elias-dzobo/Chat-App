import socket
import sys
import threading

def send_message(s, d_port):
    while True:
        message = input('Enter a message: ')
        if message:
            s.sendto(message.encode(), ('localhost', d_port))

def receive_message(s):
    while True:
        data, addr = s.recvfrom(1024)
        if data:
            print(f'\nreceived: {data.decode()}\nEnter a message: ', end='')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)
    port = int(sys.argv[1])
    destination_port = int(sys.argv[2])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('localhost', port))
    print('client started.....')
    threading.Thread(target=send_message, args=(sock, destination_port)).start()
    threading.Thread(target=receive_message, args=(sock,)).start()