# TODO Easy #### Function to demo how recursion works ###
def reverse(lst):
    if(len(lst)==1):
        print(lst[0])
    else:
        reverse(lst[1:])
        print(lst[0])
# TEST
# reverse([0,1,2,3,4])

def reverse_num(num, rev=0):
    if(num < 10):
        return(rev*10+num)
    else:
        quo = int(num/10)
        rem = num%10
        return(reverse_num(quo, rev*10+rem))
#TEST
print(reverse_num(123))

def recur(n):
    if(n==0):
        print("\tBase case reached at %s" % n)
    else:
        print("first %s **" % n)
        recur(n-1)
        print("second %s" % n) #Note: everything after recursive call stored in stack and popped LIFO after base case has been run
    print("----- END OF %s (%s) FUNC ----- \n" % ('RECUR', n))  #Note: stored in stack with perv line and popped LIFO after base case has been run

#TEST
# recur(4)

# TODO Easy: #### Function to sum all digits of number recursively ###

def digits_sum(n):
    assert int(n)==n and n>=0, "input positive integer"

    if(n==0):
        return 0
    else:
        return ((n%10) + digits_sum(int(n/10)))

#TEST:
# print("Sum = %s" % digits_sum(912))
# print("Sum = %s" % digits_sum(9.1))
# print("Sum = %s" % digits_sum(-910))


# TODO Easy: #### Function to calc power of a number ###
def num_pow(n, p):
    assert n<0 and int(n) == n, "Positive integers only"
    if (n==1):#base case
        return 0
    else:
        return (1 + num_pow(int(n/p), p))

#TEST:
# print(num_pow(16,2))
# print(num_pow(-16,2))
# print(num_pow(7.6,2))

# TODO Medium: #### Function to calc HCF(highest common factor) of a pair of numbers ###

def hcf(a,b):
    #base case:
    if(b==0): #if any num is 1, HCF has been found
        return 1
    else:
        q = int(a/b)
        r = int(a%b)
        print("a= %s, b= %s, div = %s, mod = %s \n" % (a,b,q,r))
        return q * hcf(b, r)

# print(hcf(48, 18))

# TODO Medium: #### Function to convert Decimal to Binary ###

def decimal_to_binary(n):
    if(n==0 or n==1):
        return n
    else:
        quo = int(n/2)
        rem = n%2
        return (rem + decimal_to_binary(quo)*10)

print(decimal_to_binary(5))


# #### Russian Doll recursive function ###
#
# def openRussianDoll(doll):
#     if doll == 1:
#         print("All dolls are opened")
#     else:
#         openRussianDoll(doll-1)
#
#
# openRussianDoll(4)
#
#
# # def recursionMethod(parameters):
# #     if  exit from condition satisfied:
# #         return some value
# #     else:
# #         recursionMethod(modified parameters)
#
#
# def firstMethod():
#     secondMethod()
#     print("I am the first Method")
#
# def secondMethod():
#     thirdMethod()
#     print("I am the second Method")
#
# def thirdMethod():
#     fourthMethod()
#     print("I am the third Method")
#
# def fourthMethod():
#     print("I am the fourth Method")
#
#
# firstMethod()
#
#
# def recursiveMethod(n):
#     if n<1:
#         print("n is less than 1")
#     else:
#         recursiveMethod(n-1)
#         print(n)
#
# recursiveMethod(4)
#  ## Recursion vs Iterarion###
#
# def powerOfTwo(n):
#     if n == 0:
#          return 1
#     else:
#         power = powerOfTwo(n-1)
#         return power * 2
#
# print(powerOfTwo(3))
#
# def powerOfTwoIt(n):
#     i = 0
#     power = 1
#     while i < n:
#         power = power * 2
#         i = i + 1
#     return power
#
#
# print(powerOfTwoIt(4))
#
#  ## Factorial###
#
#
# def factorial(n):
#     assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
#     if n in [0,1]:
#         return 1
#     else:
#         return n * factorial(n-1)


 ## Fibonacci###

def fibonacci(n):
    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer.'
    if n in [0,1]:
        print(n)
        return n
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(4))
