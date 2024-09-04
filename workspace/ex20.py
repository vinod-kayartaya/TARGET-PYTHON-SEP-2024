from myutils import dir2


class Person:

    __id_counter = 0

    @classmethod
    def email(cls):
        return "office@xmpl.com"

    def __init__(self, name=None, city=None):
        Person.__id_counter += 1
        self.id = Person.__id_counter
        self.name = name
        self.city = city


if __name__ == '__main__':
    p1 = Person(name='Vinod', city='Bangalore')
    p2 = Person(name='Nagesh', city='Hyderabad')

    print(dir2(p1))
    print(dir2(p1))

    print(f'id={p1.id}, name={p1.name}, city={p1.city}, email={Person.email()}')
    print(f'id={p2.id}, name={p2.name}, city={p2.city}, email={Person.email()}')

    # Person.email = 'newemail.example.com'
    # print(f'name={p1.name}, city={p1.city}, email={p1.email}')
    # print(f'name={p2.name}, city={p2.city}, email={p2.email}')

    # p1.email = 'anotheremail@xmpl.com'
    # print(f'name={p1.name}, city={p1.city}, email={p1.email}')
    # print(f'name={p2.name}, city={p2.city}, email={p2.email}')
