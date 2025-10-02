# 1. Linear Search 

# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return "target found", arr[i]
#     return -1

# arr = [2,9,4,8,5,6,3]
# target = 3
# print(linear_search(arr,target))

# 2. Binary Search 

# def binary_search(arr,target):
#     low = 0
#     high = len(arr)-1
#     while low <= high:
#         mid = (low + high) // 2
#         print(low,high)
#         if arr[mid] == target:
#             return arr[mid]
#         if arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return "doesn't exist"

# arr = [1,2,3,4,5,6,7]
# target = 7
# print(binary_search(arr,target))


