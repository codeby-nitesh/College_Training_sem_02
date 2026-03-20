# #Data Set 
# import matplotlib.pyplot as plt
# x = [23,43,54,54,34]
# y = [80,90,70,98,67]
# # plt.plot(x,y)


# # #Costmize chart
# plt.figure(figersize=(4,3))
# plt.plot(x,y,color='red',marker='0',linestyle='--',linewidtgh=2,markersize=12)
# plt.title("St.Andrew Institute of Technology")
# plt.xlable("x-axis label hai")
# plt.ylable("y-axis label hai")
# plt.show


#Multiple Line & Lagends
#import matplotlib.pyplot as plt

# x = [1,2,3,4,5,6,7]
# y1 = [10,20,30,40,50,60,70]
# y2 = [20,30,40,50,60,70,80]

# plt.plot(x, y1, label='Sales 2024')
# plt.plot(x, y2, label='Sales 2025')

# plt.title("Yoy Sales")
# plt.xlabel("Month")   # ✅ fixed
# plt.ylabel("Sales")

# plt.legend()
# plt.show()

# import random
# data =  [random.randint(1,20),for _ in range(500)]
# plt.hist(data,bins=20)
# plt.title("Historgram Example")
# plt.show()

import matplotlib.pyplot as plt
import random

# data = [random.randint(1,20) for _ in range(200)]

# plt.hist(data, bins=20)
# plt.title("Histogram Example")
# plt.show()


# categories = ['A','B','C','D','E']
# sales = [10,20,55,35,45]
# plt.pie(sales,labels=categories,autopct = '%1.1f%%',startangle = 90)
# plt.title("Pie Chart Example")
# plt.show()

# y1 = [10,20,25,35,45]
# y2 = [20,30,40,50,60]

# plt.scatter(y1,y2)
# plt.title("Scatter Plot Example")
# plt.show()

#Data -1
categories = ['A','B','C','D','E']
sales = [10,20,55,35,45]
#dat -2
y1 = [10,20,25,35,45]
y2 = [20,30,40,50,60]

plt.figure(figsize=(10,4))

#figure plot bar chart
plt.subplot(1,2,1) # row colum postion
plt.bar(categories,sales)
plt.title("Daily Seles")
plt.xlabel("Week Days")
plt.ylabel("sales")

#second ploit scatter chart
plt.subplot(1,2,2)
plt.scatter(y1,y2)
plt.title("User Example")
plt.xlabel("User1")
plt.ylabel("User2")

plt.show()




