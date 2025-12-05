# 1. Print all subarrays of the array

# nums = [1, 2, 3]
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         print(nums[i : j+1])
        

# 2.find sum of all subarrays

# nums = [1, 2, 3]
# sum = 0
# for i in range(len(nums)):
#     total = 0
#     for j in range(i,len(nums)):
#         subarray = nums[i:j+1]
#         total += nums[j]
#         sum += total
#         print("Sum of subarray", nums[i:j+1], "=", total)
# print(sum)


# 3. length of all subarrays 

# nums = [1,2,3]
# for i in range(len(nums)):
#     length = 0
#     for j in range(i,len(nums)):
#         length = j-i+1
#         subarray = nums[i: j+1]
#         print(subarray,length)
