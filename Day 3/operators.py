age = 32
height = 190.0
complex_number = 190 + 4j

def print_triangle_area():
    triangle_base = input("Enter base of a triangle: ")
    triangle_height = input("Enter height of a triangle: ")
    print("The area of the triangle is", 0.5 * int(triangle_base) * int(triangle_height))


def print_triangle_perimeter():
    a = input("Enter side a: ")
    b = input("Enter side b: ")
    c = input("Enter side c: ")
    print("Perimeter of the triangle is", int(a) + int(b) + int(c))

def print_rectangle_data():
    rectangle_length = int(input("Enter rectangle length: "))
    rectangle_width = int(input("Enter rectangle width: "))
    print("Rectangle area is", rectangle_length * rectangle_width)
    print("Rectangle perimeter is", 2 * rectangle_length + 2 * rectangle_width)


from cmath import pi

def print_circle_data(): 
    circle_radius = float(input("Enter circle radius: "))
    print("Circle area is", pi * pow(circle_radius, 2))
    print("Circle circumference is", 2 * pi * circle_radius)

point1_x = 0
point1_y = 2 * point1_x - 2

point2_x = 1
point2_y = 2 * point2_x - 2

def calculate_slope(pointA, pointB):
    return (pointB[1] - pointA[1]) / (pointB[0] - pointA[0])

first_slope = calculate_slope([point1_x, point1_y], [point2_x, point2_y])

print("Slope equals", first_slope)

def calculate_euclidean_dist(pointA, pointB):
    return pow((pointB[0] - pointA[0]), 2) + pow((pointB[1] - pointA[1]), 2)

point3 = [2, 2]
point4 = [6, 10]

second_slope = calculate_slope(point3, point4)
print("Second slop is", second_slope)
print("Distance between point (",point3[0],",",point3[1],") and (",point4[0],",",point4[1],") =", calculate_euclidean_dist(point3, point4))
print("Two slopes are equal:", first_slope == second_slope)

point5_x = 0
point5_y = pow(point5_x, 2) + 6 * point5_x + 9

# y = x^2 + 6x + 9
# 0 = x^2 + 6x + 9
# x^2 + 6x = -9
# 0 = -3 * - 3 + 6 * - 3 + 9


print("'python' and 'dragon' don't have same length:", len('python') != len('dragon'))

print("'on' can be found in 'python' and 'dragon':",'on' in 'python' and 'on' in 'dragon')

sentence = "I hope this course is not full of jargon"

print("'jargon' found in sencence:", 'jargon' in sentence)

print("There is no 'on' to be found in 'python' and 'dragon':",'on' not in 'python' and 'on' not in 'dragon')

print("Python length in string converted from float converted from length:", str(float(len('python'))))

def is_even(num):
    return (num % 2) == 0

print("Is floor division of 7 and 3 equal to int converted value of 2.7: ", 7//3 == int(2.7))

print("Is type of '10' same as type of 10:", type('10') == type(10))

print("Is int('9.8') equal to 10: ", int(9.8) == 10)

def print_weekly_earnings():
    hours = int(input("Enter hours: "))
    rate_per_h = int(input("Enter rate per hour: "))
    print("Your weekly earning is", hours * rate_per_h)

print_weekly_earnings()

# For training I think we ignore stepping years
 
def print_life_seconds():
    years = int(input("Enter how many years you have lived: "))
    print("You have lived for", years * 365 * 24 * 60 * 60, "seconds.")

print_life_seconds()

def print_table():
    print("""1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125""")
    
print_table()
