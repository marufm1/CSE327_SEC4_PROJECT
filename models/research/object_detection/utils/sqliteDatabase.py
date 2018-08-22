import sqlite3

conn = sqlite3.connect('Fruits.db')
c = conn.cursor()
name = 'banana'

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS FruitsList(fname Text, details Text)')


def read_from_db():
    c.execute("SELECT details FROM FruitsList WHERE fname = 'banana' ")
    data = c.fetchone()
    print (data)

read_from_db()





c.close()
conn.close()
