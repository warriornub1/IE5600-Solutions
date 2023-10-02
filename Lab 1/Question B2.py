def main():
    
    # DC to F : (°C × 9/5) + 32 = °F
    # F to DC : (32°F − x) × 5/9 = °C

    
    Degree_C = float(input("Celsius to Fahrenheit, : "))
    print(f"Converted : {(Degree_C * 9/5) + 32}")
    
    Degree_C = float(input("Celsius to Fahrenheit, : "))
    print(f"Converted : {(Degree_C * 9/5) + 32}")
    
    Fahrenheit = float(input("Fahrenheit to Celsius, : "))
    print(f"Converted : {(Fahrenheit - 32) * 5/9}")
    
    Fahrenheit = float(input("Fahrenheit to Celsius, : "))
    print(f"Converted : {(Fahrenheit - 32) * 5/9}")

if __name__ == '__main__':
    main()