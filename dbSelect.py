import pymysql
import pymysql.cursors

host = 'localhost'
user = 'root'
passwd = ''
db = 'pageview_simulation'

try:
    connection = pymysql.connect(host=host, user=user, password=passwd, database=db, cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()

    with open('dbQuery.sql', 'r') as SQLfile:
        SQLQuery = SQLfile.read()
    
    cursor.execute(SQLQuery)
    connection.commit()

    result = cursor.fetchall()
    cleaned_data = [f'{item['column_name']}, {int(item['total'])}' for item in result]
    
    with open('data.csv', 'wt+') as file:
        file.write('\n'.join(cleaned_data))
    
except pymysql.MySQLError as e:
    print(f'Error! --->  {e}')
    
finally:
    if connection:
        connection.close()