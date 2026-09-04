# day 4/09/2026 

# sentence = "Hello World From India"
# count = 0

# for i in range(len(sentence)):
#     if sentence[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         count = count + 1
# print(count)


# 2. count the vowels 

# sentence = "Akriti is eating an apple today"

# count = 0

# for i in range(len(sentence)-1):
#     if sentence[i] == " ":
#         if sentence[i + 1] in "AEIOUaeiou":
#             count = count + 1
# if sentence[0] in "AEIOUaeiou":
#     count = count + 1


# print(count)

# Q3: String Rotation Checker 🔄
# Check if one string is a rotation of another (e.g., "bottlewater" is "waterbottle" rotated).

# string = "water" 
# rotation = "terwa"
# # Output: True
# isRotation = False
# for i in range(len(string)):
#     rotated_string = string[i:] + string[:i]
#     if rotated_string == rotation:
#         isRotation = True  


# print(isRotation)



# Q4: Diamond Star Pattern 💎: 
# Print a diamond shape made of stars, given the number of rows for the top half.

  
text = "water"


print(text[2:])  
print(text[:2]) 
