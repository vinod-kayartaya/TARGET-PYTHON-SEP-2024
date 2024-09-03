from ex16 import Employee


class Salesperson(Employee):
    def __init__(self, **kwargs) -> None:
        Employee.__init__(self, **kwargs)
        self.sales_target = kwargs.get('sales_target', 1_000_000)

    def print(self):
        super().print()
        print(f'Target : {self.sales_target}')

    def to_dict(self):
        d = {
            k.replace('_Employee__', ''): self.__dict__[k]
            for k in self.__dict__.keys()
        }

        return d

if __name__ == '__main__':
    s1 = Salesperson(name='Harish', sales_target = 1_500_000)
    s1.salary = 500_000
    s1.print()
    print(s1.to_dict())