import sqlite3

conn = sqlite3.connect('readings.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE stock_open_price
          ''')

c.execute('''
          DROP TABLE stock_news
          ''')

conn.commit()
conn.close()
