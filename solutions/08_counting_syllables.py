"""Counting syllables
Define a function named count that takes a single parameter. 
The parameter is a string. The string will contain a single word divided
 into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2.
"""
"""
count isminde bir fonksiyon yazın. Bu fonksiyon bir adet string parametre alsın.
Bu string hecelere ayrılmış bir kelime olsun. Hecelerin arasında - işareti olsun.
Mesela:
"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Fonksiyonunuz heceleri saysın, ve hece sayısını dönsün.

Mesela count("ho-tel") fonksiyonu çağrıldığında, fonksiyon 2 dönsün.
"""


# def count(string):
#     counter = 1
#     for i in string:
#         if i == "-":
#             counter += 1
#     return counter


# print(count("ter-min-a-tor"))

# naive solution
def count(word):
    syllables = 1
    for letter in word:
        if letter == "-":
            syllables = syllables + 1
    return syllables

# using the count method


def count(word):
    return word.count("-") + 1

# using split


def count(word):
    return len(word.split("-"))
