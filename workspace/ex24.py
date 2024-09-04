from threading import Thread, current_thread
import time


def do_something(message='doing something', limit=10):
    for i in range(limit):
        print(f'{message} for {i}th time in the {current_thread().name }')
        time.sleep(0.25)

    
def print_dots():
    while True:
        print('.', end='', flush=True)
        time.sleep(0.25)


def main():
    start_time = time.time()
    t1 = Thread(target=do_something, name='my_thread_1', kwargs={'message': 'walking', 'limit': 7})
    t2 = Thread(target=do_something, args=('walking', 5))
    t1.start()
    t2.start()

    # t3 = Thread(target=print_dots)
    # t3.daemon = True
    # t3.start()
    Thread(target=print_dots, daemon=True).start()

    # t1.join()
    # t2.join()

    threads = [t1, t2]
    [t.join() for t in threads]

    end_time = time.time()
    print(f'total time take is {end_time - start_time}ms')



if __name__ == '__main__':
    print(f'starting the app in the {current_thread().name}')
    main()
