import sqlite3

class ProductsDatabase:
    def __init__(self, pro_db):
        self.con = sqlite3.connect(pro_db)
        self.cur = self.con.cursor()

        sql= '''
        CREATE TABLE IF NOT EXISTS products(
        name text,
        count text,
        buy_price text,
        low_sell_price text,
        sell_price text,
        trader text,
        date_of_buy text,
        id Integer Primary Key
        )
'''

        self.cur.execute(sql)
        self.con.commit()

    def insert(self, name, count, buy_price, low_sell_price, sell_price, trader, date_of_buy):
        self.cur.execute('insert into products values(?,?,?,?,?,?,?,NULL)',
                        (name, count, buy_price, low_sell_price, sell_price, trader, date_of_buy))
        self.con.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM products')
        rows = self.cur.fetchall()
        return rows
    
    def update(self, id, name, count, buy_price, low_sell_price, sell_price, trader, date_of_buy):
        self.cur.execute('update products set name=?,count=?,buy_price=?,low_sell_price=?,sell_price=?,trader=?,date_of_buy=? where id=?',
                        (id, name, count, buy_price, low_sell_price, sell_price, trader, date_of_buy))
        self.con.commit()

    def update2(self, id, name, count, buy_price, low_sell_price, sell_price, trader, date_of_buy):
        self.cur.execute('insert into products values(?,?,?,?,?,?,?,?,NULL)',
                        (id, name, count, buy_price, low_sell_price, sell_price, trader, date_of_buy))
        self.con.commit()

    def remove(self, id):
        self.cur.execute('delete (name,count,buy_price,low_sell_price,sell_price,trader,date_of_buy) from products where id=?', (id,))
        self.con.commit()