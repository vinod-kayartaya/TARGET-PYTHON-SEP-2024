from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['customers_db']

if __name__ == '__main__':
    customers = db.customers.find()

    for c in customers:
        print(c.get('name'))


if __name__ == '__main__1':
    print('Enter customer details: ')
    name = input('Name : ')
    city = input('City : ')
    email = input('Email: ')
    cust = {'name': name, 'city': city, 'email': email}
    db.customers.insert_one(cust)
    print('Saved')
    