# Michael L. Kelley Jr.
# Polygon.py
# 11/14/12
# Draw polygon based on user input


import turtle  	# Turtle graphics mode

def polygon(length, sides):
	for i in range(sides):
		turtle.fd(length)
		turtle.left(360/sides)

 # Display a greeting and some ask for input

print("Welcome to Polygon Creator!")

how_many = int(input("How many sides do you want?"))
how_big = int(input("How long should these sides be?"))

# Draw the output

polygon(how_big, how_many)

input("Press a key to quit.")
