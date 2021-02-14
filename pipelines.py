# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class Assignment1Pipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='postgres',
            database='news_data')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" drop table if exists news""")
        self.curr.execute("""create table news(
                              Date text,
                              Headline text
                              )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into news values (%s,%s)""", (
            item['Date'][0],
            item['Headline'][0]
        ))
        self.conn.commit()
