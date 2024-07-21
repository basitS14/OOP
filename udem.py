class User:

    def login(self):
        print("Login")
    def registaration(self):
        print("Registration")
    
class Student(User):
    
    def enroll(self):
        print("Enroll")

    def courses(self):
        print("couses")

class instructor(User):
    def batches(self):
        print("batches")