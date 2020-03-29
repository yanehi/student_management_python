from student.student import Student

def main_menue():

    p = Student("peter", "maffay")
    
    students = [
    ("Max", "Meyer1"),
    ("Peter", "Peters2"),
    ("Max", "Meyer3"),
    ("Peter", "Peters4"),
    ("Max", "Meyer5"),
    ("Peter", "Peters6"),
    ]
    
    menue_point = ""

    while(menue_point != "0"):
        print("------Main Menue------")
        print("1) List students.")
        print("2) Add student.")
        print("3) Remove student.")
        print("4) Edit student")
        print("0) Save and Quite")
        
        menue_point = input('Input:')
        
        if menue_point == "1":
            print("---------------------")
            print("1) List students")
            p.print_all_students(students)
            print("---------------------")
        
        elif menue_point == "2":
            print("2) Add student.")
        
        elif menue_point == "3":
            print("3) Remove student.")
        
        elif menue_point == "4":
            print("4) Edit student")
        
        elif menue_point == "0":
            print("0) Save and Quite")
        
        else:
            print("Invalid input!!")