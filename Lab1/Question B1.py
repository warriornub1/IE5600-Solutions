def main():
    # DECLARE CONSTANT
    # 1 SGD -> 1.35 USD
    # 1 USD -> 1/1.35
    EXCHANGE_RATE = 1.3500
    
    
    SGDtoUSD = float(input("USD to SGD, : "))
    print(f"Total Converted : {SGDtoUSD * EXCHANGE_RATE}")
    
    SGDtoUSD = float(input("USD to SGD, : "))
    print(f"Total Converted : {SGDtoUSD * EXCHANGE_RATE}")
    
    
    
    USDtoSGD = float(input("SGD to USD, : "))
    print(f"Total Converted : {USDtoSGD / EXCHANGE_RATE}")
    
    USDtoSGD = float(input("SGD to USD, : "))
    print(f"Total Converted : {USDtoSGD / EXCHANGE_RATE}")
    
if __name__ == '__main__':
    main()
    