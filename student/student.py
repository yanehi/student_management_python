class Student():
    
    def __init__(self, first_name, last_name, matriculation_number, language, term, average_grade, username, state, street_name, street_number):  
        self.first_name = first_name
        self.last_name = last_name
        self.matriculation_number = matriculation_number
        self.language = language
        self.term = term
        self.average_grade = average_grade
        self.username = username
        self.state = state
        self.street_name = street_name
        self.street_number = street_number
        
    def print_student(self, student, counter):
        first_name, last_name, matriculation_number, language, term, average_grade, username, state, street_name, street_number = student
        print("Student Nr: " + str(counter))
        print("Firstname: " + first_name)
        print("Lastname: " + last_name)
        print("Matriculation Number: " + matriculation_number)
        print("Language: " + language)
        print("Term: " + term)
        print("Average Grade: " + average_grade)
        print("Username: " + username)
        print("State: " + state)
        print("Street: " + street_name + " Nr. " + street_number)
        print("")
    
    def print_all_students(self,students):
        counter = 1
        for student in students:
            self.print_student(student, counter)
            counter += 1
    
    def add_student(self):
        first_name = input('Firstname: ')
        last_name = input('Lastname: ')
        matriculation_number = input('Matriculation Number: ')
        language = input('Language: ')
        term = input('Term: ')
        average_grade = input('Average Grade: ')
        username = input('Username: ')
        state = input('State: ')
        street_name = input('Street: ')
        street_number = input('Nr: ')
        
        new_student = (first_name, last_name, matriculation_number, language, term, average_grade, username, state, street_name, street_number)

        return new_student

# s = Student("","","","","","","","","","")
# s.print_all_students(students)