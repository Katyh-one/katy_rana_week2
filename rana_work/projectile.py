# maths function used to input pi, tan & cos
import math

# Assigning the number variables
g = 9.81
vo = 44
pi = math.pi
degrees = 80
x = 0.5
yo = 1
# Theta calculation based on example
theta = degrees * (pi / 180)

# Variable created to multiply g by x squared. Using the math.pow function to square x Can use **2 instead of math.pow
gx_squared = g * math.pow(x, 2)

# Variable created to input cos in to the formula using 'math.cos' and then square it using math.pow
vo_cos_squared = (vo * math.pow(math.cos(theta), 2))

# Formula used to calculate height of a projectile using above variable combinations
y = yo + x * math.tan(theta) - (gx_squared / 2 * vo_cos_squared)

# Print checks for elements
# Calculator returns 2.873
print(theta)
print(x * math.tan(theta))
print(gx_squared)
print(math.cos(theta))
print(2 * vo_cos_squared)
print(y)
