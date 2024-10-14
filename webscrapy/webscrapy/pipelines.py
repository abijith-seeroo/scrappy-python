# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class WebscrapyPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('my_quotes.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS test_1""")
        self.curr.execute("""create table test_1(title text,author  text,tags text) """)

    def store_db(self,item):
        query = """INSERT INTO test_1 (title, author, tags) VALUES (?, ?, ?)"""
        self.curr.execute(query, (item['title'][0], item['author'][0], item['tags'][0]))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
