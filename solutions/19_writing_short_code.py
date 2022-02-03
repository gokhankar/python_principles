"""
Writing short code
Define a function named convert that takes a list of numbers as its 
only parameter and returns a list of each number converted to a string.

For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

What makes this tricky is that your function body must only contain a 
single line of code.
"""
"""
convert adında bir fonksiyon yazın. Tek parametresi sayılardan oluşan bir
liste olsun. Ve bu fonksiyon her sayının stringe dönüştürüldüğü bir liste dönsün.

Mesela convert([1, 2, 3]) çağrıldığında, ["1", "2", "3"] dönsün.

Biraz daha zorlaştıralım, fonksiyonunuz içeriği tek satıdan oluşsun.(single line of code)
"""

# using a list comprehension




from typing import Type
def convert(ns):
    return [str(n) for n in ns]

# using map


def convert(ns):
    return list(map(str, ns))


myList = [1, 2, 3, 4, 5, "a", "b", "c", 8, 9, 1, 2, 3, "merhaba"]
myNewList = []
for i in myList:
    if type(i) == int:
        myNewList.append(i)
print(myNewList)


# myNewList = [i for i in myList if type(i) == int]
