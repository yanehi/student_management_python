class Student():
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def print_student(self):
        print("Firstname: " + self.firstname)
        print("Lastname: " + self.lastname)
    
    def print_all_students(self,students):
        counter = 1
        for student in students:
            firstname, lastname = student
            print("Student Nr.:" + str(counter))
            print("Firstname: " + firstname)
            print("Lastname: " + lastname)
            print("")
            counter += 1


# s = Student("Max","Peters")

# s.print_all_students(students)