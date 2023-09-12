def main():
    
    NRIC = str(input("Input NRIC : "))
    CheckValid(NRIC)

def CheckValid(NRIC):
    
    if len(NRIC) == 9:
        if NRIC[0] in ('S' or 'T' or 'F' or 'G'):
            
            weighted_sum = (int(NRIC[1]) * 2) + (int(NRIC[2]) * 7) + (int(NRIC[3]) * 6) + (int(NRIC[4]) * 5) + (int(NRIC[5]) * 4) + (int(NRIC[6]) * 3) + (int(NRIC[7]) * 2)
            
            if  NRIC[0] == ("T" or "G"):
                weighted_sum += 4  = # weighted_sum = 4 + weighted_sum
            
            mod_11 = weighted_sum % 11
            
            if NRIC[0] == 'S' or NRIC[0] == 'T':
    
                if mod_11 == 0:
                    check_alphabet = 'J'
                elif mod_11 == 1:
                    check_alphabet = 'Z'
                elif mod_11 == 2:
                    check_alphabet = 'I'
                elif mod_11 == 3:
                    check_alphabet = 'H'
                elif mod_11 == 4:
                    check_alphabet = 'G'
                elif mod_11 == 5:
                    check_alphabet = 'F'
                elif mod_11 == 6:
                    check_alphabet = 'E'
                elif mod_11 == 7:
                    check_alphabet = 'D'
                elif mod_11 == 8:
                    check_alphabet = 'C'
                elif mod_11 == 9:
                    check_alphabet = 'B'
                elif mod_11 == 10:
                    check_alphabet = 'A'
                
            else:
                
                if mod_11 == 0:
                    check_alphabet = 'X'
                elif mod_11 == 1:
                    check_alphabet = 'W'
                elif mod_11 == 2:
                    check_alphabet = 'U'
                elif mod_11 == 3:
                    check_alphabet = 'T'
                elif mod_11 == 4:
                    check_alphabet = 'R'
                elif mod_11 == 5:
                    check_alphabet = 'Q'
                elif mod_11 == 6:
                    check_alphabet = 'P'
                elif mod_11 == 7:
                    check_alphabet = 'N'
                elif mod_11 == 8:
                    check_alphabet = 'M'
                elif mod_11 == 9:
                    check_alphabet = 'L'
                elif mod_11 == 10:
                    check_alphabet = 'K'
                    
            if NRIC[8] == check_alphabet:
                print(f'{NRIC} is a valid NRIC')
            else:
                print(f'{NRIC} is not a valid NRIC')
            
            
        else:
            print('The first character of an identity card number must be the alphabet S, T, F or G')
    
    else:
        print("ID Card must be 9 Numbers")

if __name__ == '__main__':
    main()