from database import SqliteConn


def create_user_table(db):
    db.update('CREATE TABLE users (first_name text, last_name text)', ())


def main():
    db = SqliteConn(db_file='flask-simple-example.db')
    db.connect_to_db()
    create_user_table(db)


if __name__ == "__main__":
    main()
