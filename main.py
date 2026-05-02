
##1
# persons=[
#     {'name':'Saisha','age':10},{'name':'Jammie','age':19},{'name':'Yatra','age':10},{'name':'Dennis','age':20}   
# ]
# # Filter people age 18 and above
# ages=(filter(lambda p:p['age']>18,persons))
# #Get names
# names=(map(lambda p:p['name'],ages))
# print(list(names))

##2
# from functools import reduce
# a=[1,2,3,4,5]
# product=(reduce(lambda x,y:x*y,a))
# print(product)

##3
# numbers=[1,2,3,4,5,6,7,8,9]
# #using a lambda function to check for even numbers
# even=list(filter(lambda n:n%2==0,numbers))
# # square=list(map(lambda a:a*a,even))
# # print(square)
# # list comprehension for squares
# square=[a*a for a in even]
# print(square)


##4
# #isdigit() is a string method in Python.
# #It checks whether all characters are digits (0 to 9).
# check=lambda x:x.isdigit()
# print(check("123"))
# print(check("abc123"))

# ##5
# # import datetime class
# from datetime import datetime
# #now() is a method,it gives current system date and current time
# today=datetime.now()
# extract=lambda d:(d.year,d.month,d.day)#today goes into d
# print(extract(today))

# #alternate way
# from datetime import datetime  
# def extract(d):
#     return (d.year, d.month, d.day)
# today = datetime.now()
# print(extract(today))

###6

#Using recursive-Because the function calls itself inside its own definition.
fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
# fib = function name
# lambda = one-line function
# n = input number
# if n <= 1 return n
# fib(0) = 0
# fib(1) = 1
# else return previous two Fibonacci numbers added
# fib(n-1) + fib(n-2)
for i in range(10):
 print(fib(i), end=" ")

# #alternate way
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# fib(10)