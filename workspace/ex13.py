from myutils import lined, repeat


@lined
def say_hello():
    print("Hello, world!")


@repeat(3)
def greet():
    print("Welcome to python.")


def main():
    say_hello()
    greet()


if __name__ == '__main__':
    main()
