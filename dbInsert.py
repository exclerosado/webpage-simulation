import pymysql
import pymysql.cursors

host = 'localhost'
user = 'root'
passwd = ''
db = 'pageview_simulation'


def insert_data(_clienteID, _landing_page, _personal_data, _address_data, _payment_data, _confirmation, _goal, _date_time):
    try:
        connection = pymysql.connect(host=host, user=user, password=passwd, database=db, cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        
        sql = 'INSERT INTO web_page_logs (clientID, landing_page, personal_data, address_data, payment_data, confirmation, goal, date_time) VALUES (%(clientID)s, %(landing_page)s, %(personal_data)s, %(address_data)s, %(payment_data)s, %(confirmation)s, %(goal)s, %(date_time)s)'
        vals = {
            'clientID': _clienteID,
            'landing_page': _landing_page,
            'personal_data': _personal_data,
            'address_data': _address_data,
            'payment_data': _payment_data,
            'confirmation': _confirmation,
            'goal': _goal,
            'date_time': _date_time
        }
        
        cursor.execute(sql, vals)
        connection.commit()
        
    except pymysql.MySQLError as e:
        print(f'Error! --->  {e}')
        
    finally:
        if connection:
            connection.close()
