import sqlite3


class SqliteConn():
    def __init__(self, db_file='example.db'):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect_to_db(self):
        """ Connect to database and initialize cursor """
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def update(self, query, params):
        self.cursor.execute(query, params)
        self.conn.commit()

    def first(self, query, params):
        self.cursor.execute(query, params)
        # Gets a tuple of the fields in the table
        return self.cursor.fetchone()

    def all(self, query, params):
        self.cursor.execute(query, params)
        # Gets a tuple of the fields in the table
        return self.cursor.fetchall()
