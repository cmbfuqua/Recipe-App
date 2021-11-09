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
    recipes = []
    recipe = Recipe_Book()
    user = User()
    print('Hello, welcome to your families home recipe app\n')
    print('How may I help?\n')

    

    option = 0
    while option != 5:
        put_menu()

        option = int(input('What would you like to do? '))

        if option == 1:
            add_recipe(recipes)

        if option == 2:
            edit_recipes(recipes)

        if option == 3:
            delete_recipe(recipes)
        if option == 4: 
            view_recipes(recipes)

if __name__ == '__main__':
    main()