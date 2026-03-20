# str = ("SAITM Collleg")
# print(str[0])
# str = "SAITM Collleg"
# print(str[1:5])
# str = "SAITM Collleg"
# print(str.capitalize())
# str = "SAITM Collleg"
# print(str.upper())
# str = "SAITM Collleg"
# print(str.lower())
# str = "SAITM Collleg"
# print(str.casefold())



#time
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)

# timestamp = time.strftime('%H')
# print(timestamp)

# timestamp = time.strftime('%M')
# print(timestamp)

# timestamp = time.strftime('%S')
# print(timestamp)


#import time

# current = time.time()
# print(current)

# print("Wait for it...")
# time.sleep(2)  # pauses for 2 seconds
# print("Done")

# print(time.ctime())
# print("returns a structured object (year, month, day, etc.)")
# t = time.localtime()
# print(t)




# start = time.time()

# # code to measure
# for i in range(1000000):
#     pass

# end = time.time()
# print("Execution time:", end - start)



#Real Drawings → Turtle Module

#turtle lets you draw actual graphics on screen like a pen.

#import turtle

# t = turtle.Turtle()

# for i in range(5):
#     t.forward(100)
#     t.right(144)

# turtle.done()

#Example 2: Colorful Circle Pattern

# t = turtle.Turtle()

# colors = ["red", "blue", "green", "yellow"]

# for i in range(36):
#     t.color(colors[i % 4])
#     t.circle(100)
#     t.right(10)

# turtle.done()


#Conditional statement
# age  = 19
# if (age>=18):
#     print("eligible for Vote")
# else:
#     print("no eligible for vote")
    
    
    
# import time
# import os

# pattern = ["/ ", "- ", "\ ", "| "]
# for i in range(20):
#     print(pattern[i % 4], end="\r")
#     time.sleep(0.2)

# import turtle

# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.pencolor("green")
# t.speed(0)

# for i in range(1000):
#     t.forward(i * 2)
#     t.right(91)


# mark = 85
# if mark >= 90:
#     print("Grade A")
# elif mark >= 75:
#     print("Grade B")
# elif mark >= 60:
#     print("Grade c")
# else :
#     print("Fail")
    
    
# #Nested if
# num = 12
#if num > 0:
#   if num % 2 == 0:
#     print("Number is even")
#   else :
#     print("Number is Odd")
#else : 
#   print("Number is Negative")
    
#short hand if
# x = 20
# if x > 10: print("x is greater than 10")




# num1 = float(input("Enter 1st Your Number:"))
# num2 = float(input("Enter 2nd Your Number:"))
# operation = input("Choose operation(+,-,*,/):")
# if operation == "+":
#     print("result:",num1+num2)
# elif operation == "-":
#     print("result:",num1-num2)
# elif operation == "*":
#     print("result:",num1*num2)
# elif operation == "/":
#     print("result:",num1+num2)
#     if num2 != 0:
#         print("result",num1/num2)
#     else:
#         print("error:division by zero!")
# else:
#     print("Invalid operation!") 

#weather problem
# weather = input("enter the weather (sunny,rainy,cold):").lower()
# if weather == "sunny":
#     print("wear sunglasses")
# elif weather == "rainy":
#     print("take an umberella")
# elif weather == "cold":
#     print("wear a jacket")
# else:
#     print("I don't know that weather type.")

# #traffic light problrm 
# light = input("Enter traffic light color (red,yellow ,green):")
# if light ==  "red":
#     print("stop")
# elif light == "yellow":
#     print("Get Ready")
# elif light == "Green":
#     print("go")
# else:
#     print("Invailid light color!") 


# #loop in python
# for i in range(5):
#     print("Hello",i)

# #while loop - when we know dont know exact repetition;run until condition is false
# print("While loop")
# count = 1
# while count <= 5:
#     print("Hello",count)
#     count +=1


# #loop control

# #break - exit loop immediatly
# #continue - skip current iteration 
# #pass - do nothing (placehoplder)
# for i in range(1,6):
#     if i == 3:
#         continue
#     if i == 5:
# #         break
# #     print(i)


# #loop inside another loop.
# for i in range(2):
#     for j in range(3):
#         print("i = ",i,"j = ",j)



# for i in range(10):
#     print(i)


# num = 10
# while num>=1:
#     print(num)
#     num -= 1


# for i in range(1,11):
#     print(f"5 x {i} = {5*i}")


# num = 2
# while num <= 20:
#     print(num)
#     num+=1


# rows = 10
# for i in range(1,rows+1):
#     for j in range(i):
#         print("*",end = " ")
#     print()


            #using  pandas 

import pandas as pd

# data = {"Name": ["A", "B","c", "D","E", "F","G", "H"],
#         "Age": [20, 25,36,35,32,25,14,84],
#         "Branch": ["AIML","AIML","AIML","AIML","AIML","AIML","AIML","AIML",],
#         "Section":["A","A","A","A","A","A","A","A",]
#         }
# df = pd.DataFrame(data)

# print(df)


# Data = {
#     "Name":["Nitesh","Rahul","Lucky","Nadeem","Ritesh","Priyesh","Anuj","Ritesh"],
#     "Branch":["B.Tech","B.Tech","B.Tech","B.Tech","BCA","BCA","BCA","BCA"],
#     "Salary":[25000,23000,24000,23000,25000,26000,28000,96000,],
#     "Company Name":["Google","Google","Google","Google","Google","Google","Google","Google",],
#     "Position":["Softwere Engineer","Web Developer","Management","Team Leader","CEO","Head of the management","Machin Engineer","Reader"]
# }
# df = pd.DataFrame(Data)
# #print(df)
# #Basic DataFrame Understanding 
# # print(df.head(3))
# # print(df.columns)
# # print(df.dtypes)
# # print(df.info())
# #print(df.rename(columns={'Salary':'Payment'}))
# print(df.describe())
# df.to_csv('new_data.csv')



# titanic = pd.read_csv("global_central_bank_rates_1945_2026.csv")

# print(titanic.head())
# print(titanic.shape)
# print(titanic.columns)




Data_company = {
    "id": [101,102,103,104,105,106,107,108,109,111,112,113,114,115],
    "name": ["Nitesh","Nitesh","Nitesh","Nitesh","Nitesh","Nitesh","Nitesh","Nitesh","Nitesh","Nitesh","Nitesh","Nitesh","Nitesh","Nitesh","Nitesh",],
    "age": [25,23,26,36,35,36,25,24,25,15,32,26,35,25,42],
    "sallary": [23666,23236,32232,36523,23651,23651,25631,65239,98562,35126,65234,69854,35214,23654,25814],
    "doj":['10022025','11032025','11032025',15032025,20032025,30032025,26032025,15032025,14032025,16032025,19032025,20032025,13032025,18032025,10032025,]
}
df = pd.DataFrame(Data_company)
print(df)