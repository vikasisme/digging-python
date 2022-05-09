# Recursion
def fib(n):
    if n in {1, 0}:
        return n
    return fib(n-1) + fib(n-2)

# Space complexity optimized
def fibonacci(n): 
    a = 0
    b = 1 
    
    if n < 0:
        return -1
    
    if n in {0, 1}:
        return n

    for _ in range(1,n):
        c = a + b
        a = b
        b = c
    
    return b
    
if __name__ == "__main__":
    sum = fib(9)
    sum1 = fibonacci(9)
    print(f"Fibonacci at nth postion: {sum} - {sum1}")