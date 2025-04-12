import os
import mysql.connector.pooling
from dotenv import load_dotenv

load_dotenv()

dbconfig = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
}

class MySQLPool:
    def __init__(self):
        self.pool = self.create_pool(pool_name="main_pool", pool_size=5)

    def create_pool(self, pool_name, pool_size):
        return mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            **dbconfig
        )

    def close(self, conn, cursor):
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    def execute(self, sql, args=None, commit=False):
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql, args or ())
            if commit:
                conn.commit()
                last_id = cursor.lastrowid
                return last_id
            else:
                return cursor.fetchall()
        except Exception as e:
            print(f"[MySQL ERROR] {e}")
            return []
        finally:
            self.close(conn, cursor)

    def executemany(self, sql, args, commit=False):
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, args)
            if commit:
                conn.commit()
            else:
                return cursor.fetchall()
        except Exception as e:
            print(f"[MySQL ERROR] {e}")
            return []
        finally:
            self.close(conn, cursor)
