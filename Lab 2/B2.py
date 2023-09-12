def main():
    
    choice = str(input("Enter choice (C / F): "))
    if choice == 'C' :
        Degree_C = float(input("Celsius to Fahrenheit, : "))
        print(f"Converted : {(Degree_C * 9/5) + 32}")
    elif choice == 'F' :
        Fahrenheit = float(input("Fahrenheit to Celsius, : "))
        print(f"Converted : {(Fahrenheit - 32) * 5/9}")
    else:
        print("Wrong Choice")


if __name__ == '__main__':
    main()