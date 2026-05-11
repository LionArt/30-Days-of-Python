from sys import argv

x : str = 15.3
lista : list = [ "Tom", "Jerry", "Tim", "Bom", "Dim" ]
dialog : str = """Ricky: Zajebiscie kocham lukrecje. 
Barbara: Ja tez."""
print(dialog)

dialog : str = (
    "Ricky: Zajebiscie kocham lukrecje.\n" 
    "Barbara: Ja tez."
)
print(dialog)

dialog : str = ("""\
Ricky: Zajebiscie kocham lukrecje.
Barbara: Ja tez."""
)
print(dialog)

print(lista)
print(lista[0], " & ", lista[1])
print("Hello World!")

lista_mixed : list = [ "Artur", 32, "Suwałki", 190, 97.8, 18 ]
print(lista_mixed)
lista_mixed[1] = 33
print(lista_mixed)


tupla : tuple = ( "Artur", 32, "Suwałki", 190, 97.8, 18 )
print(tupla)
# tupla[1] = 33 -> CAUSES ERRROR
tupla = "Oh Cock"
print(tupla)

dictionary : dict = {
    "name" : "Artur",
    "city" : "Suwalki"
}

secik : set = { "Artur", 32, "Suwałki", 190, 97.8, 18 }

print(dictionary)
print(dictionary["name"])

if (len(argv) > 1) :
    print(argv[1])

print(secik)

lista : list = [ 10, 9.8, 3.14, 4 - 4j, ['Artur', 'Python', 'Polska'], "Artur" ]

for element in lista:
    print(type(element))

import cmath

def euclidean(a, b) -> float:
    return cmath.sqrt(( (b[0] - a[0]) ** 2) + ( (b[1] - a[1]) ** 2))

print(euclidean((2, 3), (10,8)))