import mysql.connector as connector
try:
    con = connector.connect(
        user='root',
        password='12345om',
        database='pythonDB'
    )
    try:
        # Check connection
        if con.is_connected():
            print('Connected')
        # Creating cursor object
        cur = con.cursor()
        # Insert multiple record
        sql = 'INSERT INTO student (name, roll, fees) VALUES (%s, %s, %s)'
        records = [('Raju', 105, 15000.20), ("Chandu", 106, 16000), ("Rahul ", 107, 1800.50)]
        cur.executemany(sql, records)    # this method is used to insert multiple record in mysql database

        print(cur.rowcount, 'rows inserted :-) ')
        print('std id :- ', cur.lastrowid)
        con.commit()
    except Exception as e:
        con.rollback()
        print('record is not inserted :-) ', e)
        
except Exception as e:
    print('Unable to connect :-) ', e)



