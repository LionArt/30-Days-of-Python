strings = ['Thirty', 'Days', "Of", "Python"]
one_string = " ".join(strings)

print(one_string)

strings = ['Coding', 'For', 'All']
one_string = " ".join(strings)

print(one_string)

company = one_string
print(company)

print(len(company))
print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

company = company[7::]
print(company)

result = "Coding For All".find("Coding") != -1
print("Does \"Coding For All\" contain \"Coding\"?", result)

coding = "Coding For All"
print(coding.replace("Coding", "Python"))
print("Python For Everyone".replace("Everyone", "All"))
print("Coding For All".split(" "))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))
print("Coding For All"[0])
print("Coding For All"[-1])
print("Coding For All"[10])

def get_acronym(x) -> str:
    if type(x) != type(str()):
        return "Not a string"
    temp = x.split(" ")
    result = ""
    for word in temp:
        result += word[0].upper()
    return result

print(get_acronym("Python For Everyone"))
print(get_acronym("Coding For All"))

print("First \"C\" found in index [","Coding For All".index("C"),"]")
print("First \"F\" found in index [","Coding For All".index("F"),"]")
print("Last \"l\" found in index [","Coding For All People".rfind("l"),"]")
print("First \"because\" found in index [","You cannot end a sentence with because because because is a conjunction".find("because"),"]")
print("Last \"because\" found in index [","You cannot end a sentence with because because because is a conjunction".rfind("because"),"]")
print("You cannot end a sentence with because because because is a conjunction".replace("because because because", "", 1))
print("Coding For All starts with \"Coding\": ","Coding For All".startswith("Coding"))
print("Coding For All ends with \"coding\": ","Coding For All".endswith("coding"))
print("   Coding For All      ".strip())
print("\"30DaysOfPython\" is identifier: ","30DaysOfPython".isidentifier())
print("\"thirty_days_of_python\" is identifier: ","thirty_days_of_python".isidentifier())
print("#".join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")