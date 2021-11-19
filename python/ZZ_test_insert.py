import mysql.connector
from mysql.connector import Error
from datetime import date, datetime

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='recipe_app',
                                         user='root',
                                         password='2001053597Rex?')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        registered = datetime.strptime('11/18/2021','%m/%d/%Y')
        last_paid = datetime.strptime('11/18/2021','%m/%d/%Y')
        birthday = datetime.strptime('12/16/1999','%m/%d/%Y')

        insert_query = f'''
        INSERT INTO users (`fname`,`mname`,`lname`,`registered`, `last_paid`,`birth_day`,`passwords`, `user_name`,`email`)
        VALUES ('Marin','LaRee','Fuqua','{registered}','{last_paid}','{birthday}','2001053597Rex?','mfuqua','mcrockett@gmail.com');'''
        cursor.execute(insert_query)
        connection.commit()
        print(cursor.rowcount,'Record inserted successfully into users table')
        cursor.close()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")