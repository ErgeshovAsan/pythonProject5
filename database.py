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
                    phone_number TEXT NOT NULL,
                    product INTEGER NOT NULL,
                    rating INTEGER NOT NULL,
                    comment TEXT,
                    date DATE NOT NULL
                )
            """)
            conn.commit()


    def save_review(self, data: dict):
        with sqlite3.connect("db.sqlite3") as conn:
            conn.execute("""
                INSERT INTO reviews (name, phone_number, food_rating, cleanliness_rating, extra_comments, process_data)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (data["name"], data["phone_number"], data["food_rating"], data["cleanliness_rating"],
                 data["extra_comments"], data["process_data"]))




database = Database("db.sqlite3")