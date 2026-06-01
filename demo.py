# def mean(a,b):
#     m = (a*b)/(a+b)
#     return m

# value = mean(8,4)
# print(value)

# num = int(input("Enter number: "))
# f=1
# for i in range(1,num):
#     f = f*i

# while(num>0):
#     f=f*num
#     num=num-1
    
# print("Factorial of ",num," is ",f)

# num = int(input("Enter number: "))
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return (n * factorial(n-1))
        
# print("Factorial of",num,"is",factorial(num))

# fibonacci series
# def fibonacci(n):
#     if(n<=1):
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# num = int(input("Enter number of terms: "))

# for i in range(num):
#     print(fibonacci(i))

# str = input("Enter value: ")

# if (str=="quit"):
#     print("Correct")
# else:
#     raise ValueError("Invalid value")

# import random
# import string

# message = input("Enter message: ")
# type = input("Enter what you wanna do: ") #encode or decode

# Encode - if the word is smaller than 3 letters, reverse it
#        - if the word is greater than 3 letters, remove first letter and append it at the end, add 3 random letters in starting and at the end
# Decode - if the word is smaller than 3 letters, reverse it
#        - if the word is greater than 3 letters, remove 3 random letters from starting and at the end, remove last letter and append it at the start

# if(type=="encode"):
#     messageList = message.split(" ")
#     new_message=""
#     for word in messageList:
#         if(len(word)<3):
#             new_word=word[::-1]
#             new_message+=new_word+" "
#         else:
#             # Remove first letter and append it at the end
#             word_shifted = word[1:] + word[0]
#             # Add 3 random letters in starting and at the end
#             random_start = "".join(random.choices(string.ascii_letters, k=3))
#             random_end = "".join(random.choices(string.ascii_letters, k=3))
#             new_word = random_start + word_shifted + random_end
#             new_message+=new_word+" "
#     print(new_message.strip())
# else:
#     messageList = message.split(" ")
#     new_message=""
#     for word in messageList:
#         if(len(word)<3):
#             new_word=word[::-1]
#             new_message+=new_word+" "
#         else:
#             # Remove 3 random letters from starting and at the end
#             word_stripped = word[3:-3]
#             # Remove last letter and append it at the start
#             new_word = word_stripped[-1] + word_stripped[:-1]
#             new_message+=new_word+" "
#     print(new_message.strip())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"{self.name} is {self.age} years old")


a = Person("Ashwini", 24)
b = Person(20, 25)
a.details()
b.details()