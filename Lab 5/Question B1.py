import mean_calculator as mc

def main():
    
    print('*** Welcome to Mean Calculator ***')

    while True:
        
        choice = input('Do you have a new dataset to process? (Y/N) = ').strip().upper()
        if choice == 'Y':
            numbers = mc.get_numbers()
            
            if len(numbers) > 0:
                print('You have entered = {}'.format(numbers))
                print('Please select the required mean number to compute:\n\tA = Arithmetic Mean\n\tG = Geometric Mean\n\tH = Harmonic Mean\n\tQ = Change New Dataset')
                option = input('> ').strip().upper()
                
                if option == 'A':
                    
                    print('Arithmetic Mean is {:.3f}'.format(mc.calculate_arithmetic_mean(numbers)))
                
                elif option == 'G':
                    
                    print('Geometric Mean is {:.3f}'.format(mc.calculate_geometric_mean(numbers)))
                
                elif option == 'H':
                    
                    print('Harmonic Mean is {:.3f}'.format(mc.calculate_harmonic_mean(numbers)))
                
                elif option == 'Q':
                    
                    break;
            
        else:
            break
        print('Exiting program...')

if __name__ == '__main__':
    main()