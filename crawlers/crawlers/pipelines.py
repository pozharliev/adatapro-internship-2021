import logging
import sqlite3

class CrawlersPipeline:
    def __init__(self):
        self.connection = sqlite3.connect("./availablePS5.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS AvailablePS5
                (
                    id INTEGER PRIMARY KEY, 
                    site VARCHAR(255), 
                    availability VARCHAR(255), 
                    price DECIMAL(255)
                )
            """
            )

    def process_item(self, item, spider):
        self.cursor.execute(
            """INSERT INTO AvailablePS5 (site, availability, price) values (?, ?, ?)""",
            (item["site"], item["availability"], item["price"]),
        )
        self.connection.commit()
        logging.debug("Item stored {}".format(item["site"]))
        return item
