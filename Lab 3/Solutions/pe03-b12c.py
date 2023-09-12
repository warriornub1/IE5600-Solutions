import time
import sys



def get_expected_stopping_time(n):
    
    stopping_time_interval = {
        n < 10**1: 19,
        10**1 <= n < 10**2: 118,
        10**2 <= n < 10**3: 178,
        10**3 <= n < 10**4: 261,
        10**4 <= n < 10**5: 350,
        10**5 <= n < 10**6: 524,
        10**6 <= n < 10**7: 685,
        10**7 <= n < 10**8: 949,
        10**8 <= n < 10**9: 986,
        10**9 <= n < 10**10: 1132,
        10**10 <= n < 10**11: 1228,
        10**11 <= n < 10**12: 1348
    }
    
    return stopping_time_interval[True]



def collatzSequence(n, expected_stopping_time, steps=0):
    
    steps += 1
    
    if steps > expected_stopping_time:
        
        print('****** EUREKA ******: We found a positive integer that defies the Collatz Conjecture!!!')
        return
    
    if n > 0:
        
        print(n, end='. In {} steps\n'.format(steps)) if n == 1 else print(n, end=', ')
    
        if n == 1:
            
            return
            
        else:
            
            collatzSequence(n // 2, expected_stopping_time, steps) if n % 2 == 0 else collatzSequence(n * 3 + 1, expected_stopping_time, steps)



def main():
    
    try:
    
        original_stdout = sys.stdout    
        f = open('collatz.txt', 'w')
        sys.stdout = f
        
        num = 1
    
        while True:
            
            current_expected_stopping_time = get_expected_stopping_time(num)
            
            print('Collatz 3n+1 sequence for {} expected to stop in {} steps: '.format(num, current_expected_stopping_time), end='')
            collatzSequence(num, current_expected_stopping_time)
            num += 1
            
            # time.sleep(0.1)
    
    except KeyboardInterrupt:
        
        if original_stdout != None:
            
            sys.stdout = original_stdout



if __name__ == '__main__':
    
    main()
