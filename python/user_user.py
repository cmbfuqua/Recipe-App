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
        self.user_id:int

    def set_password(self):
        password = ''
        while password != self.password:
            password = input('Password: ')
            self.password = input('Confirm Password: ')
            if password != self.password:
                print('Passwords must be identical, please try again')
    
    def sign_up(self,connection):
        print('Please fill out all of the information below:')
        print('---------------------------------------------')
        self.fname = input('Fist Name: ')
        self.mname = input('Middle Name: ')
        self.lname = input('Last Name: ')
        self.registered = date.today()
        self.last_paid = date.today()
        unique = False
        # This is the logic to check for a unique user name in the database. 
        # it needs to be unique or else the password verrification won't work.
        while unique == False:
            self.user_name = input('User Name: ')
            log_in = f'''SELECT count(user_name) FROM users where user_name = '{self.user_name}';'''
            cursor = connection.cursor()
            cursor.execute(log_in)
            result = cursor.fetchall()
            #print(result[0][0])           
            if result[0][0] > 0:
                unique = False
                print('That user name already exists. Please try again.\n')
                cursor.close()
            else:
                cursor.close()
                unique = True      
        self.birth_day = datetime.datetime.strptime(input('Birthday (mm/dd/yyy): '),'%m/%d/%Y')
        self.email = input('Email: ')
        self.password = 'blank'
        self.set_password()
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

    def get_username(self,connection): 
        found_user = False
        while found_user != True:
            self.user_name = input('User Name: ')
            get_user = f'''SELECT user_name FROM users where user_name = '{self.user_name}';'''
            cursor = connection.cursor()
            cursor.execute(get_user)
            result = cursor.fetchall()
            #print(result[0][0])           
            if result[0][0] == self.user_name:
                found_user = True
                cursor.close()
            else:
                print(f'No user name like "{self.user_name}"" in the system. Please try again.\n')
                cursor.close()
    
    def get_password(self,connection):
        equal = False
        while equal != True:    
            self.password = input('Password: ')

            get_password = f'''SELECT passwords FROM users WHERE user_name = '{self.user_name}';'''
              
            cursor = connection.cursor()
            cursor.execute(get_password)
            result = cursor.fetchall()
            cursor.close()
            #print(result[0][0])
            if self.password == result[0][0]:
                equal = True
            else:
                print('The password does not match the username. Please try again.')

    def get_credentials(self,connection):
        get_password = f'''SELECT * FROM users WHERE user_name = '{self.user_name}';'''
        
        cursor = connection.cursor()
        cursor.execute(get_password)
        result = cursor.fetchone()
        cursor.close()
        self.user_id = result[0]
        self.fname = result[1]
        self.mname = result[2]
        self.lname = result[3]
        self.registered = result[4]
        self.last_paid = result[5]
        self.birth_day = result[6]
        self.password = result[7]
        self.user_name = result[8]
        self.email = result[9]

    def sign_in(self,connection):
        self.get_username(connection)
        self.get_password(connection)
        self.get_credentials(connection)
        
    def edit_info(self,connection):
        self.fname = input('Fist Name: ')
        self.mname = input('Middle Name: ')
        self.lname = input('Last Name: ')
        self.birth_day = datetime.datetime.strptime(input('Birthday (mm/dd/yyy): '),'%m/%d/%Y')
        self.email = input('Email: ')
        unique = False
        while unique == False:
            user_name = input('User Name: ')
            if user_name != self.user_name:
                get_usernames = f'''SELECT count(user_name) FROM users where user_name = '{self.user_name}';'''
                cursor = connection.cursor()
                cursor.execute(get_usernames)
                result = cursor.fetchall()
                #print(result[0][0])           
                if result[0][0] > 0:
                    unique = False
                    print('That user name already exists. Please try again.\n')
                    cursor.close()
                else:
                    cursor.close()
                    unique = True
            else:
                unique = True
        insert_query = f'''
        UPDATE users 
        SET `fname` = '{self.fname}',`mname` = '{self.mname}',`lname` ='{self.lname}',
            `birth_day` = '{self.birth_day}', `user_name` = '{self.user_name}',
            `email` = '{self.email}'
        WHERE `user_id` = {self.user_id}
        '''  
        cursor = connection.cursor()
        cursor.execute(insert_query)
        connection.commit()
        print(cursor.rowcount,'Record inserted successfully into Users table')
        cursor.close()

    def change_password(self,connection):
        self.get_password(connection)
        self.set_password()

        insert_query = f'''
        UPDATE users 
        SET `passwords` = '{self.password}''
        WHERE `user_id` = {self.user_id}
        '''  
        cursor = connection.cursor()
        cursor.execute(insert_query)
        connection.commit()
        print(cursor.rowcount,'Record inserted successfully into Users table')
        cursor.close()


    

