# "Find the smallest element in an array. Input: [4, 2, 9, 1, 7]

# arr = [-5, 2, 9, 1, 7]
# min = arr[0]
# for i in range(len(arr)-1):
#      if arr[i] < min:
#         min = arr[i]    
# print(min)

# "Check if two strings are anagrams (same letters, different order).Input: ""listen"", ""silent""
# Output: True"
# "Move all zeros to the end of the array while keeping order.Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]"

# nums = [0, 1, 0, 3, 12]
# i = 0   
# for j in range(len(nums)):  
#     if nums[j] != 0:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
# print(nums)

# "Use Linear Search to find the number 7 in the array:
# At which index is it found?"

# arr = [2, 4, 7, 1, 9]
# target = 7
# for i in range(len(arr)):
#    if arr[i] == target:
#     print("target found",i)



# "Use Selection Sort to sort the array:

# arr = [29, 10, 14, 37, 13]
# n = len(arr)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1,n):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
# print(arr)


# Given an array, count how many numbers are even.
# nums = [2, 5, 6, 8, 11, 14], Output:4

# nums = [2, 5, 6, 8, 11, 14]
# count = 0
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         count += 1
# print(count)



# Count Increasing Adjacent Pairs Count how many times:
# nums[i] < nums[i+1]
# Example: [1, 3, 2, 4, 6] → pairs: (1,3), (2,4), (4,6) → 3

# nums = [1, 3, 2, 4, 6]
# count = 0
# pair = []
# for i in range(len(nums)-1):
#     if nums[i] < nums[i+1]:
#         pair.append((nums[i], nums[i+1]))
#         count += 1
            
# print(count, pair)


# Longest Increasing Continuous Subarray
# Find the length of the longest strictly increasing continuous subarray.
# [1, 2, 3, 2, 3, 4, 5]
# Longest increasing continuous subarray is [2, 3, 4, 5] → length = 4

# nums = [1, 2, 3, 2, 3, 4, 5]
# max_l = 0
# for i in range(len(nums)):
#     length = 0
#     for j in range(i,len(nums)):
#         length = j-i+1
#         if max_l < length:
#             max_l = length
#             subarray = nums[i: j+1]
        
# print(max_l)






# Count How Many Subarrays Have Sum < 5
# nums = [1,2,3]
# sum = 0
# count = 0
# for i in range(len(nums)):
#     total = 0
#     for j in range(i,len(nums)):
#         total += nums[j]
#         if total < 5:
#             count += 1
#         sum += total
#         subarray = nums[i : j+1]
#         print(subarray,total)
# print(count)



# Count subarrays where every number is strictly increasing.
# nums = [1,2,1]
# count = 0
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         subarray = nums[i: j+1]
#         is_inc = True

#         for k in range(len(subarray)-1):
#             if subarray[k] >= subarray[k+1]:
#                 is_inc = False
#                 break
#         if is_inc:
#             count += 1
# print(count)


# Count Subarrays with Positive Sum
# Count all subarrays whose sum is greater than 0.
# Example: [1, -2, 3]
# Possible positive subarrays: [1], [3], [1,-2,3] → 3
    
# arr = [1,-2,3]
# count = 0
# for i in range(len(arr)):
#     total = 0
#     sum = 0
#     for j in range(i,len(arr)):
#         total += arr[j]
#         sum = total
#         subarray = arr[i:j+1]
#         print(subarray, sum)
#         if sum > 0:
#             count += 1
# print(count)

