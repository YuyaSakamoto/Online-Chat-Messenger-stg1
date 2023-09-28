import socket

server_address = '127.0.0.1'
server_port = 12345
buffsize = 4096
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def recv_message():
    data = udp_sock.recv(buffsize)
    message = data.decode()
    print(f'{message}')

def send_message():
    message = input('write a message: ')
    full_message =  message.encode()
    udp_sock.sendto(full_message, (server_address, server_port))

def main():
    send_message()
    recv_message()

if __name__=="__main__":
    main()