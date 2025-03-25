filename = "students.txt"

case

    
target = input("Enter a name: \n")


try:
    
    with open(filename, 'r') as file:
        found = False
        for lines in file:
            if target == lines.strip().split(',') [0]:
                print(f"{target} scored {lines.strip().split(',') [1]}")
                found = True
                break
        if found == False:
            print("Student not found!")
except FileNotFoundError:
    print("Error: The file does not exist.")
            
    
    

