import mysql.connector as connector

config = {
    'user': 'root',
    'password': '12345om',
    'database': 'pythonDB'
}
try:
    con = connector.connect(**config)
    #  Create cursor object
    if con.is_connected():
        print("Connection successful")
    try:
        myc = con.cursor()
        myc.execute('SELECT *FROM student WHERE roll = %s', (102, ))
        rows = myc.fetchall()
        for r in rows:
            print(r)

        myc.close()
        con.close()
    except Exception as e:
        print('Problem occurs (:- ',  e)

except Exception as e:
    print('Unable to connect. :-) ', e)
