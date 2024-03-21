import sqlite3


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection


sql_to_create_products_table = '''CREATE TABLE Products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER DEFAULT NULL
)'''


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


my_connection = create_connection('products.db')
if my_connection is not None:
    print('Successfully connected')
    # create_table(my_connection, sql_to_create_products_table)


def products(connection, product):
    sql = '''INSERT INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_products(connection, product):
    sql = '''UPDATE products SET price = ?, WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products(connection, limit, price):
    sql = ''''SELECT * FROM products WHERE price <= ? and quantity > ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (limit, price))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def delete_products(connection, id):
    sql = '''DELETE  FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def find_by_keyword(connection, keyword):
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM products WHERE product_title LIKE ?''', ('%' + keyword + '%',))
        products = cursor.fetchall()
        return products
    except sqlite3.Error as e:
        print("Произошла ошибка при выполнении запроса:", e)
        return None


# products(my_connection, ('Milk', 80, 6))
# products(my_connection, ('Bread', 35, 8))
# products(my_connection, ('Salt', 30, 15))
# products(my_connection, ('Cookies', 160, 13))
# products(my_connection, ('Oil', 130, 12))
# products(my_connection, ('Rice', 130, 25))
# products(my_connection, ('Cheese', 450, 3))
# products(my_connection, ('Eggs', 130, 20))
# products(my_connection, ('Meat', 500, 7))
# products(my_connection, ('Bananas', 200, 5))
# products(my_connection, ('Tomato', 170, 10))
# products(my_connection, ('Potato', 50, 10))
# products(my_connection, ('Мыло', 60, 9))
# products(my_connection, ('Мыло ванильное', 55, 12))
# products(my_connection, ('Pelmeni', 100, 14))
# products(my_connection, ('Juice', 130, 11))
# find_by_keyword(my_connection, 'Мыло')
# select_products(my_connection, 100, 5)
# select_all_products(my_connection)
# products(my_connection, ('Milk', 80, 6))
# delete_products(my_connection, 20)
my_connection.close()
