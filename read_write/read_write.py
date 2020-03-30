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
            
        file.close()
        
    except FileNotFoundError:
        print("File not found!")
    
    return students


def write_csv(students, filename, mode):
      
    student_list = students
      
    try:
        file = open(filename, mode)
        file.write("first_name;last_name;matriculation_number;language;term;average_grade;username;state;street_name;street_number" + "\n")
        for student in student_list:
            file.write(student[0] + ";" + student[1]+ ";" + student[2]+ ";" + student[3]+ ";" + student[4]+ ";" + student[5]+ ";" + student[6]+ ";" + student[7]+ ";" + student[8]+ ";" + student[9] + "\n")
            
        file.close()
        
    except FileNotFoundError:
        print("File not found!!")