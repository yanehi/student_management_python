class Student():
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def print_student(self):
        print("Firstname: " + self.firstname)
        print("Lastname: " + self.lastname)