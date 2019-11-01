import math

#Input
#What inputs are needed to calculate the volume of a cylinder?
file = open("data.txt","w")

print("\n\tThe volume of a Cylinder is:")
print("\n\t\t\tV = \u03C0\u00d7radius\u00b2\u00d7height")
print("\n\tThis program will take a radius and height which you provide")
print("\tand print the volume! (Cool,eh?)")

height = 1
radius = 1

name = input("What is your name: ")   #takes users name


while  (radius >= 0 and height >= 0):
	#Loop
	radius = input("\n\tInput radius(cm): ")
	radius = (int)(radius)      #cast to int

	height = input("\n\tInput height(cm): ") #input
	height = (int)(height)     #cast to int

	#Process
	#What formula is used to calculate the volume of a cylinder?








	volume=math.pi*radius*radius*height
	volume = round(volume,2)

	#Output
	print("Hi "+name+"!")
	print("Given a cylinder with:")
	print("\n\tRadius = "+str(radius))
	print("\n\t\tand")
	print("\n\tHeight = "+str(height))
	print("\nThe volume is: "+str(volume),"to 2 decimal places.")
	#What is important about the output?

	#END OF WHILE BLOCK