# -*- coding: utf-8 -*-
"""
Spyder Editor

• Input – Asks the user to input a word of at most 5 alphabets.
• Process – Check whether the word is a palindrome.
• Output – Print out a message to inform the user whether the word is a palindrome.

"""

def main():
    
    
    word = str(input("Enter word: "))
    if len(word) > 5:
        print("Sorry, Please enter word <5.\n")
        #raise Exception("Sorry, Please enter word <5.\n")
    else:
        word = word.lower()
        word = word.strip()
        palindrome = word[::-1]
        if word == palindrome:
            print("It is a palindrome")
        else:
            print("It is not a palindrome. Please try again")
        
        #To make it faster
        print(fasterCheck(word))
        
def fasterCheck(word):
    pt_front = 0
    pt_back = len(word) - 1
    while(pt_front < pt_back):
        if(word[pt_front] != word[pt_back]):
            return "It is not a palindrome. Please try again"
        else:
            pt_front += 1
            pt_back -= 1
    return "It is a palindrome"
            
    '''
    
    word = str(input("Enter word: "))
    word = word.lower()
    palindrome = word[::-1]
    
    if word == palindrome:
        print("It is a palindrome")
    else:
        print("It is not a palindrome. Please try again")

    
    '''
if __name__ == '__main__':
    main()