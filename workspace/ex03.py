from ex02 import say_hello

if __name__ == '__main__':
    # this block is executed only when this file run (and not imported)
    msg = say_hello("Vinod")
    print(msg)
    msg = say_hello("Uday", "Delhi")
    print(msg)
    print(msg)
    msg = say_hello(city="Mumbai", name="Rohit")
    print(msg)
