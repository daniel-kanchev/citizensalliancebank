from itemadapter import ItemAdapter
import sqlite3


class DatabasePipeline:
    # Database setup
    conn = sqlite3.connect('citizensalliancebank.db')
    c = conn.cursor()

    def open_spider(self, spider):
        self.c.execute(""" DROP TABLE IF EXISTS articles """)

        self.c.execute(""" CREATE TABLE articles (
        title text,
        content text
        ) """)

    def process_item(self, item, spider):
        # Insert values
        self.c.execute("INSERT INTO articles ("
                       "title, "
                       "content)"
                       " VALUES (?,?)",
                       (item.get('title'),
                        item.get('content')
                        ))

        print(f"New Article: {item['title']}")

        self.conn.commit()  # commit after every entry

        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()