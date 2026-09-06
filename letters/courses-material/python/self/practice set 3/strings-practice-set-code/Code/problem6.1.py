sentence = "Coding in Python is fun"
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in sentence.lower(): 
    if(char in vowels):
        sum += 1

print(f"There are {sum} vowels in this sentence")


# self code

# sentence = "Coding in Python is fun"

# sum = 0

# for char in sentence.lower():
#     # print(char)
#     # print(type(char))
#     if(char == 'a'):
#         sum = sum+1
#     elif(char == 'e'):
#         sum = sum+1
#     elif(char == 'i'):
#         sum = sum+1
#     elif(char == 'o'):
#         sum = sum+1
#     elif(char == 'u'):
#         sum = sum+1
#     else:
#         sum

# print(sum)