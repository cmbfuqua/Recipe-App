from book import Recipe_Book

class User():
    def __init__(self):
        self.name: str 
        self.phone: str 
        self.birth_day: str 
        self.country: str
        self.language:str
        self.state: str
        self.privilege = 'user'
    
    def put_info(self):
        print('{} - {} \n{} {} {} {}'.format(self.name, self.phone, self.birth_day, self.country, self.state, self.language))

