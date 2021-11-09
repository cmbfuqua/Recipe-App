from user import User

class Primary_Account_Holder(User):
    def __init__(self):
        super().__init__()
        self.privilege = 'Owner'
    
    def put_info(self):
        return super().put_info()
