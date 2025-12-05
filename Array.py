# // 1. Find out non-repeating character in an array of integers 

# def non_repeating_character(arr):
#     for i in range(len(arr)):
#         is_unique = True

#         for j in range(len(arr)):
#             if i != j and arr[i] == arr[j]:
#                 is_unique = False
#                 break

#         if is_unique:
#             return arr[i]
        
#     return None

# arr = [10,10,4,5,4]
# print(non_repeating_character(arr))


#2.You have an array of student marks: [85, 42, 73, 91, 58].
# Find the second lowest mark.

# def second_lowest(arr):
#     n = len(arr)

#     for i in range(n-1):
#         min_index = i
#         for j in range(i+1,n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i] , arr[min_index] = arr[min_index] , arr[i]
        
#     return arr, arr[1]

# arr = [85, 42, 73, 91, 58]
# print(second_lowest(arr))


# 3. Median of two sorted array. 
# nums1 = [1,3]
# nums2 = [2]
# median = 0
# nums1.extend(nums2)
# n = len(nums1)
# for i in range(n):
#     for j in range(n-i-1):
#         if nums1[j] > nums1[j+1]:
#             nums1[j],nums1[j+1] = nums1[j+1],nums1[j]
# mid = n // 2
# if n % 2 != 0:
#     median = nums1[mid]
# else:
#     median = (nums1[mid - 1] + nums1[mid]) / 2

# print(median)


# 4.Print all the even numbers from the given array.
# Input:- [1, 4 ,5, 8, 10, 3]
# Output:- [4,8,10]

# arr = [1, 4 ,5, 8, 10, 3]
# even = []
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         even.append(arr[i])

# print(even)


# 5.Find the Majority Element
# Input:-[3, 3, 4, 2, 4, 4, 2, 4, 4]
# Output:- 4

# arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
# count = 0
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i != j and arr[i] == arr[j]:
#             count += 1




# 6. Check if a Number is Prime
# Problem: Given an integer n, determine if it is a prime number.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(7))   


# 7.Problem: Given an array and a target, return the indices of
#   two numbers that add up to the target.

# def two_sum(nums, target):
#     n = nums_len = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []


# 8. Count Numbers in an Array
# Problem: Given an array, count how many elements it has.
# Input: [10, 20, 30, 40]
# Output: 4

# arr = [10, 20, 30, 40]
# count = 0
# for i in range(len(arr)):
#     count += 1
# print(count)


# 9.Sum of All Elements
# Problem: Given an array, return the sum of all numbers.
# Input: [1, 2, 3, 4, 5]
# Output: 15

# nums = [1, 2, 3, 4, 5]
# sum = 0
# for i in range(len(nums)):
#     sum += nums[i]
# print(sum)


# 10.Remove Duplicates From a Sorted Array
# Problem: Given a sorted array, remove duplicates in-place so that
#  each element appears only once, and return the new length.
# Input: [1, 1, 2, 2, 3, 3, 3, 4]
# Output: 4

# nums = [1, 1, 2, 2, 3, 3, 3, 4]
# def removeDuplicates(nums):
#     if not nums:
#         return 0
#     i = 0
#     for j in range(1, len(nums)):
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i] = nums[j]

#     return i + 1  


# Check if Array Contains a Given Element
# Input: [1, 2, 3, 4], x = 3
# Output: True

# nums = [1,2,9,4,6,1,8]
# x = 3
# if x in nums:
#     print("True")
# else:
#     print("False")



# Given an array of integers, sort the array in ascending order using Bubble Sort.
# arr = [5, 2, 9, 1, 5, 6]
# n = len(arr)

# for i in range(n):
#     for j in range(n-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)  
            
# 3. Count even numbers in an array
# Input: [2, 5, 6, 7, 8]

# nums = [2, 5, 6, 7, 8]
# count = 0
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         count += 1
# print(count)

  
# Find the maximum element in an array.Input: [3, 1, 7, 4, 2]
# arr = [3, 1, 7, 4, 9]
# z = max(arr)
# print(z)
    
# Remove duplicates from an array while keeping order.

# nums = [1, 2, 2, 3, 1, 4]
# result = []
# for n in nums:
#     if n not in result:
#         result.append(n)

# print(result)   

# Two Sum Problem 
# Given an array and a target number, find two numbers whose sum equals the target.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# nums = [2,7,11,15]
# target = 15
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#           print(i,j)       



# Q1. Find the Peak Element in an Array
# A peak element is an element that is strictly greater than its neighbors.
# Given an array nums, return any one peak element’s index.
# Input: nums = [1, 3, 5, 4, 2]
# Output: 2   (because nums[2] = 5 is a peak)

# nums = [1, 3, 5, 4, 7]
# i = 1

# while i < len(nums)-1:
#     if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
#         print(nums[i])
#     i += 1


# Q2. Longest Substring Without Repeating Characters
# Given a string s, return the length of the longest substring where no character repeats.
# Input: s = "abcabcbb"
# Output: 3   ("abc")


# Q1. Longest Consecutive Sequence
# Given an unsorted array of integers, return the length of the longest sequence of numbers that appear consecutively (in any order).
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4  
# Explanation: The longest consecutive sequence is [1, 2, 3, 4]

# nums = [100, 4, 200, 1, 3, 2]

# n = len(nums)
# for i in range(n):
#     for j in range(n-i-1):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]

# max_len = 1
# curr_len = 1

# for i in range(1, n):
#     if nums[i] == nums[i-1] + 1:
#         curr_len += 1
#     elif nums[i] == nums[i-1]:
#         continue
#     else:
#         curr_len = 1

#     if curr_len > max_len:
#         max_len = curr_len

# print(max_len)

# Q2. Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals k.
# Input: nums = [1, 1, 1], k = 2
# Output: 2  
# Explanation: Subarrays are [1,1] at indexes (0,1) and (1,2)

nums = [1, 1, 5]
k = 6
sum = 0
count = 0

for i in range(len(nums)):
    sum = 0
    for j in range(i, len(nums)):
        sum += nums[j]
        if sum == k:
            count += 1

print(count)
