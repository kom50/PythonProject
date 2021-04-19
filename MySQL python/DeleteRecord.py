import mysql.connector as connector
config = {
    'user' : 'root',
    "password" : '12345om',
    'database' : 'pythondb'
}
try:
    # Creating connection object
    conn = connector.connect(**config)
    # Check connection
    if conn.is_connected():
        print('Connected')

    try:
        # Creating cursor object
        cur = conn.cursor()
        sql = 'delete from student where stdid = 4'
        cur.execute(sql)     # execute query
        print(cur.rowcount, 'record deleted. :-) ')
        conn.commit()
    except Exception as e:
        conn.rollback()
        print('Error :- ', e)
    conn.close()

except:
    print('Unable to connect :-) ')

