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
    c.execute("""SELECT * FROM states""")
    for row in c.fetchall():
        print(row)
