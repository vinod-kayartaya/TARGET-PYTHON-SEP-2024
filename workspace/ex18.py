class Phone:
    def __init__(self) -> None:
        super().__init__()
        print('Phone.__init__() called')

class MobilePhone(Phone):
    def __init__(self) -> None:
        super().__init__()
        print('MobilePhone.__init__() called')

    def fn(self):
        print('MobilePhone.fn() called')

class Camera:
    def __init__(self) -> None:
        super().__init__()
        print('Camera.__init__() called')

    def fn(self):
        print('Camera.fn() called')

class SmartPhone(Camera, MobilePhone):
    def __init__(self) -> None:
        super().__init__()
        print('SmartPhone.__init__() called')

if __name__ == '__main__':
    sp = SmartPhone()
    print(SmartPhone.mro())
    sp.fn()  # calls from Camera because of MRO
    MobilePhone.fn(sp)
    sp.__init__()