import math

#Input
#What inputs are needed to calculate the volume of a cylinder?

print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03C0\u00d7radius\u00b2\u00d7height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")



name = input("What is your name: ")   #takes users name

radius = input("\n\tInput radius(cm): ")
radius = (int)(radius)      #cast to int

height = input("Input height(cm): ") #input
height = (int)(height)     #cast to int

#Process
#What formula is used to calculate the volume of a cylinder?

volume=math.pi*radius*radius*height
volume = round(volume,2)

#Output
print("Hi "+name+"!")
print("Give a cylinder with:")
print("Radius = "+str(radius))
print("Height = "+str(height))
print("The volume is: "+str(volume))  
#What is important about the output?
