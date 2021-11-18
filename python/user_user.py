from datetime import date
from mysql.connector import Error

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
        self.birth_day = input('Birthday: ')
        self.user_name = input('User Name: ')
        self.email = input('Email: ')

        password = ''
        while password != self.password:
            password = input('Password: ')
            self.password = input('Confirm Password: ')
            if password != self.password:
                print('Passwords must be identical, please try again')
        
        # Post the information to the database
        insert_query = f'''
        INSERT INTO users (fname,mname,lname,registered,
                           last_paid,birth_day,password,
                           user_name,email)
        VALUES ({self.fname},{self.mname},{self.lname},{self.registered},
                {self.last_paid},{self.birth_day},{self.password},
                {self.user_name},{self.email})
        '''
        try:   
            cursor = connection.cursor()
            cursor.execute(insert_query)
            connection.commit()
            print(cursor.rowcount,'Record inserted successfully into Laptop table')
            cursor.close()
        except Error as error:
            print('Failed to insert record into User table {}'.format(error))
        

    
    

