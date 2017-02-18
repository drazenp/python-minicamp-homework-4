import sqlite3

connection = sqlite3.connect('database.db')
print('Opend databse successfully')

connection.execute('CREATE TABLE movies (title TEXT, Description TEXT)')
print('Table created successfully');

connection.close()