x = "sun"
y = "moon"
z = "stars"
print(x, y, z, sep="|", flush=True)   
#imprimir separados por la linea como tal
#######################################
import math

r = math.sqrt(71)
print(r)

#el squart es para sacar la raí cuadrada 
#######################################3
n = float(input("Please enter a number: "))
r = round(n)
print(r)

########################################3

# Example 6

# Get a string of text from the user.
text1 = input("Enter a motivational quote: ")

# Call the built-in len function to get the number of characters in the text. ojo aqui cuenta hasta los espacios. 
length = len(text1)

# Call the string upper method to convert the quote to upper case characters.
text2 = text1.upper()
text3 = text1.capitalize()

# Call the built-in print function to print the length of the text and the text in all upper case for the user to see.
print(length, text2, text3)

#############################
text = input("Enter a motivational quote: ")
# Example 7

import math

# Get a number from the user.
number = float(input("Enter a number: "))

# Call the math.sqrt function and
# immediately print its return value.
print( math.sqrt(number) )

# Call the math.sqrt function again and
# use its return value in an if statement.

if math.sqrt(number) < 100:
    print(f"The square root is less than 100.")
elif math.sqrt(number) > 100:
    print(f"The square root is more than 100.")
else:
    print(f"The square root is exactly 100.")



