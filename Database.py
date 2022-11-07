import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts(id integer primary key,"
                         "part_name text, customer text, type text, price text)")
        self.conn.commit()
    def fetch(self):
        self.cur.execute("SELECT *from parts")
        rows = self.cur.fetchall()
        return rows
    def insert(self, part, customer, type, price):
        self.cur.execute("insert into parts values(NULL, ?, ?, ?, ?)",
                         (part, customer, type, price))
        self.conn.commit()
    def remove(self,id):
        self.cur.execute("delete from parts where id=?", (id,))
        self.conn.commit()
    def update(self, id, part, customer, type, price):
        self.cur.execute("update parts set part = ?, customer=?, "
                         "type=?, price=? where id=?",
                         (part, customer, type, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


#db.insert("CPU", "Ivan Popov", "PcPartPicker", "1200")
#db.insert("Motherboard", "Kalin Donev", "PcPartPicker", "550")
#db.insert("Memory", "Georgi Stavrev", "PcPartPicker", "100")
#db.insert("Case", "Iva Mancheva", "PcPartPicker", "400")
