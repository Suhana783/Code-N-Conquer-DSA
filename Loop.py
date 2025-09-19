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



   