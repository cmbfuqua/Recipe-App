from book import Recipe_Book
from user import User
def put_menu():
    print('Please select a number:')
    print('1: Enter a new recipe')
    print('2: Edit a recipe')
    print('3: Delete a recipe')
    print('4: View your recipes')
    print('5: Quit')


def main():
    recipe = Recipe_Book()
    user = User()
    print('Hello, welcome to your families home recipe app\n')
    print('How may I help?\n')

    

    option = 0
    while option != 5:
        put_menu()

        option = int(input('What would you like to do? '))

        if option == 1:
            recipe.add_recipe()

        if option == 2:
            recipe.edit_recipes()

        if option == 3:
            recipe.delete_recipe()
        if option == 4: 
            recipe.view_recipes()

if __name__ == '__main__':
    main()