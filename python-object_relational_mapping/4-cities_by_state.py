#!/usr/bin/python3
"""Connect to a MySQL database with MySQLdb
connector and print result of query"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name FROM cities
    LEFT JOIN states ON states.id = cities.state_id
    ORDER BY cities.id""")
    for row in c.fetchall():
        print(row)
