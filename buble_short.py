""" Bubble Short """

# nums = [4, 1, 5, 8, 3, 6, 7]

# for i in range(len(nums)-2, -1, -1):

#     for j in range(0, i+1):

#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]

# print(nums)

""" Recursion """

def bubble_short(nums):
    n = len(nums)

    for i in range(n - 2, -1, -1):
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums
print(bubble_short([1, 3, 2, 5, 4, 9, 7, 8]))