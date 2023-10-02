def main():
    student = {"Naruto" : 15, "Sakura" : 14, "Sasuke" : 13, "Kakashi" : 23, "Itachi" : 17}
    while(1):
        try:
            choice = int(input("Enter choice : \n\
         1: Enter new student data \n \
        2: Query the age of a student \n \
        3: Compute the average age of the student \n \
        4: Count the number of students of each age\n \
        5: To exit\n"))
    
            if choice == 1:
                name = str(input("Enter name : "))
                age = int(input("Enter age : "))
                
                if name in student.keys():
                    print("Name already exist")
                else:
                    student[name] = age
                    
            elif choice == 2:
                print("Query the age of a student")
                name  = str(input("Enter name : "))
                if name not in student.keys():
                    print("Name in ninja book for record")
                else:
                    print(f"Ninja name : {student[name]}")
                    
            elif choice == 3:
                
                print("Calculating average age of student...")
                total_age = 0
                for name in student.values():
                    total_age += student[name]
                average_age = total_age / len(student)
                print("Average age of ninaj in the village is {:.1f}".format(average_age))
                
            elif choice == 4:
                age = student.values()
                list_age = list(age)
                list_age.sort()
                unique_age = set(list_age)
                
                print('Age\tCount\n---\t-----\n', end='')
                for uq in unique_age:
                    count = list_age.count(uq)
                    print(uq, count)
                    
            elif choice == 5:
                print("Exiting.........")
                break
            print("------------------------------------")
        except ValueError:
            print("Please enter a valid integer number")
if __name__ == '__main__':
    main()