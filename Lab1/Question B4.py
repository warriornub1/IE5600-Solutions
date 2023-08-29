def main():
    
    a = "Captain America"
    b = "Thor"
    
    a, b = b, a
    
    print("Value of a : {}".format(a))
    print("Value of b : {}".format(b))
    
    
    # Using complementary arithmetic operations, i.e., + and -, or * and /
    # For integer numbers, we can also use XOR ^ 

    varA = 111
    varB = 888

    varA = varA + varB # varA = 111 + 888
    varB = varA - varB # varB = 999 - 888
    print("varB {}".format(varB) )
    varA = varA - varB # varA = 999 -111
    print("varA {}".format(varA) )

if __name__ == "__main__":
    main()