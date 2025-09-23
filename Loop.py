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

# count = 0
# while True:
#     num = int(input("enter number:"))
#     if num < 0:
#         continue
#     count += 1

#     if num == 8:
#         print("You have guessed the number")
#         break

#     if count == 4:
#         print("attempt over reached the limit",count)
#         break
    
#     print("keep trying",count)


# 9.Start with a number n = 1. Keep incrementing and printing it.
#   Skip printing multiples of 7 using continue. Break the loop when n becomes greater than 100.

# n = 1
# while n <= 100:
#     if n % 7 == 0:
#         n += 1
#         continue
#     if n > 100:
#         break
#     print(n)
#     n += 1


# 10.Continuously take words from the user. Skip words shorter than 3 letters, and 
#    stop the loop when the user enters "stop".

# while True:
#     word = input("enter word:")
#     if len(word) < 3:
#         continue
#     if word == "stop":
#         break
#     print(word)


# level increased 

# 1.Keep asking the user to enter numbers. Skip negative numbers using continue. 
#   Stop if the running sum of entered numbers exceeds 500.

# sum = 0
# while True:
#     num = int(input("Enter number:"))
#     if num < 0:
#         continue
#     sum += num
#     if sum > 500:
#         break
#     print(num)
   

# 2.Continuously read characters from the user. Skip vowels using continue. 
#   Stop the loop if the user enters a digit.

# while True:
#     char = input("Enter character:")
#     if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#         continue
#     if char.isdigit():
#         break
#     print(char)


# 3.Keep generating random numbers between 1–20. Skip numbers less than 5 using continue.
#   Stop when you get exactly 13.

# while True:
#     num = int(input("Enter any number:"))
#     if num < 5:
#         continue
#     if num == 13:
#         break
#     if num > 20:
#         break
#     print(num)


# 4.Start with a counter at 50. Keep subtracting 3 each loop. Skip printing if the result is negative. 
#   Stop the loop if the counter becomes exactly 11.

# counter = 50
# i = 3
# while counter >= 11:
#     if counter  == 11:
#         break
#     print(counter)
#     counter -= i


# 5.Continuously accept numbers from the user. 
#  Skip multiples of 10. Stop if the number is prime.
num = int(input("Enter a number: "))
if num < 2:
    print("Not prime")
else:
    i = 2
    is_prime = True
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, "is prime")
    else:
        print(num, "is not prime")

