# empty database
# database = dict({})

# sample database
database = {'alice': 25, 'bob': 24, 'charles': 23, 'deborah': 22, 'edward': 21, 'farah': 22, 'george': 19, 'hubert': 24, 'issac':22}



def main():
    
    while True:
        
        print('*** Welcome to Students\' Age Database ***')
        # print('\n', database,'\n')
        print('A: Input New Student')
        print('B: Query Student\'s Age')              
        print('C: Compute Average Age')
        print('D: Count Students by Age')
        print('E: Exit')
        
        option = input('> ').strip().upper()
        
        if option == 'A':
        
            name = input('Enter student\'s name = ').strip()
            age = int(input('Enter student\'s age = ').strip())
            
            if name in database.keys():
                
                print('Student already exists')
                
            else:
                
                database[name] = age
                print('Student added successfully')
            
        elif option == 'B':
            
            name = input('Enter student\'s name = ').strip()
            age = database.get(name)
            
            if age == None:
                
                print('Student does not exist')
                
            else:
                
                print('Student\'s age is {}'.format(age))
        
        elif option == 'C':
            
            ages = database.values()
            total_age = 0
            
            for age in ages:
                
                total_age += age
                
            average_age = total_age / len(ages)
            
            print('Average age of all students is {:.1f}'.format(average_age))
        
        elif option == 'D':
            
            ages = database.values()
            ages = list(ages)
            ages.sort()
            unique_ages = set(ages)
            
            print('Age\tCount\n---\t-----\n', end='')
            
            for age in unique_ages:
                
                print('{:3d}\t{:3d}'.format(age, ages.count(age)))
        
        else:
            
            break                
        
    print('Goodbye :)')



if __name__ == '__main__':
    
    main()
