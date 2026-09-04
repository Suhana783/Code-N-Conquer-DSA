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

# nums = [1, 1, 5]
# k = 6
# sum = 0
# count = 0

# for i in range(len(nums)):
#     sum = 0
#     for j in range(i, len(nums)):
#         sum += nums[j]
#         if sum == k:
#             count += 1

# print(count)



# Find minimum and maximum elements from a given array 
# arr = [1, 4, 3, 8, 6]
# min_val = arr[0]
# max_val = arr[0]

# for i in range(len(arr)):
#     if arr[i] > max_val:
#         max_val = arr[i]
#     elif arr[i] < min_val:
#         min_val = arr[i]

# print(max_val, min_val)


# Question 2: Find the "Kth" maximum element in an unsorted array.

# arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
# k = 4

# n = len(arr)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1], arr[j]


# kth_max = arr[n - k]
# print(kth_max)



# Reverse an array 

# arr = [2,3,4]
# i = 0
# j = len(arr)-1
# while i <= j and j < len(arr):
#     arr[i], arr[j] = arr[j], arr[i]
#     i += 1
#     j -= 1
# print(arr)
            

# Given an unsorted array having both negative and positive integers. Place all 
# negative elements at the end of the array without changing the order of positive elements 
# and negative elements.

# def moveNegativesToEnd(arr):
#     n = len(arr)
#     temp = []

#     for i in range(n):
#      if arr[i] >= 0:
#         temp.append(arr[i])

#     for i in range(n):
#       if arr[i] < 0:
#         temp.append(arr[i])

#     for i in range(n):
#      arr[i] = temp[i]


# arr = [1, -1, 3, 2, -7, -5, 11, 6]
# print(moveNegativesToEnd(arr))
# print(arr)


# You are given an array arr[] of size n - 1 that contains distinct integers in 
# the range from 1 to n (inclusive). This array represents a permutation of the 
# integers from 1 to n with one element missing. Your task is to identify and return
# the missing element.

# arr = [1, 2, 3, 5]
# n = len(arr) + 1
    
# expected_sum = n * (n+1) // 2
# actual_sum = sum(arr)

# print (expected_sum - actual_sum)


# Find the 3rd minimum element in the array.
# arr = [12, 4, 7, 19, 3, 8, 15]
# k = 3

# n = len(arr)
# for i in range (n-1):
#     for j in range(n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# kth_min = arr[k-1]

# print(kth_min)


# Find the second smallest element in the array.
# arr = [7, 2, 9, 1, 5, 3]

# min_val = arr[0]
# second_min = 0

# for i in range(len(arr)):
#     if arr[i] < min_val:
#         min_val = arr[i]
#         second_min = min_val
#     elif second_min < min_val:
#         second_min = min_val
# print(second_min)
    

# arr = ["-2","9","5","2","5"]
# found = "no"

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] == arr[j]:
#          found = "yes"
#          print("duplicate number:", arr[i])

# if found == "no":
#    print("no duplicate found")


# 1. reverse the number 

# digit = "12365"
# reverse = ""

# for i in range(len(digit)-1,-1,-1):
#    reverse = reverse + digit[i]
# print(reverse)



# 2. fibonacci 

# n = 5

# f = 0
# s = 1

# for i in range(n):
#     print(f)

#     next = f + s
#     f = s
#     s = next

# 3. find min and max  

# arr = [2,1,4,6,4]

# max_val = 0
# min_val = 0
# for i in range(len(arr)):
#     if arr[i] > max_val:
#         max_val = arr[i]
#     if arr[i] < min_val:
#         min_val = arr[i]
# print(max_val, min_val)



# find all factors of a number even it should work for negative numbers

# N = 10

# if N > 0:
#     for i in range(1, N + 1):
#         if N % i == 0:
#             print(i)

# else:
#     for i in range(-1, N-1,-1):
#         if N % i == 0:
#             print(i)

# print all prime numbers between 1 to 30 (sieve algorithm)

# N = 20

# prime = [True] * (N + 1)

# prime[0] = False
# prime[1] = False

# for i in range(2, N + 1):

#     if prime[i]:

