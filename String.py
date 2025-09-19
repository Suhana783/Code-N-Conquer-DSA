# 1.Reverse a String
# Given a string, reverse it without using built-in reverse functions.

# word = "suhana"
# reverse_word = ""
# for i in range(len(word)):
#     reverse_word = word[i] + reverse_word
# print(reverse_word)


# 2.Check Palindrome
# Determine if a given string is a palindrome (reads the same forwards and backwards).


# def palindrome_checker(word):
#     i = 0
#     j = len(word)-1
#     while i <= j and j < len(word):
#         if word[i] == word[j]:
#             i += 1
#             j -= 1
#         else:
#             return "not a palindrome"
#     return "is palindrome"

# word = "rabcr"
# print(palindrome_checker(word))


# // 3. Find out non-repeating character in an array of integers 

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


