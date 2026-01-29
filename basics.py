"""Count Digits 
"""
# n = 2345123
# count = 0

# while n > 0:
#     res = n % 10
#     n = n // 10
#     count += 1
# print(count)

"""String Reverse"""

# def String_Reverse(string):
#     rev = string[::-1]
#     return(rev)
# print(String_Reverse("pawan"))

"""Reverse number"""

# def reverese_number(num):
#     reverese = 0
#     while num > 0:
#         l_num = num % 10
#         reverese = reverese * 10 + l_num
#         num = num // 10
#     return reverese
# print(reverese_number(1239))

"""Palindrom Number"""

# def Palindrom_Number(num):
#     n = num
#     rev = 0

#     while num != 0:
#         l_num = num % 10
#         rev = rev * 10 + l_num
#         num = num // 10

#     if (rev == n):
#         return ("This is Palindrom Number")
#     else:
#         return ("This is not Palindrom Number")
    
# print(Palindrom_Number(1134))

"""String Palindrom"""

# def StringPalindrom(string):
#     reverese_str = string[::-1]

#     if string == reverese_str:
#         return f"{string}, is palindrom"
    
#     else:
#         return f"{string}, is not palindrom"

# print(StringPalindrom(str("sumit")))

"""Armstrong Number"""

# def Arm_Number(num):
#     n = num
#     digits = len(str(n))
#     arm_num = 0

#     while num > 0:
#         l_dig = num % 10
#         arm_num += l_dig ** digits
#         num = num // 10

#     print(f"The number is :", arm_num)
#     if n == arm_num:
#         return ("This is Armstrong Number")
#     else:
#         return ("This is not Armstrong Number")
    
# print(Arm_Number(370))
    

"""Factors of Number 01"""

# def Factors_of_number(num):
#     fact = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             fact.append(i)
        
#     return fact

# print(Factors_of_number(19))


"""Factors of Number 02"""

# def Factors_of_number(num):
#     fact = []
#     for i in range(1, (num // 2) + 1):
#         if num % i == 0:
#             fact.append(i)

#     fact.append(num)

#     return fact

# print(Factors_of_number(30))

