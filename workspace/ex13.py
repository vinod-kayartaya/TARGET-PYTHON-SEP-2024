from myutils import *


@lined
def say_hello():
    print("Hello, world!")


@args_to_uppercase
@repeat(3)
def greet(msg):
    print(msg)

@args_to_uppercase
def print_info(name, age, email):
    line(length=20)
    print(f'Name  = {name}')
    print(f'Age   = {age} years')
    print(f'Email = {email}')
    line(length=20)


def main():
    say_hello()
    greet("Hello, and welcome to Python")
    print_info('John', 33, 'Dallas')

if __name__ == '__main__':
    main()
