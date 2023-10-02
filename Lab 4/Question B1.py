
def check_palindrome(word):
    start, end = 0, len(word) - 1
    while start < end:
        if word[start] != word[end]:
            return "Not a palindrome"
        start += 1
        end -= 1
    return "Is a palindrome"
    
def main():
    word = str(input("Enter word to check for palindrome : "))
    word = word.lower().replace(" ", "")
    
    new_word = []
    for c in word:
        if c.isalpha():
            new_word.append(c)
    
    print(check_palindrome(new_word))
    

if __name__ == '__main__':
    main()