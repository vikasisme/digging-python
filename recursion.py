def factorial(n):
    if n < 0: 
        return -1
    
    if n in {0, 1}:
        return 1
    
    return n * factorial(n-1)

def countdown(n):
    print(n)

    if n == 0:
        return 
    
    countdown(n-1)

def factorial_ternary(n):
    return 1 if n in {0, 1} else n * factorial_ternary(n-1) 

if __name__ == "__main__":
    f = factorial_ternary(5)
    print(f"{f}")
    countdown(10)

import ds.stack as Stack