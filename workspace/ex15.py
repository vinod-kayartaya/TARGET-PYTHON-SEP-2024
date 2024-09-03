from typing import Any
from myutils import dir2


class Person:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.city = kwargs.get('city')

    def __str__(self) -> str:
        return f'Person(name={self.name}, email={self.email}, city={self.city})'
    
    def __setattr__(self, name: str, value: Any) -> None:
        if not name in ['name', 'city', 'email']:
            raise NameError(f'Invalid property name {name}')
        
        super().__setattr__(name, value)
    
    def print(self):
        print(f'Name  = {self.name}')
        print(f'Email = {self.email}')
        print(f'City  = {self.city}')
        print()
    
if __name__ == '__main__':
    p1 = Person(name='Vinod')
    p2 = Person()

    p1.email='vinod@vinod.co'
    p1.city = 1234
    # p1.state = 'Karnataka'
    
    p1.print()
    Person.print(p1)

    print(p1)
    print(p1.__str__())
    print(Person.__str__(p1))
    print(dir2(p1))
    print(dir2(p2))
