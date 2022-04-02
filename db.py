import json
from tkinter import messagebox
import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='krishna.r.k28091',
    database='supermarket'
)

dummy_product_details = [
   
    {
        'product_id': 2,
        'product_name': 'Chocolates',
        'price': 10.0
    },
    {
        'product_id': 3,
        'product_name': 'Coffee',
        'price': 10.0
    },
    {
        'product_id': 4,
        'product_name': 'Tea',
        'price': 10.0
    },
    {
        'product_id': 5,
        'product_name': 'Brush',
        'price': 10.0
    },
]
# done
def insert_product_in_db(product):
    with connection.cursor() as cursor:
        sql = 'INSERT INTO product_detail(product_id, product_name, price, quantity, category) values (%s, %s, %s, %s, %s)'
        cursor.execute(sql, (product['product_id'], product['product_name'], product['price'], product['quantity'], product['category']))
    connection.commit()
# done
def delete_product_from_db(product_id: int):
    with connection.cursor() as cursor:
        sql = 'DELETE FROM product_detail WHERE product_id=%s'
        cursor.execute(sql, product_id)
        print(f'{cursor.rowcount} rows deleted')
    connection.commit()
# done
#  array is not supported in mysql java script notation language
def get_order_details():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM orders"
        cursor.execute(sql)
        order_details = cursor.fetchall()
        return_detail = []
        for detail in order_details:
            product_detail = json.loads(detail[4])
            return_detail.append((
                detail[0],
                detail[1],
                detail[2],
                detail[3],
                product_detail
            ))
        return return_detail

def add_order_in_db(details):
    order_details = json.dumps(details['order_details']) #json-----------------------------------------------------------
    with connection.cursor() as cursor:
        sql = "INSERT INTO orders(customer_name, total, od_dt, order_details) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (details['customer_name'], details['total'], details['od_dt'], order_details))
        print(f'Order {cursor.lastrowid} added')
    connection.commit()
    messagebox.showinfo("showinfo", "Your order has been placed")
    
    # added directly in message boxes 

def search_products(name: str):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM product_detail where product_name=%s"
        cursor.execute(sql, (name))
        ok=cursor.fetchall()
        # connection.commit()
    messagebox.showinfo("showinfo",ok)
#     pass

def get_products():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM product_detail"
        cursor.execute(sql)
        return cursor.fetchall()

def get_products_by_category(category: str):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM product_detail where category=%s"
        cursor.execute(sql, (category))
        return cursor.fetchall()

def update_product_detail(product_id: int, details):
    with connection.cursor() as cursor:
        print(details)
        sql = f"UPDATE product_detail SET product_name = %s, price = %s, quantity = %s where product_id = %s"
        cursor.execute(sql, (details['product_name'], details['price'], details['quantity'], product_id))
    connection.commit()
    
def get_product_category():
    with connection.cursor() as cursor:
        sql = """SELECT COLUMN_TYPE AS allCategories 
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_SCHEMA = 'supermarket' AND TABLE_NAME = 'product_detail' AND COLUMN_NAME = 'categories'"""
        cursor.execute(sql)
        row = cursor.fetchone()
        print(row)

#  when mysql not working , to check order 
if __name__ == "__main__":
    # add_order({
    #     'customer_name': 'Krishna',
    #     'total': 300,
    #     'od_dt': '2022-03-27'
    # })
    # with connection.cursor() as cursor:
    #     sql = "alter table product_detail modify column category enum(%s, %s, %s, %s) not null"
    #     cursor.execute(sql, ('food', 'daily needs', 'beverages', 'electronics'))
    get_product_category()
    pass