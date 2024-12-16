import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS reviews(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone_number INTEGER NOT NULL,
                    product INTEGER NOT NULL,
                    rating INTEGER NOT NULL,
                    comment TEXT,
                    data DATE NOT NULL
                )
            """)
            conn.commit()


    def save_review(self, data: dict):
        with sqlite3.connect("db.sqlite3") as conn:
            conn.execute("""
                INSERT INTO reviews (name, phone_number, product, rating, comment, data)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (data["name"], data["phone_number"], data["product"], data["rating"],
                      data["comment"], data["data"]))




database = Database("db.sqlite3")