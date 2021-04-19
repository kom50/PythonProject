import mysql.connector
#
try:
    con = mysql.connector.connect(
        user='root',
        password='12345om',
    )
    if con.is_connected():
        print('Connected :-)')

    # creating cursor object
    cur = con.cursor()
    # mycur.execute('create database pythonDB')
    cur.execute('show databases')
    for a in cur:
        print(a)

except:
    print('Unable to connect :-) ')

# Install mysql-connector in pycharm
