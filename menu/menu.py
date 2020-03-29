from student.student import Student

def read_csv(filename, open_mode):
    counter = 0
    first_name = ""
    last_name = ""
    matriculation_number = ""
    language = ""
    term = ""
    average_grade = "" 
    username = "" 
    state = ""
    street_name = ""
    street_number = ""

    students = []

    try:
        file = open(filename, "r")
        
        for line in file:
            if counter != 0:
                first_name = line.strip().split(";")[0]
                last_name = line.strip().split(";")[1]
                matriculation_number = line.strip().split(";")[2]
                language = line.strip().split(";")[3]
                term = line.strip().split(";")[4]
                average_grade = line.strip().split(";")[5]
                username = line.strip().split(";")[6]
                state = line.strip().split(";")[7]
                street_name = line.strip().split(";")[8]
                street_number = line.strip().split(";")[9]
                students.append((first_name, last_name, matriculation_number, language, term, average_grade, username, state, street_name, street_number))
            counter += 1
            
    except FileNotFoundError:
        print("File not found!")
    
    return students

def main_menue():

    s = Student("","","","","","","","","","")
    student_list = read_csv("/home/yannic/git/student_management_python/data/sample_students.csv", "r")
    
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
            s.print_all_students(student_list)
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