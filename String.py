#1.String Traversal 
# name = "Python"
# for ch in name:
#     print(ch)

# for i in range(len(name)):
#     print(i,":",name[i])

#2.Extracting substring from string 
# text = "Programming"
# print(text[3:-1])
# print(text[0:5])

# 3.Pattern Matching / Searching in Strings 
#  (i)Using in Operator
# text = "I Love Programming"
# print("Love" in text)
# print("python" in text)

# (ii)Using find() Method
# text = "Programming in python is fun"
# print(text.find("fun"))
# print(text.find("play"))


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



# 1. Longest Common Subsequence 
# def lcs_recursive(s1, s2, i, j):
#     # Base case
#     if i == 0 or j == 0:
#         return 0
    
#     # If last characters match
#     if s1[i-1] == s2[j-1]:
#         return 1 + lcs_recursive(s1, s2, i-1, j-1)
    
#     # If last characters don’t match
#     else:
#         return max(lcs_recursive(s1, s2, i-1, j), 
#                    lcs_recursive(s1, s2, i, j-1))

# # Example
# s1 = "ABCDEF"
# s2 = "AEBDF"
# print("LCS length:", lcs_recursive(s1, s2, len(s1), len(s2)))


# Naive Pattern Matching (Easy code)
# def naive_search(text, pattern):
#     n = len(text)
#     m = len(pattern)
    
#     for i in range(n - m + 1):
#         if text[i:i+m] == pattern:
#             print(f"Pattern found at index {i}")

# # Example
# text = "AABAACAADAABAABA"
# pattern = "AABA"
# naive_search(text, pattern)


# Longest Common Prefix

# 1.Find the longest common prefix for the following list of strings:
# ["apple", "app", "april"]

# def longestCommonPrefix(strs):
#     prefix = strs[0]
#     for i in range(1,len(strs)):
#         current_word = strs[i]
#         j = 0

#         while j < len(prefix) and j < len(current_word) and prefix[j] == current_word[j]:
#             j += 1

#         prefix = prefix[:j]
#         if prefix == "":
#             break
#     return prefix

# strs = ["apple", "app", "april"] 
# print(longestCommonPrefix(strs))


# # 2.Find the LCP for:return "" for no match
# # ["dog", "cat", "bird"]

# def longestCommonPrefix(strs):
#     prefix = strs[0]
#     for i in range(1,len(strs)):
#         current_word = strs[i]
#         j = 0

#         while j < len(prefix) and j < len(current_word) and prefix[j] == current_word[j]:
#             j += 1
#         prefix = prefix[:j]
#         if prefix == "":
#          return ""
#     return prefix

# strs = ["dog", "cat", "bird"]
# print(longestCommonPrefix(strs))


# 3.Challenge: large input
#   ["flow", "flower", "flight", "flourish", "flip"]

# def longestCommonPrefix(words):
#     prefix = words[0]
#     for i in range(1,len(words)):
#         current_word = words[i]
#         j = 0

#         while j < len(prefix) and j < len(current_word) and prefix[j] == current_word[j]:
#             j += 1
#         prefix = prefix[:j]
#     return prefix 

# words = ["flow", "flower", "flight", "flourish", "flop"]
# print(longestCommonPrefix(words))


# 4.Find the longest prefix of the given string which is also a suffix.
# Input :- "abcdabcabcd"
# Output:- "abcd"

# s = "abcdabcabcd"
# longest = ""
# for i in range(1,len(s)):
#     prefix = s[:i]
#     suffix = s[-i:]
#     if prefix == suffix:
#         longest = prefix
# print(longest)


# 6. Reverse a String
# Problem: Given a string s, return the reversed string.
# Example: "hello" → "olleh"

# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("hello"))            


# Given a string s, return the index of the first character that does not 
# repeat.If no such character exists, return -1.

# s = "nanno"
# found = False

# for i in range(len(s)):
#     count = 0
#     for j in range(len(s)):
#         if s[i] == s[j]:
#             count += 1
#     if count == 1:
#         print(i)
#         found = True
#         break

# if not found:
#     print(-1)

# Count occurrences of a character
# Input: string = "banana", char = "a"
# Output: 3

# string = "banana"
# char = "a"
# count = 0
# for i in range(len(string)):
#     if string[i] == char:
#         count += 1
# print(count)




# Write a function that reverses a string. The input string is given as an array of characters s.
# s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"] 

# left = 0
# right = len(s)-1

# while left < right:
#     s[left], s[right] = s[right], s[left]
#     left += 1
#     right -= 1
# print(s)


# Q1: Write a program to find and list all the duplicate characters present in a given string.

# s = "banana"
# duplicate_val = []


# s = s.lower()
# for i in range(len(s)):
#     j = i+1

#     while j < len(s):
#         if s[i] == s[j] and s[i] not in duplicate_val:
#             duplicate_val.append(s[i])
#         j += 1
# print(duplicate_val)


# Given a string s which may contain lowercase and uppercase characters. The task is 
# to remove all duplicate characters from the string and find the resultant string. 
# The order of remaining characters in the output should be same as in the original string.
           
# s = "geEksforGEeks"
# i = 0
# j = len(s)-1
# duplicate_val = []

# s = s.lower()
# while i <= j and j < len(s):
#     if s[i] == s[j]:
#         duplicate_val.append(s[i])
#         j -= 1
#     i += 1
    
# print(duplicate_val)

    

            
        

