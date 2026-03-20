# #Sequence 
# name = "Nitesh","Rahul","123"
# print(name)

# #List
#  # Create a list
# my_list = [1, 2, 3, 4]

# # Add item
# my_list.append(5)
# print(my_list)
# # Remove item
# my_list.remove(2)
# print(my_list)
# # Access item
# print(my_list[0])  # first element
# #insert
# my_list.insert(25,89) 
# print(my_list)


# # #Dictionary
# my_dictionary = {'Nmae':"Nitesh",'Age':27,'Name2':"Lucky",'Age2':36}
# print(my_dictionary)


# #set 
# my_sets = {1,23,43,"Nitesh"}
# print(my_sets)
# print(type(my_sets))
# name = "Nitesh"
# print(name)

# my_list  = [1,23,43,87,"you are not performing well"]
# print(my_list)
# print(len(my_list))
# #removing value in list 
# my_list.remove(43)
# print(my_list)
# my_list.pop() #last element
# print(my_list)
# del my_list[0] #by indexing 
# print(my_list)
# print(my_list)




# age  = int(input("Enter Your Age : "))
# if age < 13:
#     print("You are a child")
# elif age < 20:
#     print("You are Teenager.")
# elif age < 60:
#     print("You are Adult")


#Tuple operation 
a = (1,2,5)
b = (25,35,645) 
 #not changeable tuple
print(a+b)


my_tuple = (25,364,65,6542,3552,665)
# my_tuple.remove(25)
print(my_tuple)


a = ("It's a rainy day \n you are a Bad man ")
print(a)

a = ("It's a rainy day\tyou are a Bad man ") #\t for space
print(a)

a = ("It's a rainy day      you are a Bad man ")  #for length of the string
print(a)

a = ("It's a rainy day you are a Bad man ")
print(len(a))

a = ("It's a rainy day you are a Bad man ")
print(a.find('t'))


a = ("It's a rainy day you are a Bad man ") #indexing string
print(a[-11])


a = ("It's a rainy day you are a Bad man ") #slicing string
print(a[6:-11])

a = ("It's a rainy day you are a Bad man ") #membership
print("b" in 'rainy') #false

a = ("It's a rainy day you are a Bad man ")
print(a.lower())

a = ("It's a rainy day you are a Bad man ")
print(a.upper())

a = ("It's a rainy day you are a Bad man ")
print(a)

a = ("It's a rainy day you are a Bad man ")
print(a.capitalize())

a = ("It's a rainy day you are a Bad man ")
print(a.title())


a = (" It's a rainy day you are a Bad man ")
print(a)

a = ("  It's a rainy day you are a Bad man                ")
print(a.strip())

a = ("It's a rainy day you are a Bad man ")
print(a.replace('a','b'))


a = ("It's a rainy day you are a Bad man ")
print(a.find('a'))

a = ("It's a rainy day you are a Bad man ")
print(a.count('a'))

a = ("It's a rainy day you are a Bad man ")
print(a.startswith("a")) #  True / False

a = ("It's a rainy day you are a Bad man ")   #  True / False
print(a.lstrip().startswith("a"))

a = ("It's a rainy day you are a Bad man ")     #  True / False
print(a.lstrip().startswith("i"))

a = ("It's a rainy day you are a Bad man ")     #  True / False
print(a.lstrip().startswith(" "))

you = "you are a person of Aura"
me = you.split()
print(me)









