class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0

        self.menu()

    def check_pin(self ):
        temp = input("Enter your pin")
        if temp == self.pin:
            return 1
        else:
            return 0
    def set_pin(self):
        self.pin = input("Set your pin: ")
        print("PIN is set !!!")

    def deposit(self):
        correct  = self.check_pin()
        amount = int(input("Enter the amount:"))
        if correct:
            self.balance = self.balance + amount
        else:
            print("PIN is incorrect ")
    
    def withdraw(self):
        correct  = self.check_pin()
        amount = int(input("Enter the amount:"))
        if correct:
            self.balance = self.balance - amount
            print('Operation successful')
        else:
            print("PIN is incorrect ")

    def check_balance(self):
        correct  = self.check_pin()
        if correct:
            print("Your Balance is " , self.balance)
        else:
            print("PIN is incorrect")

    

    def menu(self):
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
            

    