from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import json, math


def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def handle_client(client_socket, client_addr):
    print(f'got a connection from a client at {client_addr}')
    req = client_socket.recv(1024).decode()
    req = json.loads(req)

    resp = {}

    if req['method_name'] == 'factorial':
        resp['result'] = factorial(*req['method_args'])
    elif req['method_name'] == 'power':
        resp['result'] = math.pow(*req['method_args'])

    client_socket.send(json.dumps(resp).encode())
    client_socket.close()


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_addr = ('192.168.158.156', 1234)
    server_socket.bind(server_addr)
    server_socket.listen()
    print(f'server started at {server_addr[0]}:{server_addr[1]}')
    while True:
        print('waiting for client connection...', flush=True)
        client_socket, client_addr = server_socket.accept()
        Thread(target=handle_client, args=(client_socket, client_addr)).start()



if __name__ == '__main__':
    main()
