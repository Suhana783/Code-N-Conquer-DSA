# 21/08/2026

# Ques1: License Plate Palindrome Checker (Using Loops)
# A license plate is called a palindrome if it reads the same forwards and backwards.
# Write a function to check if a given plate number is a palindrome.

# word =  "RACECAR"
# reverse = ""
# # OUTPUT: True
# word = "DL8CAF9"
# # OUTPUT: False

# for i in range(len(word)-1,-1,-1):
#     reverse = reverse + word[i]
# if word == reverse:
#     print("isPalindrome")
# else:
#     print("not a palindrome")


# Ques2: Chessboard Pattern Printer (Nested Loop) 

# n = 5
# for i in range(n):
#     for j in range(n):
#         if (i + j) % 2 == 0:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()


# Ques3: Movie Ticket Price Calculator, A cinema calculates ticket price using these rules:
# Age below 5 → Base price ₹0 (free)
# Age 5–11 → Base price ₹150
# Age 60 or above → Base price ₹100
# Everyone else → Base price ₹250
# If it's a weekend, add ₹50 to the price
# If the person has a student card AND is between 12–59 years old, subtract ₹50
 
# age = 25
# is_weekend = True
# has_student_card = True
# movie_ticket = 0
# OUTPUT: 250

# age = 25
# is_weekend = True
# has_student_card = True

# if age < 5:
#     movie_ticket = 0

# elif age <= 11:
#     movie_ticket = 150

# elif age >= 60:
#     movie_ticket = 100

# else:
#     movie_ticket = 250

# if is_weekend:
#     movie_ticket = movie_ticket + 50

# if has_student_card and age >= 12 and age <= 59:
#     movie_ticket = movie_ticket - 50

# print(movie_ticket)




# Ques4: Odd-Even Vehicle Rule Checker
# plate = "DL8CAF3342"
# date = 15
# # OUTPUT: Allowed

# for i in range(len(plate)-1,-1,-1):
#         if date % 2 != 0:
#             if int(plate[i]) % 2 != 0:
#                 print("Allowed")
#                 break
#             else:
#                 print("Not Allowed")
#                 break
#         else:
#             print("Not Allowed")
#             break

 
# Day - 24/08/2026
# Q1: Missing Number Detective An array contains numbers from 1 to n, but one number is missing. 
# Find it — without sorting the array.

# arr =   [1, 2, 4, 5, 6, 7, 8]  
# n = 8
# missing_value = 0
# sum = n * (n + 1) // 2
# total = 0
        
# for i in range(len(arr)):
#     total = total + arr[i]
# missing_value = sum - total
# print(missing_value)
    
# 2
# arr = [2, 7, 11, 15, 5, 9] 
# target = 9
# # OUTPUT: [(0, 1)]
# p = ()
# new = []

# for i in range(len(arr)):
#     for j in range(i+1,len(arr)-1):
#         if arr[i] + arr[j] == target:
#             p = (i,j)
#             new = new + [p]
# print(new)


# Q2: Matrix Diagonal Difference Given a square matrix, find the absolute difference between
# the sum of its main diagonal (top-left to bottom-right) and its secondary diagonal 
# (top-right to bottom-left).

# m = [[11, 2, 4],
#        [4, 5, 6],
#        [10, 8, -12]]
# main = 0
# secondary = 0
# difference = 0
# (main diagonal: 11+5-12 = 4 | secondary: 4+5+10 = 19 | |4-19| = 15) 

# for i in range(len(m)):
#     main = main + m[i][i]
#     secondary = secondary + m[i][len(m)-1-i]

# if main > secondary:
#     difference = main - secondary
# else:
#     difference = secondary - main 
# print(difference)

  
# Day 25/08/2026

# sentence = "ThE quick brown fox"
# count = 0
# word = ""


# for i in range(len(sentence)):

#     word = word + sentence[i]
#     if sentence[i] == " ":

#         print(word, count)
#         count = 0
#         word = ""
        
#     else:
#         if sentence[i] in "AEIOUaeiou":
#             count = count + 1
           

