import mysql.connector as connector

try:
    con = connector.connect(
        user='root',
        password='12345om',
        database='pythondb'
    )
    #check connect
    if con.is_connected():
        print('Connected (:-')

    try:
        # creating cursor object
        mycur = con.cursor()
        mycur.execute('''
                      CREATE TABLE student( 
                            stdid int  PRIMARY KEY AUTO_INCREMENT,
                            name varchar(20) not null,
                            roll int not null,
                            fees float not null
                      )
        ''')
        print('table is created');
    except Exception as e:
        print('Table is not created (:- ', e)

except Exception as e:
    print('Unable to connect ', e)

# mycur.close()
# con.close()