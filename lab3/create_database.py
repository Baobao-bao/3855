import sqlite3

conn = sqlite3.connect('readings.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE stock_open_price
          (id INTEGER PRIMARY KEY ASC, 
           date VARCHAR(100) NOT NULL,
           stock_code VARCHAR(10) NOT NULL,
           open_price INTEGER)
          ''')


c.execute('''
          CREATE TABLE stock_news
          (id INTEGER PRIMARY KEY ASC, 
           date VARCHAR(100) NOT NULL,
           stock_code STRING NOT NULL,
           news VARCHAR(1000),
           source VARCHAR(20))
          ''')

conn.commit()
conn.close()




