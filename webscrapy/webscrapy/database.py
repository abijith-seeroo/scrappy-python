import sqlite3

conn=sqlite3.connect('my_quotes.db')
curr=conn.cursor()


query="""create table test_1(title text,author  text,tags text) """
query="""INSERT INTO test_1 VALUES ('thomas','john','jomon')"""
curr.execute(query)
conn.commit()
conn.close()