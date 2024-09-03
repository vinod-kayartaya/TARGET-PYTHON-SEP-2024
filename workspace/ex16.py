class Employee:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get('name')
        self.gender = kwargs.get('gender')
        self.salary = kwargs.get('salary')

    # readable property (getter) for 'name'
    @property
    def name(self):
        return self.__name.upper()
    
    # writable property (setter) for 'name'
    @name.setter
    def name(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('name must be a str')
        
        if isinstance(value, str) and len(value)>25:
            raise ValueError('name must be <= 25 letters')
        
        self.__name = value

    # readable property (getter) for 'gender'
    @property
    def gender(self):
        return self.__gender.upper()
    
    # writable property (setter) for 'gender'
    @gender.setter
    def gender(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('gender must be a str')
        
        if isinstance(value, str) and \
            value.lower() not in ('m', 'f', 'male', 'female'):
            raise ValueError('gender must be one of "m", "f", "male", "female"')
        
        self.__gender = value

    # readable property (getter) for 'salary'
    @property
    def salary(self):
        return self.__salary
    
    # writable property (setter) for 'salary'
    @salary.setter
    def salary(self, value):
        if value is not None and type(value) not in(int, float):
            raise TypeError('salary must be a number')
        
        if value is not None and \
            (value < 25_000 or value > 500_000):
            raise ValueError('salary must be between 25000 to 500000')
        
        self.__salary = value

    def print(self):
        print(f'Name   : {self.__name}')
        print(f'Gender : {self.__gender}')
        print(f'Salary : {self.__salary}')


if __name__ == '__main__':
    e1 = Employee()
    e1.name = 'Ramesh'  # the setter for 'name' is called here
    e1.salary = 199_900
    e1.gender = 'MALE'
    # print(f'name is {e1.name}')  # the getter for name is called
    e1.print()