# empty database
# database = list([])

# sample database
database =  [{'name': 'Alice Lee', 'age': 25, 'gender': 'F', 'telephone': '91234567'}, {'name': 'Bob Tan', 'age': 24, 'gender': 'M', 'telephone': '90000001'}, {'name': 'Charles Lim', 'age': 23, 'gender': 'M', 'telephone': '90000002'}, {'name': 'Deborah Goh', 'age': 22, 'gender': 'F', 'telephone': '90000003'}, {'name': 'Edward Chia', 'age': 21, 'gender': 'M', 'telephone': '90000004'}, {'name': 'Farah Koh', 'age': 22, 'gender': 'F', 'telephone': '90000005'}, {'name': 'George Tan', 'age': 19, 'gender': 'M', 'telephone': '90000006'}, {'name': 'Hubert Wong', 'age': 24, 'gender': 'M', 'telephone': '90000007'}, {'name': 'Issac Newton', 'age': 22, 'gender': 'M', 'telephone': '90000008'}, {'name': 'Juliet Robert', 'age': 24, 'gender': 'F', 'telephone': '90000009'}, {'name': 'Kim Lee', 'age': 22, 'gender': 'M', 'telephone': '90000010'}, {'name': 'Bob Tan', 'age': 21, 'gender': 'M', 'telephone': '98881111'}, {'name': 'Bob Tan', 'age': 19, 'gender': 'M', 'telephone': '98881112'}, {'name': 'Charles Lim', 'age': 25, 'gender': 'M', 'telephone': '98881113'}, {'name': 'Susan Ang', 'age': 30, 'gender': 'F', 'telephone': '98881114'}, {'name': 'Jackie Chan', 'age': 19, 'gender': 'M', 'telephone': '98881115'}] 



def main():
    
    while True:
        
        print('*** Welcome to Students\' Age Database ***')
        # print('\n', database,'\n')
        print('A: Input New Student')
        print('B: Query Student\'s Information')              
        print('C: Crosstabulation of Students\' Gender and Age')
        print('D: Exit')
        
        option = input('> ').strip().upper()
        
        if option == 'A':
        
            name = input('Enter student\'s name = ').strip()
            age = int(input('Enter student\'s age = ').strip())
            gender = input('Enter student\'s gender (M: Male and F: Female) = ').strip().upper
            telephone = input('Enter student\'s telephone number = ').strip()
            
            database.append({'name':name, 'age':age, 'gender':gender(), 'telephone':telephone})
            
        elif option == 'B':
            
            name = input('Enter student\'s name = ').strip()
            
            results = []
            
            for student in database:
                
                if student['name'] == name:
                    
                    results.append(student)
            
            if len(results) > 0:
            
                print('There are {} matching students'.format(len(results)))
                
                for student in results:
                    
                    print('{:<20s}\t{:>3s}\t{}\t{}'.format(student['name'], str(student['age']), student['gender'], student['telephone']))
                
            else:
                
                print('Student does not exist')                
        
        elif option == 'C':            
            
            genders = list([])
            
            for student in database:
                
                genders.append(student['gender'])
                        
            genders = set(genders)            
            genders = list(genders)            
            genders.sort()
            
            crosstab = dict({})
            
            for gender in genders:
                
                ages = list([])
                
                for student in database:
                    
                    if student['gender'] == gender:
                    
                        ages.append(student['age'])
                            
                ages = set(ages)            
                ages = list(ages)            
                ages.sort()
                                
                crosstab[gender] = dict({})
                
                for age in ages:
                    
                    count = 0
                    
                    for student in database:
                    
                        if student['gender'] == gender and student['age'] == age:
                            
                            count += 1
                        
                    crosstab[gender][age] = count
                    
            print('Gender\tAge\tCount\n-----------------')
            
            for outerkey,outervalue in crosstab.items():
                
                is_first_line = True
                
                for innerkey,innervalue in outervalue.items():
                    
                    if is_first_line:
                        
                        print('{:<7s}\t{}\t{}'.format(outerkey, innerkey, innervalue))
                        is_first_line = False
                        
                    else:
                        
                        print('{:<7s}\t{}\t{}'.format(' ', innerkey, innervalue))
        
        else:
            
            break                
        
    print('Goodbye :)')



if __name__ == '__main__':
    
    main()
