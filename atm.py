class Atm:

    __counter = 1                    # static / class variable
    def __init__(self):
        self.__pin = ''            #' __ 'used for hiding it from the user
        self.__balance = 0
        Atm.__counter = Atm.__counter + 1 
        self.__menu()

    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new)== int:
            Atm.__counter = new
        else:
            print("Invlaid Value")

    def check_pin(self ):
        temp = input("Enter your pin")
        if temp == self.__pin:
            return 1
        else:
            return 0
    def set_pin(self):
        self.__pin = input("Set your pin: ")
        if type(self.__pin)== str:
            print("PIN is set !!!")
        else:
            pritn("Not allowed")

    def deposit(self):
        correct  = self.check_pin()
        amount = int(input("Enter the amount:"))
        if correct:
            self.__balance = self.__balance + amount
        else:
            print("PIN is incorrect ")
    
    def withdraw(self):
        correct  = self.check_pin()
        amount = int(input("Enter the amount:"))
        if correct:
            self.__balance = self.__balance - amount
            print('Operation successful')
        else:
            print("PIN is incorrect ")

    def check_balance(self):
        correct  = self.check_pin()
        if correct:
            print("Your Balance is " , self.__balance)
        else:
            print("PIN is incorrect")

    

    def __menu(self):
        user_input = input('''
            1. Set pin
            2. deposit
            3. withdraw
            4. check balance
            5. exit
        ''')

        if user_input == '1':
            self.set_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.show_balance()
        else:
            print("Thank you")
            

    