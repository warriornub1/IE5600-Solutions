def main():
    student = [ {"Name" : "Naruto", "Age": 14, "Gender" : "Male", "Phone" : 999}, 
               {"Name" : "Sakura", "Age": 14, "Gender" : "Female", "Phone" : 888}, 
               {"Name" : "Sakuke", "Age": 16, "Gender" : "Male", "Phone" : 777},
               {"Name" : "Kakashi", "Age": 14, "Gender" : "Male", "Phone" : 666}, 
              {"Name" : "Itachi", "Age": 17, "Gender" : "Male", "Phone" : 555} ]
    while(1):
        try:
            choice = int(input("Enter choice : \n\
         1: Enter new student data \n \
        2: Query the age of a student \n \
        3: Count the number of students of each age \n \
        4: To exit\n"))
    
            if choice == 1:
                name = str(input("Enter name : ")).strip()
                age = int(input("Enter age : ")).strip()
                gender = int(input("Enter gender : ")).strip().upper
                phone = int(input("Enter phone : ")).strip()
                student.append({"Name" : name, "Age": age, "Gender" : gender, "Phone" : phone})
                
                
                    
            elif choice == 2:
                print("Query the name student(s)")
                name  = str(input("Enter name : "))
                for record in student:
                    if name == record["Name"]:
                        print(record["Name"])
                
                    
            elif choice == 3:
                
                male_age_set = set()
                male_age_list = list()
                female_age_set = set()
                female_age_list = list()
                
                for person in student:
                    if person["Gender"] == "Male":
                        male_age_set.add(person["Age"])
                        male_age_list.append(person["Age"])
                    else:
                        female_age_set.add(person["Age"])
                        female_age_list.append(person["Age"])
                
                print('Gender\tAge\tCount\n Female-----------------')
                for age in female_age_set:
                    num_of_age = female_age_list.count(age)
                    print(f"{age}   {num_of_age}")
                
                for age in male_age_list:
                    num_of_age = male_age_list.count(age)
                    print(f"{age}   {num_of_age}")
                    
            elif choice == 4:
                print("Exiting.........")
                break
            print("------------------------------------")
        except ValueError:
            print("Please enter a valid integer number")
if __name__ == '__main__':
    main()