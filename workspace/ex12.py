def say_hello(name, city, /):
    print(f'Hello {name}. How is weather in {city}?')


def average(*args):
    nums = [n for n in args if type(n) in (int, float)]
    return sum(nums)/len(nums)


def create_person(**kwargs):
    person = {}
    person['name'] = kwargs.get('fname', '') + ' ' + kwargs.get('lname', '')
    person['name'] = person['name'].strip()
    person['email'] = kwargs.get('email', 'no email available')
    person['phone'] = kwargs.get('phone', 'no phone available')
    return person


def main():

    p1 = create_person(fname='Vinod', lname='Kumar', email='vinod@vinod.co')
    p2 = create_person(username='Shyam')

    print(p1)
    print(p2)

    # say_hello('Vinod', 'Bangalore')
    # say_hello(city='Bangalore', name='Vinod')
    # avg = average(10, 20, 3.4, 59.2, False, 'Vinod')
    # print(f'{avg = }')

    # data = [10, 20, 22.22, 19.4, 'Vinod', 0.4]
    # avg = average(*data)
    # print(f'{avg = }')


if __name__ == '__main__':
    main()
