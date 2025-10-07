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
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            print(f"Pattern found at index {i}")

# Example
text = "AABAACAADAABAABA"
pattern = "AABA"
naive_search(text, pattern)
