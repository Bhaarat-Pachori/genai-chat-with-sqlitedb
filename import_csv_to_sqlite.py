import pandas as pd
import sqlite3


class SqliteConnect:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def make_connection(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_connect_n_cursor(self):
        return self.connection, self.cursor

    def commit_to_table(self):
        self.connection.commit()

    def kill_connection(self):
        self.connection.close()


def create_sqlite_database(db_name: str, tab_name: str, conn_obj: SqliteConnect):
    # Connect to your SQLite database
    conn_obj.make_connection(db_name)
    conn, cursor = conn_obj.get_connect_n_cursor()
    conn.cursor()

    # Read your CSV file in chunks (adjust chunk_size as needed)
    chunk_size = 10000
    for chunk in pd.read_csv('flights.csv', chunksize=chunk_size):
        chunk.to_sql(tab_name, conn, if_exists='append', index=False)

    # Create an index on the 'orig' column
    cursor.execute('CREATE INDEX idx_orig ON flights_details (origin)')

    # Commit changes and close the connection
    conn_obj.commit_to_table()
    conn_obj.kill_connection()

if __name__ == '__main__':
    sql_con = SqliteConnect()
    create_sqlite_database("flights.db", "flights_details", sql_con)

    # execute a query to test the data points count
    sql_con.make_connection("flights.db")
    conn, cursor = sql_con.get_connect_n_cursor()
    # _ = cursor.execute('''SELECT COUNT(*) FROM flights_details''')
    # print(f"Total rows in table: {cursor.fetchone()[0]}")
    # rows = cursor.execute('''SELECT COUNT(*) FROM flights_details WHERE dest = 'MIA' AND month = '08' AND year = '2013';''')
    # chunk_size = 100  # Adjust this based on your needs
    # while True:
    #     rows = cursor.fetchmany(chunk_size)
    #     if not rows:
    #         break  # No more rows to fetch
    #
    #     for row in rows:
    #         # Process each row in the chunk (e.g., print, analyze, etc.)
    #         print(row)

    sql_con.kill_connection()
