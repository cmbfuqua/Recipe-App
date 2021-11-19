from user_user import User
import mysql.connector
from mysql.connector import Error
def put_reicpe_menu():
    print('Please select a number:')
    print('1: Enter a new recipe')
    print('2: Edit a recipe')
    print('3: Delete a recipe')
    print('4: View your recipes')
    print('5: Go back')

def put_user_menue():
    print('Please select a number:')
    print('1: Edit User Info')
    print('2: Edit password')
    print('3: Go back')

def put_main_menu():
    print('Please select a number')
    print('1: Group')
    print('2: User')
    print('3: Recipes')


def main():
    ##################################################
    # Connect to Database
    ##################################################
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

    except Error as e:
        print("Error while connecting to MySQL", e)
    ####################################################
    # Begin program
    ####################################################
    print('\n\nHello, welcome to your families home recipe app\n')
    choice = int(input('Would you like to 1: sign up or 2: sign in? '))
    if choice == 1:
        user = User()
        user.sign_up(connection)
    elif choice == 2:
        valid_login = False
        user = User()
        while valid_login == False:
            valid_login = user.sign_in(connection)
        print('VALID LOGIN')
    else:
        print('invalid option')


    ####################################################
    # Legacy code
    ####################################################
    #option = 0
    #while option != 5:
    #    put_menu()

    #    option = int(input('What would you like to do? '))

#        if option == 1:
 #           recipe.add_recipe()

  #      if option == 2:
   #         recipe.edit_recipes()

    #    if option == 3:
     #       recipe.delete_recipe()
      #  if option == 4: 
       #     recipe.view_recipes()
    ################################################
    # Disconnect from database
    ################################################
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

if __name__ == '__main__':
    main()