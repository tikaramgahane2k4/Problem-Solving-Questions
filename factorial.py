"""Factorial of Number"""

def factorial_of_num(num):
    if num == 0 or num == 1:
        return 1
    
    return num * factorial_of_num(num - 1)

print(factorial_of_num(5))


