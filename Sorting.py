# 1.insertion_sort 

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         for j in range(i-1, -1, -1): 
#             if arr[j] > key:
#                 arr[j+1] = arr[j]
#             else:
#                 arr[j+1] = key
#                 break
#         else: 
#             arr[0] = key
#     return arr

# arr = [2, 8, 5, 1, 9]
# print(insertion_sort(arr))
            


# 2.second way of insertion_sort 

# def insertion_sort(arr):
#  for i in range(1,len(arr)):
#     key = arr[i]
#     j = i-1
#     while j >= 0 and arr[j] > key:
#       arr[j+1] = arr[j]
#       j -= 1

#     arr[j+1] = key 
#  return arr 

# arr = [8, 3, 5, 2]
# print(insertion_sort(arr))

# 3.selection_sort 

# arr = [5,3,8,4,2]
# n = len(arr)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1,n):
#         arr[j] < arr[min_index]
#         min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]

# print(arr)


