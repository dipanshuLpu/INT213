import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS pms (id INTEGER PRIMARY KEY, part text, customer text, vnumber text, time text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM pms")
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, vnumber, time):
        self.cur.execute("INSERT INTO pms VALUES (NULL, ?, ?, ?, ?)",
                         (part, customer, vnumber, time))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM pms WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, vnumber, time):
        self.cur.execute("UPDATE pms SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                         (part, customer, vnumber, time, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

