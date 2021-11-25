from user_user import User
import mysql.connector
from mysql.connector import Error

def put_main_menu():
    print('Please select a number:')
    print('1: Group')
    print('2: User')
    print('3: Recipes')
    print('4: Quit')

def put_recipe_menu():
    print('Please select a number:')
    print('1: Enter a new recipe')
    print('2: Edit a recipe')
    print('3: Delete a recipe')
    print('4: View your recipes')
    print('5: Go back')

def put_group_menu():
    print('Please select a number:')
    print('1: Create group')
    print('2: Edit group info')
    print('3: Add admin')
    print('4: Remove admin')
    print('5: Add member')
    print('6: Remove member')

def put_user_menu():
    print('Please select a number:')
    print('1: Edit User Info')
    print('2: Change Password')
    print('3: Go back')



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
    print('\nHello, welcome to your families home recipe app\n')
    choice = int(input('Would you like to 1: sign up or 2: sign in? '))
    if choice == 1:
        user = User()
        user.sign_up(connection)
        print('\nThank you for signing up, now please sign in.')
        user.sign_in(connection)
    elif choice == 2:
        user = User()
        user.sign_in(connection)
    else:
        print('invalid option')
    ####################################################
    # Basic Menu logic
    ####################################################
    main_option = 0
    print()
    while main_option != 4:
        put_main_menu()
        main_option = int(input('Number: '))
        ########################################
        # Go into the group menu
        ########################################
        if main_option == 1:
            put_group_menu()
        #     second_option = 0
        #     while second_option != 6:
        #         second_option = int(input('Number: '))
        #         if second_option == 1:

        #         elif second_option == 2:
                
        #         elif second_option == 3:

        #         elif second_option == 4:

        #         elif second_option == 5:
        ########################################
        # Go into the user menu
        ########################################
        elif main_option == 2:
            second_option = 0
            while second_option != 3:
                put_user_menu()
                second_option = int(input('Number: '))
                if second_option == 1:
                    user.edit_info(connection)
                elif second_option == 2:
                    user.change_password(connection)
        # ########################################
        # # Go into the recipe menu
        # ########################################
        elif main_option == 3:
            put_recipe_menu()
            second_option = 0
            while second_option != 5:
                second_option = int(input('Number: '))
                if second_option == 1:
                    user.recipe_book.add_recipe(connection)
                elif second_option == 2:
                    user.recipe_book.edit_recipes()
                elif second_option == 3:
                    user.recipe_book.delete_recipe()
                elif second_option == 4:
                    user.recipe_book.view_recipes()
        elif main_option == 4:
            continue
        else:
            print('Invalid number, try again.')


    ################################################
    # Disconnect from database
    ################################################
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

if __name__ == '__main__':
    main()