import mysql.connector as connector
config = {
    'user': 'root',
    'password': '12345om',
    'database': 'pythonDB'
}
try:
    con = connector.connect(**config)
    try:
        cur = con.cursor()
        sql = 'SELECT * FROM student WHERE roll= %(id)s'
        data = {'id': 102}  # (101, )   #
        cur.execute(sql, data)

        rows = cur.fetchall()
        for row in rows:
            print(f' {row[0]} {row[1]} {row[2]}')

        cur.close()   # close cursor object
        con.close()   # close connection object
    except Exception as e:
        con.rollback()
        print('Unable to show. :-) ', e)

except Exception as e:
    print('Unable to connect. :-) ', e)
else:
    print('Connected. ')
