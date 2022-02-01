"""
Flatten a list
Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])
Should return the list:

[1, 2, 3, 4]
"""

"""
flatten adında bir fonksiyon yazın. Parametresi listelerden oluşan bir liste olsun.
Fonksiyon bu listeyi tek boyutlu bir listeye dönüştürsün. Bu listeyi dönsün.

mesela eğer flatten([[1, 2], [3, 4]]) çağrılırsa:
fonksiyon şunu dönsün:
[1, 2, 3, 4]

"""


# def flatten(list):
#     lastList = []
#     for i in list:
#         for j in i:
#             lastList.append(j)
#     return lastList


# print(flatten([[1, 2], [3, 4]]))

# naive solution
def flatten(outer_list):
    result = []
    for inner_list in outer_list:
        for item in inner_list:
            result.append(item)
    return result

# solution with nested list comprehensions
# (can be put on a single line for conciseness)


def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]
