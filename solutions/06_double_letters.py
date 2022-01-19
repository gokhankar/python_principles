"""
Double letters
The goal of this challenge is to analyze a string 
to check if it contains two of the same letter in a row. 
For example, the string "hello" has l twice in a row, 
while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. 
The parameter is a string. Your function must return True if there 
are two identical letters in a row in the string, and False otherwise.
"""
"""
Bu alıştırmanın amacı bir stringin ardarda iki aynı harf içerip içermediğinin kontrolüdür.
Mesela "hello" stringi ardarda iki "l" harfi içermektedir.
"nono" stringi ise ardarda iki özdeş harf içermemektedir.
double_letters adında ve tek parametre alan bir fonksiyon yazın. 
Parametre bir string olsun. Eğer bu parametre ardarda aynı harf içeriyorsa True,
aksi durumda False dönsün.
"""


def double_letters(text):
    result = False
    letter = ""
    for i in text:
        if i == letter:
            return True
        letter = i

    return result

# def double_letters(string):
#     for i in range(len(string) - 1):
#         letter1 = string[i]
#         letter2 = string[i+1]
#         if letter1 == letter2:
#             return True
#     return False
