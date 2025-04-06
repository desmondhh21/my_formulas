
#Prints area of a square
def square_area(length, width):
    return length * width
print("The area of this square is:", square_area(4,84))

#Prints area of a triangle
def triangle_area(base, height):
    return (base * height) /2
print("The area of this triangle is:", triangle_area(4,8))

#Prints area of a circle
def circle_area(radius, pi = 3.141592653589793):
    return pi * (radius ** 2)
print("The area of this circle is:", circle_area(55))

#Prints if you should go into a stock trade based on it's RSI
def rsi_signal(rsi):
    if rsi < 5 or rsi > 95:
        print("Pull the trigger!", "RSI is", rsi)
    else:
        print("Don't pull the trigger yet!", "RSI is", rsi)

rsi_signal(54)

#Prints the graviational focre of two object inputs
def gravitational_force(m1, m2, distance, gconstant = 6.677430 * 10**-11):
    return gconstant * (m1 * m2) / distance ** 2
print("The gravitational force for these two obnjects is:", gravitational_force(24, 5, 5))

