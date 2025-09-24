# selection_sort 

# arr = [5,3,8,4,2]
# n = len(arr)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1,n):
#         arr[j] < arr[min_index]
#         min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]

# print(arr)


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





