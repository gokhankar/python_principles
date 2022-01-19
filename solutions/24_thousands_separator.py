"""
Thousands separator
Write a function named format_number that takes a non-negative number 
as its only parameter.

Your function should convert the number to a string and add commas as a
thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
"""
"""
format_number adında bir fonksiyon yazın. Bu fonksiyon negatif olmayan bir sayıyı 
parametre olarak alır.
Bu fonksiyon bu sayıyı stringe çevirir ve binlikleri virgül ile ayırır.
Mesela;
format_number(1000000)
"1,000,000" döner.
"""


# def format_number(num):
#     text = str(num)
#     myList = []
#     for i in text:
#         myList.insert(0, i)
#     counter = 1
#     myLastList = []
#     for i in myList:
#         if len(myList) == counter:
#             myLastList.insert(0, i)
#             break
#         elif counter % 3 == 0:
#             myLastList.insert(0, i)
#             myLastList.insert(0, ",")
#         else:
#             myLastList.insert(0, i)
#         counter += 1
#     lastText = "".join(myLastList)
#     print(lastText)


# built-in solution
def format_number(n):
    return "{:,}".format(n)


format_number(100000)
