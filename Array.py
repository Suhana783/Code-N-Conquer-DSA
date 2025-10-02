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

# 3.write a python function that takes a list of numbers and returns a new list with each number squared, 
#    using a loop and finds its time complexity
# def squared_num(list):
#     new_list = []
#     for i in range(len(list)):
#         new_list.append(list[i]*list[i])
#     return new_list

# list = [2,4,3,6,7,1]
# print(squared_num(list))


# 4.Write a programme to find the factorial of a number using loop 

# num = int(input("Enter any number:"))
# product = 1
# for i in range(1,num+1):
#     product = product * i
# print(product)

# 5.write a function that accepts a list and returns the sum of 
#   even numbers in the list and calculate its time complexity

def prime_num(list):
    sum = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            sum += list[i]
    return sum

list = [2,4,1,3,5,7]
print(prime_num(list))