from datetime import date
from mysql.connector import Error
import datetime

class User():
    def __init__(self):
        self.fname: str 
        self.mname: str
        self.lname: str
        self.registered:str
        self.last_paid:str
        self.birth_day: str 
        self.password:str
        self.user_name:str
        self.email:str
        self.user_book:dict
        self.user_group:dict
    
    def sign_up(self,connection):
        print('Please fill out all of the information below:')
        print('---------------------------------------------')
        self.fname = input('Fist Name: ')
        self.mname = input('Middle Name: ')
        self.lname = input('Last Name: ')
        self.registered = date.today()
        self.last_paid = date.today()
        self.birth_day = datetime.datetime.strptime(input('Birthday (mm/dd/yyy): '),'%m/%d/%Y')
        self.user_name = input('User Name: ')
        self.email = input('Email: ')
        self.password = 'blank'
        password = ''
        while password != self.password:
            password = input('Password: ')
            self.password = input('Confirm Password: ')
            if password != self.password:
                print('Passwords must be identical, please try again')
        
        # Post the information to the database
        insert_query = f'''
        INSERT INTO users (`fname`,`mname`,`lname`,`registered`, `last_paid`,`birth_day`,`passwords`, `user_name`,`email`)
        VALUES ('{self.fname}','{self.mname}','{self.lname}','{self.registered}','{self.last_paid}','{self.birth_day}','{self.password}','{self.user_name}','{self.email}');'''
        try:   
            cursor = connection.cursor()
            cursor.execute(insert_query)
            connection.commit()
            print(cursor.rowcount,'Record inserted successfully into Users table')
            cursor.close()
        except Error as error:
            print('Failed to insert record into User table {}'.format(error))
        
    def sign_in(self,connection):
        self.user_name = input('User Name: ')
        self.password = input('Password: ')

        log_in = f'''SELECT passwords FROM users WHERE user_name = '{self.user_name}';'''
        try:   
            cursor = connection.cursor()
            cursor.execute(log_in)
            result = cursor.fetchone()
            cursor.close()
            if self.password == result[0]:
                return True
            else:
                return False
        except Error as error:
            print('Failed to insert record into User table {}'.format(error))
        

    
    

