from socket import socket, AF_INET, SOCK_STREAM
import json


def main():

    while True:
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_addr = ('192.168.158.156', 1234)
        print(f'connecting to the server at {server_addr}')
        server_socket.connect(server_addr)

        print("""
    0. Exit
    1. Factorial of `a`
    2. `a` raised to the power of `b`
              
""")
        req = {}
        choice = int(input('Enter your choice: '))
        if choice == 0:
            break

        if choice == 1:
            req['method_name'] = 'factorial'
            num = int(input('Enter a number: '))
            req['method_args'] = (num, )
        elif choice == 2:
            req['method_name'] = 'power'
            a = int(input('Enter value for `a`: '))
            b = int(input('Enter value for `b`: '))
            req['method_args'] = (a, b)
        else:
            print('Invalid choice!!!')
            continue

        server_socket.send(json.dumps(req).encode())
        resp = server_socket.recv(1024).decode()
        resp = json.loads(resp)

        print(f'The result is {resp["result"]}')

if __name__ == '__main__':
    main()
    