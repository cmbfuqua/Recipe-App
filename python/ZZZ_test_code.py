
from user_user import User
import mysql.connector
from mysql.connector import Error

try:
        connection = mysql.connector.connect(host='localhost',
                                            database='recipe_app',
                                            user='root',
                                            password='2001053597Rex?')
        if connection.is_connected():
            print("You're connected to database")

        log_in = f'''SELECT count(user_name) FROM users;'''
        cursor = connection.cursor()
        cursor.execute(log_in)
        result = cursor.fetchall()
        cursor.close()
        print(result[0][0])
        print(type(result[0][0]))
        print('bfuqua' in result)
        if result:
            unique = False
            print('That user name already exists. Please try again.')   

except Error as e:
    print("Error while connecting to MySQL", e)
# %%
