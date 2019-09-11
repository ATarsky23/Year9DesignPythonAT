#Comments are made with a #
#It is essentail you comment 
#code

#This program will take to intergers

#Input
#The input function returns the string the user end
#All inputs start as Strings
#Casting is the proscess of changing type
#To change the type of variuble you "cast" i
name=input("Please input your name: ")
a=input("Please input your first number: ")
a=int(a)#self-referincing assiggmnet statemnet
b=input("Please input your second number: ")
b=int(b)

#Proscess
product= a * b

#Output
print("Hi "+name)
print("The product of "+str(a)+" and "+str(b)+" is "+str(product)+".")
