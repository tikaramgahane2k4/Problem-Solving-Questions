"""String is Palindrome or Not by method"""

# name = "pap"

# rev = name[::-1]

# if name == rev:
#     print('is palindrome')

# else:
#     print('not palindrome')

"""  By loop """

name = 'pawa'
# sto = []
# re = []
# for i in name:
#     sto.append(i)

# for j in range(1, len(sto)+ 1):
#     re.append(sto[-j])

# if sto == re:
#     print('is palindrom')

# else:
#     print('not palindrom')


"""By recursion """

# def isPalindrom(name, left, right):
#     if left >= right:
#         return True
    
#     if name[left] != name[right]:
#         return False
    
#     return isPalindrom(name, left + 1, right - 1)

# print(isPalindrom('pawap', 0, len(name) - 1))