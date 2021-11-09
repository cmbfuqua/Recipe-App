from ingredient import Ingredient
class Recipe():
    def __init__(self):
        self.name:str 
        self.ingredients = []
        self.instructions: str 

    def add_ingredient(self):
        ingredient = Ingredient()
        ingredient.add_ingredient()
        self.ingredients.append(ingredient)

    def edit_ingredient(self):
        for ingredient in self.ingredients:
            print(ingredient.item)       
        done = ''
        while done.lower() != 'quit':
            name = input('What is the name of the ingredient: ')
            for ingredient in self.ingredients:
                if ingredient.name.lower() == name.lower():
                    ingredient.measurement = input('What is the new measurement: ')
                    ingredient.quantity = int(input('What is the new quantity: '))
                else:
                    print('Sorry, that is an invalid option. Please enter a valid ingredient name:')
            done = input('Is there another ingredent you would like to edit? ')

    def remove_ingredient(self):
        for ingredient in self.ingredients:
            print(ingredient.name)
        in_list = True
        while in_list:
            name = input('What is the name of the ingredient')
            for ingredient in self.ingredients:
                if ingredient.name.lower() == name.lower():
                    self.ingredients.remove(ingredient)
                    in_list = False
                    print('Removed the recipe :)')
                else:
                    print('Sorry, that is an invalid ingredient.')
    
    def add_instructions(self):
        self.instructions = input('What are the instructions: ')

    def view_recipe(self):
        print('\t\t{}'.format(self.name))
        for ingredient in self.ingredients:
            ingredient.put_ingredient()
        print(self.instructions)
        print('\n\n-------------------------------------')
