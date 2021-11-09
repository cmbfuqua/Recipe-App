from recipe import Recipe
class Recipe_Book():
    def __init__(self):
        self.name: str
        self.owner: str 
        self.creation: str 
        
    def add_recipe(recipes):
        recipe = Recipe()
        recipe.name = input('What is the name of the recipe: ')
        num_ingredients = int(input('How many ingredients are there? '))
        for num in range(num_ingredients):
            print('\n-------------------------------------------\n')
            recipe.add_ingredient()
            
        print('\n-------------\n')
        recipe.add_instructions()
        recipes.append(recipe)
        print()

    def edit_recipes(recipes):
        option = input('Which recipe would you like to edit? ')
        how = ''
        while how.lower() != 'quit':
            how = input('What do you want to change?(name, ingredient, instructions, quit): ')
            for recipe in recipes:
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
