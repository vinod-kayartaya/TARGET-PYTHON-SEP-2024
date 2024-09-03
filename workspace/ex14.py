from myutils import dir2


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f'Book object with title="{self.title}" and price={self.price}'


if __name__ == '__main__':
    b1 = Book('Let us C', 299)
    b2 = Book('Python Unleashed', 2999)

    print(b1)
    print(b2)