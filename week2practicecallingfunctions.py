import math
number_to_root = float (input ("Tell me a number, thanks:"))
print (math.sqrt(number_to_root))

if math.sqrt(number_to_root) < 100:
    print ("the raiz cuadrada es menor que 100.")
elif math.sqrt(number_to_root) > 100: 
    print ("the raiz cuadrada es mayor que 100.")
else:
    print ("the raiz cuadrada es exactamente 100.")
#practice of the video1: 

fname= input ("please write your name:" )
lname= input ("please write your last name:")
major= input ("please write your major:")
print (fname, lname, major, sep="/") 

#modulos: 
import math
area = float(input("what is the area of the square inches: "))
side = math.sqrt (area)
print (f"the side of the side of the square is: {side}inch.")