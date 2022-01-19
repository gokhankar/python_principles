"""
Type check
Write a function named only_ints that takes two parameters. 
Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, 
while calling only_ints("a", 1) should return False.
"""
"""
only_ints adında, iki parametre alan bir fonksiyon yazınız. 
Yazdığınız fonksiyon, eğer iki parametre de integer ise True dönmelidir. 
Diğer olasılıklarda ise False dönmelidir.
Mesela;
only_ints(1, 2)  çağrıldığında True dönmeli,
only_ints("a", 1) çağrıldığında False dönmelidir.
"""


def only_ints(num1, num2):
    if type(num1) == int and type(num2) == int:
        print(True)
        # return True
    else:
        # return False
        print(False)


only_ints(1, "2")
