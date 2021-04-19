import mysql.connector as conn


def connector():
    try:
        con = conn.connect(
            user='root',
            password='12345om',
            database='pythondb'
        )
        if con.is_connected():
            print('Connected :-) ')
            return con
    except Exception as e:
        print('Unable to connect :-) ', e)
        return None
