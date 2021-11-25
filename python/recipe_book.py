from recipe_recipe import Recipe
class Recipe_Book():
    def __init__(self):
        self.name: str
        self.owner: str 
        self.creation: str 
        self.recipes = []
        
    def add_recipe(self,connection):
        recipe = Recipe()
        recipe.set_name()
        num_ingredients = int(input('How many ingredients are there? '))
        for num in range(num_ingredients):
            print('\n-------------------------------------------\n')
            recipe.add_ingredient()
            
        print('\n-------------\n')
        recipe.add_instructions()
        self.recipes.append(recipe)
        print()

    def edit_recipes(self):
        option = input('Which recipe would you like to edit? ')
        how = ''
        while how.lower() != 'quit':
            how = input('What do you want to change?(name, ingredient, instructions, quit): ')
            for recipe in self.recipes:
                if recipe.name == option:
                    if how.lower() == 'name':
                        recipe.name = input('What is the new name: ')
                    if how.lower() == 'ingredient':
                        action = input('Would you like to edit or delete this ingredient?(remove or edit) ')
                        if how.lower() == 'remove':
                            recipe.remove_ingredient()
                        if how.lower() == 'edit':
                            recipe.edit_ingredient()
                    if how.lower() == 'instructions':
                        recipe.instruction = input('What are the new instructions? ')
    def delete_recipe(self):
        option = input('Which recipe would you like to delete? ')
        for recipe in self.recipes:
            if option.lower() == recipe.name.lower():
                self.recipes.remove(recipe)

    def view_recipes(self):
        for recipe in self.recipes:
            print(recipe.view_recipe())
            print('\n\n')
