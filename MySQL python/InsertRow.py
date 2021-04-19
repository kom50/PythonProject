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
        sql = '''INSERT INTO student (name, roll, fees) VALUES ("Rahul", 101, 2300.50), ("Chandan", 102, 1500.90), 
        ("Jai", 103, 1200.50), ("Pintu", 104, 1500.45) '''
        cur.execute(sql)
        print(cur.rowcount, 'rows inserted :-) ')
        print('std id :- ', cur.lastrowid)
        con.commit()
    except Exception as e:
        con.rollback()
        print('record is not inserted :-) ', e)

except Exception as e:
    print('Unable to connect :-) ')