# # 2.

# m = [[20, 35, 15], 
#     [40, 35, 30], 
#     [45, 40, 30]]
# total = 0
# p = ()
# new = []

# for i in range(len(m)):
#     for j in range(len(m)):
#         total = total + m[i][j]
#     if total > 100:
#         p =  i + 1 , total - 100
#         new = new + [p]
#     total = 0
# print(new)

# 3.

# sentence = "Priyanka Chopra Jonas"
# word = ""
# count = 0
# sentence = sentence.lower()

# for i in range(len(sentence)):

#     word = word + sentence[i]
#     if sentence[i] == " ":
#        if count >= 8:
#         print(word, count)
#         word =""
#         count = 0
     
#     else:

#         if sentence[i] in "abcdefghijklmnopqrstuvwxyz":
#             count = count + 1




# Day 27/08/2026 
# Q1:  Insurance Premium Calculator 🏥
# Calculate insurance premium: base rate depends on age (<25→₹3000, 25-44→₹5000, 45-59→₹8000, 60+→₹12000). 
# Add 30% if the person has a pre-existing disease, and another 20% if they smoke (both can apply together). 

# INPUT: age=65, has_disease=True, smoker=True 
# OUTPUT: 18720.0 

# age = 65
# smoke = True
# existing_disease = True
# premium = 0

# if age < 25:
#   premium = 3000

# elif age <= 25 and age >= 44:
#   premium = 5000

# elif age >= 45 and age <= 59:
#   premium = 8000

# else:
#   premium = 12000

# if existing_disease == True and smoke == True:
#   add = (premium * 30) // 100
#   premium = premium + add
#   add = (premium * 20) // 100
#   premium = premium + add

# elif existing_disease == True:
#   add = (premium * 30) // 100
#   premium = premium + add

# elif smoke == True:
#   add = (premium * 20) // 100
#   premium = premium + add

# else:
#   premium

# print(premium)
  

# # 2. 

# arr =  [0, 1, 0, 3, 12]
# # Output: [1, 3, 12, 0, 0]

# count = 0
# new = []

# for i in range(len(arr)):
#     if arr[i] == 0:
#         count = count + 1
#     elif arr[i] != 0:
#         new = new + [arr[i]]

# for j in range(count):
#     new = new + [0]
# print(new)

    
# # 3. Compress a string by counting consecutive repeated characters: "aaabbc" → "a3b2c1". 

# word =  "aaabbc"
# # Output: "a3b2c1"

# count = 1
# new = ""
# for i in range(len(word)-1):
#     if word[i] == word[i+1]:
#         count = count + 1
#     else:
#         new = new + word[i] + str(count)
#         count = 1
# new = new + word[-1] + str(count)
# print(new)


# 3. 

# m = [
#     [1,0,0],
#     [0,1,0],
#     [0,0,1]
#     ]

# diagonal = False
# count = 0

# for i in range(len(m)):
#     for j in range(len(m)):

#         if m[i][j] == 1:
#             count = count + 1
#             if i != j and m[j] == 0:
#                 diagonal = True
#             else:
#                 diagonal = False
#         else:
#             diagonal  = False

# print(diagonal)


# Day 28/08/2026 

# word = "programming"
# vowel = 0
# consonant = 0

# for i in range(len(word)):
#     if word[i] in "AEIOUaeiou":
#         vowel = vowel + 1
#     elif word[i] in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
#         consonant = consonant + 1
# if vowel > consonant:
#     print(vowel, "more vowels")
# elif consonant > vowel:
#     print(consonant, "more consonants")
# else:
#     print("Both are equal", vowel, consonant)


# digit = "212"
# sum = 0
# # Output: 2

# for i in range(len(digit)):
#    sum = sum + int(digit[i])
# sum = str(sum)

# total = 0
# count = 0
# for j in range(len(sum)):
#    count = count + 1
#    total = total + int(sum[j])
#    final = total
#    if count > 1:
#       total = str(total)
#       final = 0
#       for k in range(len(total)):
#          final = final + int(total[k])
# print(final)
         


