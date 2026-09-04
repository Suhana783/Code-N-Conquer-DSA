# Traversing an Array 

# 1. Print all elements 

# arr = [2,4,6,2,3,4]
# for i in range(len(arr)):
#     print(arr[i])

# 2. find sum of array 

# arr = [2,5,3,6]
# sum = 0
# for i in range(len(arr)):
#     sum = arr[i] + sum
# print(sum)
       
# 3. Find average

# arr = [3,2,6,7,2]

# total = 0
# for i in range (len(arr)):
#     total = arr[i] + total 
# avarage = total // len(arr)
# print(avarage)

# 4. find maximum/minimum 

# arr = [3,4,2,5,6,7,8]
# max = 0

# for i in range(len(arr)):
#     if arr[i] > max:
#         max = arr[i]
# print(max)

# 5. find the minimum number 
# arr = [-2,3,4,8]
# min = 0
# for i in range(len(arr)):
#     if arr[i] < min:
#         min = arr[i]
# print(min)


# 6. Count even/odd numbers

# arr = [3,4,2,4,6,7,8,9]
# odd = 0
# even = 0
# for i in range (len(arr)):
#     if arr[i] % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even, odd)

# 7.Count positive/negative numbers

# arr=[-2,3,0,8,-4,9,-6]
# positive = 0
# negative = 0
# for i in range(len(arr)):
#     if 0 > arr[i]:
#         negative += 1
#     else:
#         positive += 1
# print(positive, negative)

# Searching in Arrays 

# 1. Find if element exists
# def linearSearch (arr, target):
#     for i in range (len(arr)):
#         if arr[i] == target:
#             return "found", arr[i]
# arr = [2,4,8,4,5]
# target = 4
# print(linearSearch(arr, target))


#2. Find index of target
# def linearSearch (arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
    
# arr = [6,45,0,4,2,11,1]
# target = 11
# print(linearSearch(arr, target))


# 3. Count occurrences of a number
# def findOccurences(arr, num):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] == num:
#             count += 1
#     return count

# arr = [2,3,2,5,78,6,2]
# num = 2
# print(findOccurences(arr, num))


# Array Updating / Manipulation
# 1. Reverse an array

# arr = [2,3,4,5,6,7]
# l = []
# for i in range(len(arr)-1,-1,-1):
#     l.append(arr[i])
# print(l)

# 2. Copy one array into another

# arr = [2,3,4,5,6,7]
# nums = []
# for i in range(len(arr)):
#     nums.append(arr[i])
# print(nums)

# 3. Given an arr rotate the array to the right by k steps.

# arr = [1,5,2,8,2,9]
# output = [8,2,9,1,5,2]

# k = 3
# for i in range(k):
#     key = arr[-1]
#     for j in range(len(arr)-1,0,-1):
#         arr[j] = arr[j-1]

#     arr[0] = key
# print(arr)



# 4. You are given an array/list of size N. Swap every pair of adjacent elements,
# i.e., swap the elements at indices 0 and 1, 2 and 3, 4 and 5, and so on. Modify
# the given array in place without creating or returning a new array.

# N = 6
# arr = [9, 3, 6, 12, 4, 32]
# Output: [3, 9, 12, 6, 32, 4]

# for i in range(0,N-1,2):
#     arr[i], arr[i+1] = arr[i+1], arr[i]

# print(arr)


# a = float('-inf')
# print(a)


# Day 17/08/2026
# find where ticket escalation is triggered mean E and E appeared simultaneously in the array.

# ticket = ["O", "R", "E", "O", "E", "E", "R"]
# # output = "Alert triggered at index 5"

# for i in range(len(ticket)-1):
#     if ticket[i] == "E":
#         if ticket[i+1] == "E":
#             print("Alert triggered at index", i+1)
#             break
# else:
#     print("No alert triggered")

# # 2.
# nums = [100,105,95,130,90,110]
# max_drop = 0
# drop = 0
# index1 = 0
# index2 = 0

# for i in range (len(nums)-1):
#     if nums[i] > nums[i+1]:
#         drop = nums[i] - nums[i+1]
#         if drop > max_drop:
#             max_drop = drop
#             index1 = i 
#             index2 = i+1
# print(index1, index2)
# print(max_drop)


# 3. Print max work done by HR with there name without using any built in methods.
# Work = [
#     [8,8,0,8,8,0,0],
#     [8,8,8,8,8,8,0],
#     [0,8,8,0,8,0,0]
# ]


# A_total = 0 
# B_total = 0
# C_total = 0

# first = Work[0]
# second = Work[1]
# third = Work[2]

# max_work = 0


# for i in range(len(first)):
#     A_total = A_total + first[i]

# for j in range(len(second)):
#     B_total = B_total + second[j]

# for k in range(len(third)):
#     C_total = C_total + third[k]



# if A_total > B_total and A_total > C_total:
#     max_work = A_total
# elif B_total > A_total and B_total > C_total:
#     max_work = B_total
# else:
#     max_work = C_total


# if max_work == A_total:
#     print("A:", A_total)
# elif max_work == B_total:
#     print("B:", B_total)
# else:   
#     print("C:", C_total)




# Day - 18/08/2026

# fares = [180, 140, 155, 170, 190, 130, 160, 180, 158, 168]
# # Threshold: 150
# surge_pricing = []
# count = 0

# for i in range(len(fares)):
#     if fares[i] > 150:
#         count = count + 1
        
#     else:
#         surge_pricing = surge_pricing + [count]
#         count = 0
# surge_pricing = surge_pricing + [count]

# max_val = surge_pricing[0]

# for i in range(1,len(surge_pricing)):
#     if surge_pricing[i] > max_val:
#         max_val = surge_pricing[i]
# print(max_val)

# restaurant =  ["Veg", "Veg", "NonVeg", "NonVeg", "NonVeg", "Veg", "NonVeg", "NonVeg"]
# veg_count = 0
# nonVeg_count = 0
# veg_max = []
# nonVeg_max = []
# finalVeg = 0
# finalNon = 0


# for i in range(len(restaurant)):
#     if restaurant[i] == "Veg":
#         veg_count = veg_count + 1
#     else:
#         veg_max = veg_max + [veg_count]
#         veg_count = 0

#     if  restaurant[i] == "NonVeg":
#         nonVeg_count = nonVeg_count + 1
#     else:
#         nonVeg_max = nonVeg_max + [nonVeg_count]
#         nonVeg_count = 0
# veg_max = veg_max + [veg_count]
# nonVeg_max = nonVeg_max + [nonVeg_count]

# finalVeg = max(veg_max)
# finalNon = max(nonVeg_max)

# if finalVeg > finalNon:
#     print("longest streak Veg : ", finalVeg)

# else:
#     print("longest streak Non-Veg : ", finalNon)

    
# studentA = ["A", "B", "C", "C", "D", "A", "B", "D", "C", "A"]
# studentB = ["D", "B", "C", "C", "D", "A", "B", "C", "C", "A"]
# count = 0
# startIndex = 0
# endIndex = 0

# i = 0
# j = 0

# while i <= len(studentA) and j <= len(studentB):
#         if studentA[i] == studentB[j]:
#             count = count + 1
#             if count >= 4:
#                 startIndex = i
#                 endIndex = j
#                 i += 1
#                 j += 1
#         else:
#              count = 0
#              i += 1
#              j += 1

# print(startIndex, endIndex)

