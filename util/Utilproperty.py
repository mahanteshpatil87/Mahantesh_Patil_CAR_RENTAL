import mysql.connector as sql
import time


class DBConnUtil:
    @staticmethod
    def getConnection():
        host = "localhost"
        database = "MAY"
        user = "root"
        password = "123456"

        try:
            conn = sql.connect(host=host, database=database, user=user, password=password)
            if conn.is_connected():
                time.sleep(0.5)
                print("Connection successful")
                return conn
            else:
                print("Unable to connect")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None


DBConnUtil.getConnection()