# arr =  [1, 5, 2, 8, 3]
# # Output: True
# zigzag = False 

# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1] or arr[i] < arr[i+1]:
#         zigzag = True
#     else:
#         zigzag = False
#         break
# print(zigzag)


# Q4: 4.Tic-Tac-Toe Winner Checker ❌⭕ Given a 3x3 board ("X", "O", or ""), determine the 
# winner by checking all rows, columns, and both diagonals. 

# m = [["X","X","O"],
#     ["O","X",""],
#     [" "," ","X"]]

# x_winner = False
# o_winner = False    

# for i in range(len(m)):
#   for j in range(len(m)):
    
#     if m[i][0] == m[i][1] == m[i][2] == "X":
#         x_winner = True
#     elif m[i][0] == m[i][1] == m[i][2] == "O":
#         o_winner = True 

#     if m[i][j] == "X" or m[i][len(m)-j]:
#         x_winner = True
#         o_winner = False
    
#     elif m[i][j] == "O":
#        o_winner = True
#        x_winner = False
            
# print("X is winner:", x_winner)
# print("O is winner:", o_winner)



# Day 1/09/2026

# sentence = "Hello! How are you ? I am fine."
# count = 0

# for i in range (len(sentence)):
#     if sentence[i] in "?!.":
#         count = count + 1
# print(count)


# Q2: Longest Palindromic Substring 
# Find the longest substring within a string that reads the same forwards and backwards.

# word = "babad"



# Q3: Sudoku Row Validator Check if a single Sudoku row is valid — no duplicate numbers
# (ignore any 0s, which represent empty cells). 

# arr = [5,0,4,6,0,8,8,2]
# new = []
# valid = True

# for i in range(len(arr)):

#     if arr[i] in  new:
#         if arr[i] != 0:
#          valid = False
#     else:
#         if arr[i] != 0:
#          new = new + [arr[i]]

# print(valid)


# Q4: Rotate Matrix 90° Clockwise 🔄
# Rotate a matrix 90 degrees clockwise. And output should be in nested array format.

# m = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# result = []


# for i in range(len(m)):
#     row = []

#     for j in range(len(m)):
#         row.append(m[len(m)-1-j][i])

#     result = result + [row]

# print(result)


# arr = [4,3,5,6,7]
# i = 0
# j = len(arr)-1
# while i < j:
#     arr[i], arr[j] = arr[j], arr[i]
#     i = i + 1
#     j = j - 1
# print(arr)


# day 3/09/2026 

# 1. Sum of Even Numbers

# arr = [1,2,3,4,5,6,7,8]
# sum = 0
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         sum = sum + arr[i]
# print(sum)



# Q2:Print numbers from start to end. Replace multiples of 3 with "Fizz", multiples of 5
#  with "Buzz", and multiples of both with "FizzBuzz". 

# Input: start=1, end=15
# Output: ['1','2','Fizz','4','Buzz','Fizz','7','8','Fizz','Buzz','11','Fizz','13','14','FizzBuzz']


# start = 1
# end = 15
# for i in range(start, end + 1):

#     if i % 3 == 0:
#         if i % 5 == 0:
#             print("FizzBuzz")

#         else:
#             print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")

#     else:
#         print(i)  



# Q4: Segregate Negatives and Positives (Stable)
# Rearrange an array so all negative numbers come first, followed by all positive numbers — keeping their original relative order within each group. 

# arr =  [1, -2, 3, -4, 5, -6, 7]
# Output: [-2, -4, -6, 1, 3, 5, 7]


# arr =  [1, -2, 3, -4, 5, -6, 7]

# for i in range(len(arr)):
#     for j in range(len(arr)-1):

#         if arr[j] > 0 and arr[j+1] < 0:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)


# 3.
digit = 153
digit = str(digit)
N = len(digit)
total = 0
for i in range(N):
    a = int(digit[i]) ** N
    total = total + a
if total == int(digit):
    print("Armstrong")  
else:
    print("Not Armstrong")
    
