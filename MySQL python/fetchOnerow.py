import mysql.connector as conn

config = {
    'user': 'root',
    'password': '12345om',
    'database': 'pythonDB'
}
try:
    con = conn.connect(**config)

    if con.is_connected():
        print('Connected. ')

    try:
        cur = con.cursor()
        # fetch one row
        sql = 'SELECT *FROM student'
        cur.execute(sql)
        row = cur.fetchone()    # fetch one record at a time
        a = '-'
        print(f'{a:->37}')
        print(' Stu Id\t  Name\t      Roll\t   Fees')
        print(f'{a:->37}')
        while row is not None:
            # print(row)
            # print(f'Stu Id : {row[0]}, name : {row[1]}, roll : {row[2]}, fees : {row[3]}')
            print(f'{row[0]:4}\t  {row[1]:6}\t{row[2]:5}\t{row[3]:5,.2f}')
            row = cur.fetchone()
        print(f'{a:->37}')
        cur.close()
    except:
        print('Something wrong.')

    con.close()
except Exception as e:
    print('Unable to connect. ', e)
