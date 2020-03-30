from student.student import Student
from read_write import *

def delete_student_menu(student_list, matr_number, found_index):
    delete_student = input('Delete student?(y/n) -> ')
            
    if delete_student == "y":
        student_list.pop(found_index)
        print("Student deleted!")
    else:
        print("Student not deleted!")
        main_menue()

def main_menue():

    s = Student("","","","","","","","","","")
    filename = "/home/yannic/git/student_management_python/data/sample_students.csv"
    student_list = read_write.read_csv(filename, "r")
    
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
            
            new_student = s.add_student()
            student_list.append(new_student)
            
        elif menue_point == "3":
            print("3) Remove student.")
            matr_number = input('Matriculation Number: ')
            found_index = s.search_student(student_list, matr_number)
            
            delete_student_menu(student_list, matr_number, found_index)
        
        elif menue_point == "4":
            print("4) Edit student")
        
        elif menue_point == "0":
            print("0) Save and Quite")
            read_write.write_csv(student_list,filename,"w")
        
        else:
            print("Invalid input!!")