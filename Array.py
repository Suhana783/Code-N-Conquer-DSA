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


