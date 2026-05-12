from cmath import pi

# Day 2: 30 Days of python programming

first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = "Artur", "Andrulewicz", "Artur Andrulewicz", "Poland", "Suwalki", 32, 1994, False, True, False

print("first_name type is", type(first_name))
print("last_name type is", type(last_name))
print("full_name type is", type(full_name))
print("country type is", type(country))
print("city type is", type(city))
print("age type is", type(age))
print("year type is", type(year))
print("is_married type is", type(is_married))
print("is_true type is", type(is_true))
print("is_light_on type is", type(is_light_on))

print("first_name length is ", len(first_name))

print("Imie jest tak samo dlugie jak nazwisko: ", len(first_name) == len(last_name))


num_one = 4
num_two = 5
total = sum([num_one, num_two])
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two / num_one
exp = pow(num_one, num_two)
floor_division = num_one // num_two
floor_division2 = int(num_one / num_two)

def print_circle_info(r):
    if (type(r) != type(int())) & (type(r) != type(float())) :
        print("Can't print for non numeral")
    else:
        r = abs(r)
        print("Circle area = ", (pi * pow(r, 2)))
        print("Circle circumference = ", (2 * pi * r))

print_circle_info(30)

radius = input("Provide radius for circle area and circumference you want to calculate: ")
print_circle_info(int(radius))

first_name = input("What's your first name? ")
last_name = input("What's your last name? " )
country = input("What's your country? ")
age = int(input("What's your age? "))

help("keywords")
