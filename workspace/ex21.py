from sqlite3 import connect
# from psycopg2 import connect

def get_connection():
    return connect(dsn="postgresql://sandbox_owner:VQdWa1CFgAK7@ep-falling-shape-a5g06ay7.us-east-2.aws.neon.tech/sandbox?sslmode=require")


def get_connection():
    return connect('customers_data.db')


def create_customers_table():
    pg_sql = """CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE,
    city VARCHAR(50) DEFAULT 'Bangalore'
    )"""

    sqlite_sql = """CREATE TABLE customers (
    id integer PRIMARY KEY autoincrement,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE,
    city VARCHAR(50) DEFAULT 'Bangalore'
    )"""

    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(sqlite_sql)
        cur.close()


def add_customer_record():
    print('Enter customer details: ')
    name = input('Name : ')
    city = input('City : ')
    email = input('Email: ')
    sql = 'insert into customers (name, city, email) values (?, ?, ?)'
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(sql, (name, city, email))
        conn.commit()
        print('Done!')


def search_customer():
    customer_id = int(input('Enter customer id to search: '))
    sql = 'select * from customers where id = ?'
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(sql, (customer_id, ))
        row = cur.fetchone()
        if row is None:
            print(f'No data found for id {customer_id}')
        else:
            header = [c[0] for c in cur.description]
            # header = ['name', 'city', 'email']
            customer = dict(zip(header, row))
            print(f'Name  : {customer['name']}')
            print(f'City  : {customer['city']}')
            print(f'Email : {customer['email']}')


if __name__ == '__main__':
    # create_customers_table()
    # add_customer_record()
    search_customer()