# num1 = [10, 2, 3, 10, 5, 3, 2, 1, 2, 10]
# num2 = [10, 3, 5, 1]

"""num in number"""

# def num_in_number(num1, num2):
#     total = {}    
#     output = []
#     for i in range(0, len(num1)):
#         if num1[i] in total:
#             total[num1[i]] += 1
#         else:
#             total[num1[i]] = 1

#     for n in range(0, len(num2)):
#         if num2[n] in total:
#             output.append(f"{num2[n]} : {total[num2[n]]}")
        
#         else:
#             output.append(f"{num2[n]} : {0}")

#     return output

# print(num_in_number([10, 2, 3, 10, 5, 3, 2, 1, 2, 10], [10, 5, 1, 3, 4]))

"""char in lists"""

# def char_in_lists(list1, list2):
#     result = {}
#     output = []

#     for char in list1:
#         if char in result:
#             result[char] += 1

#         else:
#             result[char] = 1

#     for n in list2:
#         if n in result:
#             output.append(f"{n} : {result[n]}")
#         else:
#             output.append(f"{n}:", 0)

#     return output

# print(char_in_lists(["a", "e", "t", "d", "q", "a", "d", "q", "a"], ["a", "t", "d"]))


