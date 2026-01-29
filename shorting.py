"""  Shorting """

# arr = [1, 2, 3, 8, 1, 3, 1, 5, 9]

# for i in range(0, len(arr)):
#     min_ind = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_ind]:
#             min_ind = j

#     arr[i], arr[min_ind] = arr[min_ind], arr[i]

# print(arr)

""" Recursion Shorting"""

def arr_shorting(nums):
    n = len(nums)

    for i in range(0, n):
        min_ind = i
        for j in range(i+1, n):
            if nums[j] < nums[min_ind]:
                min_ind = j
            
        nums[i], nums[min_ind] = nums[min_ind], nums[i]

    return nums
print(arr_shorting([8,3,8,5,1,2,4]))