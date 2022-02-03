"""
Divisible by 3
Define a function named div_3 that returns True if its single integer parameter 
is divisible by 3 and False otherwise.

For example, div_3(6) is True because 6/3 does not leave any remainder. 
However div_3(5) is False because 5/3 leaves 2 as a remainder.
"""

"""
div_3 adında bir fonksiyon yazın, tek integer parametresi olsun. Eğer bu parametre 
3 e bölünebilirse True, yoksa False dönsün.

Mesela div_3(6) True dönsün çünkü 6/3 ün kalanı sıfırdır. div_3(5) ise False çünkü 
5/3 kalanı 2 dir.


"""


# def div_3(num):
#     if num % 3 == 0:
#         return True
#     else:
#         return False


# print(div_3(6))
# print(div_3(5))


def div_3(n):
    return n % 3 == 0
