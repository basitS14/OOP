class Address():

    def __init__(self , state , city , pincode):
        self.state = state
        self.city = city
        self.pincode = pincode

    def edit_address(self , new_state , new_city , new_pincode):
        self.state = new_state
        self.city = new_city
        self.pincode = new_pincode
        

class Cusotmer():

    def __init__(self , name , gender , address):
        self.name  = name
        self.gender = gender 
        self.address = address

    def edit_profile(self , new_name , new_state , new_city , new_pincode):
        self.name = new_name
        self.address.edit_address(new_state , new_city , new_pincode)
        

