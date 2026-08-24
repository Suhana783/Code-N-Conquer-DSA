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
            


# # 2.second way of insertion_sort 

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

# # 3.selection_sort 

# arr = [5,3,8,4,19,0]
# n = len(arr)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1,n):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
           

# print(arr)

# # 4. Merge sort 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l_half = arr[:mid]
    r_half = arr[mid:]
    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)
    return merge(l_half,r_half)

def merge(left,right):
    new = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    new.extend(left[i:])                                                                                                                
    new.extend(right[j:])
    return new


arr = [12,6,7,3,15]
print(merge_sort(arr))



# # 5. Quick sort 

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2] 

#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort(left) + middle + quick_sort(right)
# arr = [8,7,3,1,0,9]
# print(quick_sort(arr))


# 6 Bubble sort 

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j] , arr[j+1] = arr[j+1], arr[j]
#     return arr
    
# arr = [12,16,14,9]
# print(bubble_sort(arr))


# 8. Fair Candy Swap

# Alice and Bob have a different total number of candies. You are given two integer arrays
# aliceSizes and bobSizes where aliceSizes[i] is the number of candies of the ith box of candy
# that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.

# Since they are friends, they would like to exchange one candy box each so that after the exchange,
# they both have the same total amount of candy. The total amount of candy a person has is the sum
# of the number of candies in each box they have.

# Return an integer array answer where answer[0] is the number of candies in the box that Alice must
# exchange, and answer[1] is the number of candies in the box that Bob must exchange. If there
# are multiple answers, you may return any one of them. It is guaranteed that at least one answer
#  exists.

 

# Example 1:

# Input: aliceSizes = [1,1], bobSizes = [2,2]
# Output: [1,2]
# Example 2:

# Input: aliceSizes = [1,2], bobSizes = [2,3]
# Output: [1,2]
# Example 3:

# Input: aliceSizes = [2], bobSizes = [1,3]
# Output: [2,3]