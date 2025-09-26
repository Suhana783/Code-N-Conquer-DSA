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


# Longest Common Subsequence
