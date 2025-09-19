# 1. Write a program that keeps asking the user to enter numbers until they enter a negative number. 
#    Skip even numbers using continue, and stop immediately if the user enters 100 using break.

# while True:
    
#     num = int(input("enter number here:"))
#     if num == 100:
#         break
#     if num < 0:
#         break
#     if num % 2 == 0:
#         continue
#     print(num)
    


# 2. Simulate a simple login system: keep asking for a password until the correct one is entered. 
#    If the user enters "quit", use break to stop the loop.

# while True:
#     password = (input("Please Enter your password:"))
#     if password == "quit":
#         print("Entered correct password")
#         break 
#     if password != "quit":
#         print("wrong password")
#         continue
       


# 3. Generate numbers starting from 1. Print only the numbers not divisible by 3. 
#    Stop the loop if the number reaches 50.

# i = 1
# while i <= 50:
#     if i % 3 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1
        

# 4.Keep reading characters from the user until they type "x". 
#  Ignore spaces using continue and stop completely if they type "q".

# while True:
#     char = input("Enter any character: ")

#     if char == "q":
#         print("Loop stopped")
#         break

#     if char == "x":
#         print("Ending loop, you entered x")
#         break

#     if char == " ":  
#         continue

#     print("You entered:", char)



# 5.Write a program that simulates rolling a dice (random numbers 1–6) until a 6 appears. 
#   Skip printing the number 3 using continue.

# import random

# while True:
#     num = random.randint(1, 6)  
#     if num == 6:                  
#         print("You rolled a 6! Loop ends.")
#         break
#     if num == 3:                 
#         continue
#     print("You rolled:", num)


# 6.Continuously take input of student scores. If the score is negative, stop the loop. 
#   Skip scores greater than 100 using continue.

# while True:
#     score = int(input())
#     if score < 0:
#         break
#     if score > 100:
#         continue
#     print("your score is",score)


# 7.Keep multiplying numbers starting from 1 (factorial style). 
#   Stop if the product goes above 10,000. Skip multiplying with any 0 using continue.

# i = 1
# product = 1
# while product <= 10000:
#     product = product*i
#     if product > 10000:
#         break
#     print(product)
#     i += 1

# 8.Keep asking the user to guess a secret number. If they guess correctly, stop.
#   If they enter a number less than 0, skip without counting it as an attempt.

while True:
    num = int(input("enter number:"))
    if num < 0:
        continue
    if num == 8:
        print("You have guessed the number")
        break
    
    print("keep trying")
   