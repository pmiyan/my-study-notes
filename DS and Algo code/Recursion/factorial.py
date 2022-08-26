def factorial(n): #f(n) = n * f(n-1)
    assert n>=0 and int(n)==n, 'The Number must be a positive integer only'
    if(n<=1):
        return 1
    return(n* factorial(n-1))



# print(factorial(5))
# print(factorial(-5))
# print(factorial(0.5))

################################################################

def fib(n):
    if(n in [0,1]):
        return n
    else:
        print()
        return fib(n-1) + fib(n-2)

print(fib(6))