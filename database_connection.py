# DATABASE ACCESS MODULE WHERE DATA FROM DATABASE IS ACCESSED AND DATA IS FETCHED #

import mysql.connector


class DatabaseConnection:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='admin@123',
                                           host='localhost',
                                           database='sample_db')
        self.my_cursor = self.cnx.cursor()
        self.internal_products = []
        self.external_products = []
        self.fetch_data()

    # TODO ALL DATA FROM PRODUCTS_EXTERNAL AND PRODUCTS_INTERNAL IS BEING FETCHED
    #  PRODUCT ID ID THE PRIMARY NON-NULL KEY IN BOTH THE TABLES.
    def fetch_data(self):
        self.my_cursor = self.cnx.cursor()
        self.my_cursor.execute("SELECT * FROM products_external")
        self.external_products = self.my_cursor.fetchall()
        self.my_cursor.execute("SELECT * FROM products_internal")
        self.internal_products = self.my_cursor.fetchall()
