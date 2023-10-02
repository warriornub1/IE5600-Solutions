def main():
    
    longest = 0
    main_list, return_list = [], []
    while(1):
        sentence = str(input('Enter sentence : (empty space to exit) : '))
        if sentence == " ":
            print("Exiting Loop....")
            break
        else:
            if len(sentence.split()) > longest:
                longest = len(sentence.split())
            main_list.append(sentence.split())

    word_index = 0
    
    print(f"Longest sentence : {longest}")
    while(1):
        line = ""
        for sentence in main_list:
            if word_index < len(sentence):
                line += sentence[word_index]
        return_list.append(line)
        
        word_index += 1
        if longest == word_index:
            break
    print(return_list)
if __name__ == '__main__':
    main()