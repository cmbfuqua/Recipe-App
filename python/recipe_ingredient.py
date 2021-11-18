class Ingredient():
    def __init__(self):
        self.measurement: str
        self.item: str 
        self.quantity: int 
    
    def add_ingredient(self):
        self.item = input('What is the name of the ingredient: ')
        self.measurement = input('What is the unit of measurement: ')
        self.quantity = input('How much is needed: ')

    def put_ingredient(self):
        print('* {}------{}{}'.format(self.item,self.quantity,self.measurement))
