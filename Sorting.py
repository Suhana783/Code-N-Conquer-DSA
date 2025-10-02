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
#         if arr[j] < arr[min_index]:
#             min_index = j
#             arr[i], arr[min_index] = arr[min_index], arr[i]
           

# print(arr)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l_half = arr[:mid]
    # print(arr[:mid])
    r_half = arr[mid:]
    # print(arr[mid:])
    l_half = merge_sort(l_half)
    # print(l_half)
    r_half = merge_sort(r_half)
    # print(r_half)
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
    print(new)
    new.extend(right[j:])
    return new


arr = [12,6,7,3,15]
print(merge_sort(arr))