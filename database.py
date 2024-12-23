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
                    food_rating INTEGER NOT NULL,
                    cleanliness_rating INTEGER NOT NULL,
                    extra_comments TEXT,
                    process_data DATE NOT NULL
                )
            """)
            conn.execute("""
                            CREATE TABLE IF NOT EXISTS dishes(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                price INTEGER NOT NULL,
                                description TEXT NOT NULL,
                                category TEXT
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

    def save_dish(self, data: dict):
        with sqlite3.connect("db.sqlite3") as conn:
            conn.execute("""
                INSERT INTO dishes (name, price, description, category)
                VALUES (?, ?, ?, ?)
                """,
                (data["name"], data["price"], data["description"], data["category"]))

    def get_all_dishes(self):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute("SELECT name, price, description, category FROM dishes ORDER BY price")
            result.row_factory = sqlite3.Row
            data = result.fetchall()

            return [dict(row) for row in data]




database = Database("db.sqlite3")