#         for j in range(i * 2, N + 1, i):
#             prime[j] = False

# for i in range(2, N + 1):
#     if prime[i]:
#         print(i)



# - Classify a triangle as scalene, isoceles, equilateral or right angled on basis of its sides  and dont use logical operators

# a = 4
# b = 3
# c = 3

# if a == b:
#     if b == c:
#      print("Equilateral triangle")

# elif a == b:
#    print("Isosceles triangle")
# elif b == c:
#    print("Isoceles triangle")

# elif a*a + b*b == c * c:
#    print("right-angeled triangle")

# else:
#    print("scalene triangle")


      
# find 2nd max of 5 numbers ( take 5 input) 

# 29 july 

# n = int(input())

# if n % 5 == 0:
#    if n % 11 == 0:
#       print("both")
#    else:
#       print(5)
# elif n % 11 == 0:
#    print(11)

# else:
#    print("none")



# R = int(input())
# C = int(input())
# T = int(input())

# if R > 50:
#    if C > 0.7:
#       if T > 5600:
#        print(10)
#       else:
#         print(9)
#    else:
#      print(7)


# elif C > 0.7:
#   if T > 5600:
#     print(8)

# else:
#   print(0)



# classify a rhombus, rectangle, parallelogram, square and irregular quadrilateral on 4 sides
# AB, BC, CD, DA and 1 internal angle. Dont use any logical operator


# AB = int(input())
# BC = int(input())
# CD = int(input())
# DA = int(input())
# angle = int(input())

# if angle == 90:
#     if AB == BC:
#         if BC == CD:
#             if CD == DA:
#                 print("Square")
#     else:
#         if AB == CD:
#             if BC == DA:
#                 print("Rectangle")
#             else:
#                 print("Irregular Quadrilateral")
#         else:
#             print("Irregular Quadrilateral")
# else:
#     if AB == BC:
#         if BC == CD:
#             if CD == DA:
#                 print("Rhombus")
#     else:
#         if AB == CD:
#             if BC == DA:
#                 print("Parallelogram")
#             else:
#                 print("Irregular Quadrilateral")
#         else:
#             print("Irregular Quadrilateral")


# N = 5
# tasks = [55, 60, 44, 30,52]
# count = 0
# newTask = []


# for i in range(len(tasks)):
#     if tasks[i] >= 50:
#         if tasks[i] % 2 == 0:
#             count += 1
#             newTask = newTask + [tasks[i]]

# print("count:" ,count, newTask)

# # find max and second max from newTask array 
# i = 0
# max_val = newTask[0]
# second_max = newTask[0] 
# while i < len(newTask):
#     if newTask[i] > max_val:
#         second_max = max_val
#         max_val = newTask[i]
#     elif newTask[i] > second_max and newTask[i] != max_val:
#         second_max = newTask[i]
#     i += 1

# print("max:", max_val, "second_max", second_max)


# runs = [42, 30, 43, 40, 20]

# count = 0
# new = []
# for i in range(len(runs)):
#     if runs[i] >= 40:
#         count += 1
#         new = new + [runs[i]]
# print(count, new)

# max_val = new[0]
# second_max = new[0]

# for i in range(len(new)):
#     if new[i] > max_val:
#         second_max = max_val
#         max_val = new[i]

#     elif new[i] > second_max:
#         if new[i] != max_val:
#             second_max = new[i]
# print(max_val, second_max)

# find star players print the scores of players who scored at least 80%
# of the highest score . 

# new = [42, 43, 40]
# highest = new[0]

# for score in new:
#     if score > highest:
#         highest = score

# t = highest * 80 / 100
# for score in new:
#     if score >= t:
#         print(score)



# A student qualifies if Marks >= 75 , attendance >= 85 and no backlog. count qualified students 

# marks = [80,92,70,88,95,76,60]
# attendance = [90,85,80,95,88,87,92]
# backlog = [0,0,1,0,0,0,0]
# result = []

# for i in range(len(marks)):
#     if marks[i] >= 75:
#         if attendance[i] >= 85:
#             if backlog[i] == 0:
#                 result = result + [marks[i]]


