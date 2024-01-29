import math
# math is a module which include functions
# has constants like pi
barrel_height_yo = 1
distance_travelled_x = 0.5
elevation_angle_degree_o= 80
gravity_accelerate_g = 9.81
initial_velocity_vo = 44

# converting the argument degrees into radians using the math radians function
# needs to be radians to then be used in cos and tan functions -
# passing argument of the elevation angle in degrees to be converted
theta = math.radians(elevation_angle_degree_o)
# theta2 = elevation_angle_degree*(math.pi/180) - gets the same value as maths radians
print(theta)

# PEMDAS - parentheses, exponents, multiplication/ division, addition/ subtraction
# math.tan returns the tangent of the argument
# Broken down the calculation into its parts
# On the right hand side of the equation, the top half of the equation (gx^2)
# function pow will square the value of distance travelled
calc_grav_dist = gravity_accelerate_g * pow(distance_travelled_x, 2)
print('Gravity acceleration multiplied by square of distance travelled: ' + str(calc_grav_dist))
# calculating cosine of an angle - theta is the argument and cos returns the cosine value
# using pemdas it will evalutate what is inside the brackets, then it will multiple once done
calc_cos_vel = 2*(44 * math.cos(theta)**2)
print('velocity multiplied by cosine, squared and then multiplied by 2: ' + str(calc_cos_vel))
# using pemdas the sum will evaluate the calculation within the brackets first and then look at mult/ addition
answer = barrel_height_yo + distance_travelled_x * math.tan(theta) - (calc_grav_dist / calc_cos_vel)
print('The answer: ', str(answer))


projectile_height = barrel_height_yo + distance_travelled_x * math.tan(theta) - (gravity_accelerate_g * pow(distance_travelled_x, 2) / (2 * (44 * math.cos(theta) ** 2)))
print('Projectile height: ' + str(projectile_height))


