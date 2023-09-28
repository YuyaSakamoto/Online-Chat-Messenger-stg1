import socket
        
class Server:
    def __init__(self):
        self.address = '127.0.0.1'
        self.port = 12345
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind((self.address,self.port))
        self.buffsize = 4096
        print(f'serverが起動しました: {self.address}:{self.port}')
    
def handle_client(server):
    data, address = server.sock.recvfrom(server.buffsize)
    message = data.decode()
    print(f'print: {message}')
    server.sock.sendto(data,address)
    
def main():
    server = Server()
    while True:
        try:
            handle_client(server)
        except KeyboardInterrupt as e:
            print(e)
            server.sock.close()

if __name__ == '__main__':
    main()