# print("result : ",result) 
# highest = result[0]
# lowest = result[0]
# average = result[0]
# total = 0

# for i in range (len(result)):

#     total = total + result[i]
#     if result[i] > highest:
#         highest = result[i]
   
#     elif result[i] < lowest:
#         lowest = result[i]
# avg = total / len(result)
    
# print("highest :" ,highest)
# print("lowest : ",lowest)
# print("average : ",avg)


# gold = []
# silver = []
# bronze = []

# for i in range(len(result)):
#     if result[i] >= highest-5:
#         gold = gold + [result[i]]
#     elif result[i] >= average:
#         silver = silver + [result[i]]

#     else:
#         bronze = bronze + [result[i]]

# print("gold :", gold, "silver : " , silver, "bronze : ", bronze)


# Day 4/08/2026 

# aptitude = [100,78, 700, 70, 72]
# technical = [95, 82, 90, 75, 80]
# count = 0
# qualified = []

# for i in range (len(aptitude)):
#     if aptitude[i] >= 70:
#         if technical[i] >= 75:
#             if aptitude[i] + technical[i] >= 160:

#                 count += 1
#                 num = 0.4 * aptitude[i] + 0.6 * technical[i] 
#                 qualified = qualified + [num]
# print(qualified, count)


# highest = 0
# second_highest = 0

# for i in range(len(qualified)):
#     if qualified[i] > highest:
#         second_highest = highest
#         highest = qualified[i]
#     elif qualified[i] > second_highest:
#         if qualified[i] != highest:
#          second_highest = qualified[i]
# print("highest :", highest, "second_highest : ", second_highest)


# First sort qualified scores highest to lowest

# for i in range(len(qualified)):
#     for j in range(i + 1, len(qualified)):
#         if qualified[i] < qualified[j]:
#             temp = qualified[i]
#             qualified[i] = qualified[j]
#             qualified[j] = temp


# Find number of candidates in each batch

# total = len(qualified)

# a_count = highest * 80 / 100
# b_count = highest * 50 / 100

# A = []
# B = []
# C = []

# # a = 0
# # b = 0

# for i in range(len(qualified)):

#     if qualified[i] >= a_count:
#         A = A + [qualified[i]]
#         # a = a + 1

#     elif qualified[i] >= b_count:
#         B = B + [qualified[i]]
#         # b = b + 1

#     else:
#         C = C + [qualified[i]]


# print("Batch A:", A)
# print("Batch B:", B)
# print("Batch C:", C)


# Day 7/08/2026

# find the first empty parking slot 
# Each slot contains:
# 0 → Empty
# 1 → Occupied
# Find the index of the first empty parking slot.
# If all slots are occupied, print "Parking Full".
# Input: 1 1 1 0 1 0
# Output: 3

# slots = [1,1,1,0,1,0]
# first_empty_slot = 0
# Parking_Full = True

# for i in range(len(slots)):
#     if slots[i] == 0:
#         first_empty_slot = i
#         Parking_Full = False
#         break
# if Parking_Full == False:
#   print("First empty parking slot index:", first_empty_slot)
# else:
#    print("Parking is full")


# Problem 2: Largest Continuous Empty Area
# Find the longest continuous sequence of empty parking slots.
# Input: 1 0 0 0 1 0 0
# Output: Length = 3

# slots = [0,0,1,0,0,1]
# count = 0
# k = 4
# continue_sequence = 0
# bus_parking = False
# index_value = []
# for i in range(len(slots)):
#     if slots[i] == 0:
#         count += 1
#         index_value = index_value + [i]
#         if count > continue_sequence:
#             continue_sequence = count
#             if continue_sequence == k:
#                 bus_parking = True

#     elif slots[i] == 1:
#             count = 0
# print("count :", continue_sequence)
# if bus_parking == True:
#  print("Bus Parking Yes :", continue_sequence)
# else:
#     print("Can't park the bus")


# if len(index_value) % 2 != 0:
#  mid = len(index_value) // 2
#  print(index_value[mid])
# if len(index_value) % 2 == 0:
#     mid = (len(index_value) // 2) -1
#     print(index_value[mid])
    

# Day - 10/08/2026

