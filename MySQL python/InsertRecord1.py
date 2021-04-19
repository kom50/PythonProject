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
        while True:
            nm = input('Enter your name :- ')
            rl = int(input("Enter roll no :- "))
            fs = float(input("Enter fees :- "))

            records = (nm, rl, fs)
            cur.execute(sql, records)  # this method is used to insert multiple record in mysql database

            print(cur.rowcount, 'rows inserted :-) ')
            print('std id :- ', cur.lastrowid)
            con.commit()
            ans = input("Enter y/n :- ")
            if ans is 'n' or ans is 'N':
                break
    except Exception as e:
        con.rollback()
        print('record is not inserted :-) ', e)

except Exception as e:
    print('Unable to connect :-) ', e)