# n = int(input())
# if n > 100:
#     print("high")
# elif n < 100:
#     print("low")
# else:
#     print("safe")

# Problem 2: Character Detector
# A system receives a single character.
# Determine whether the character is:
# an uppercase alphabet
# a lowercase alphabet
# a digit
# a special character
# Input: G
# Output: UPPERCASE

# ch = input()

# if ch == ch.int():
#     print("digit")
# elif ch == ch.upper():
#     print("UPPERCASE")
# elif ch == ch.lower():
#     print("lowercase")
# else:
#     print("special character")


# password = input()
# n = len(password)
# if n >= 10:
#     print("Strong")
# elif n >= 6:
#     print("medium")
# else:
#     print("weak")




# Day - 11/08/2026 
# 1.Traffic Jam Detector 🚗
# A road has N checkpoints. At each checkpoint, the number of vehicles is recorded.
# A checkpoint is considered congested if the number of vehicles is greater than both 
# the previous and next checkpoint.
# Find the number of congested checkpoints.
# Input: 10 25 18 30 20 15 28 12
# Output: 3


# arr = [10,25,18,30,20,15,28,12]

# i = 1
# j = i + 1
# count = 0

# while i < len(arr)-1 and j > -1:
#     if arr[i] > arr[i - 1] and arr[i] > arr[j]:
#         count += 1
#     i += 1
#     j += 1

# print("Number of congested checkpoints:", count)

# 2.Power Consumption
# A device records its power consumption every hour.
# Find the longest continuous period during which power consumption keeps increasing.
# Input: 10 15 20 18 22 25 30 17
# Output: 4

# arr = [10, 15, 20, 18, 22, 25, 30, 17]
# i = 0
# j = i+1
# continueIncrement = 1

# while i < j and j < len(arr)-1:
#     if arr[j] > arr[i]:
#         continueIncrement += 1
#     else:
#         continueIncrement = 1

#     i+=1
#     j+=1
# print(continueIncrement)

# 3.Balanced Array ⚖️
# An array is called balanced at index i if the sum of all elements before i
# is equal to the sum of all elements after i.
# Find the first balanced index.
# Input: 1 2 3 6 2 4
# Output: 3


# Day 13/08/2026

# Ques1 Write a Python program that takes a list of integers and prints the sum of
# squares of all even numbers in the list.

# nums =  [1, 2, 3, 4, 5, 6]
# # Output: 56   (2² + 4² + 6² = 4+16+36)

# sum = 0
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         square = nums[i] * nums[i]
#         sum = sum + square
# print(sum)

# Ques2 Write a program to find the second largest number in a list without using
# sort(), sorted(), or max(). Use a loop and conditionals only.

# nums = [10, 5, 20, 8, 20, 15]
# # Output: 15
# max_val = nums[0]
# second_max = nums[0]
# for i in range(len(nums)):
#     if nums[i] > max_val:
#         second_max = max_val
#         max_val = nums[i]
#     elif second_max < nums[i]:
#         if nums[i] != max_val:
#             second_max = nums[i]
# print(second_max)


# Ques3 Given a list of numbers, write a program that removes duplicate elements while
# preserving the original order of first occurrence. Don't use set().
# Output: [4, 5, 6, 7, 8]

nums =  [4, 5, 4, 6, 5, 7, 8, 7]
# result = []

# for i in range(len(nums)):
#     j = i+1
#     while j <= len(nums)-1:
#         if nums[i] == nums[j]:
#             del nums[j]
#         else:
#             j += 1

# print(nums)



# Ques4 Given a list of integers and a target value, write a program to find all unique
# pairs of numbers from the list that add up to the target. Each pair should be printed 
# only once (no repeats, no reversed duplicates like (2,8) and (8,2) both showing).

# nums = [2, 7, 4, 3, 6, 8, 1]
# target = 9
# # Output: (2, 7), (3, 6), (8, 1)


# for i in range (len(nums)):
#     for j in range(i+1,len(nums)-1):
#         if nums[i] + nums[j] == target:
#             print(nums[i], nums[j])
#             del nums[i]
#             del nums[j]

         
            
            
