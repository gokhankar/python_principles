"""
Adding and removing dots
Write a function named add_dots that takes a string and adds "." 
in between each letter. For example, calling add_dots("test") should 
return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots
 that removes all dots from a string. For example, calling remove_dots("t.e.s.t")
  should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) 
should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
"""
"""
add_dots adında bir fonksiyon yazın. Bir string (parametre olarak) alsın 
ve harflerin arasına '.' eklesin. Mesela add_dots('text') çağrıldığında
't.e.s.t' dönsün.
Sonra bu fonksiyonun altına remove_dots adından bir fonksiyon yazın. Bu fonksiyon da
stringdeki bütün noktaları silsin. Mesela remove_dots("t.e.s.t") çağrıldığında
"test" dönsün.
Eğer iki fonskiyon da doğru yazılırsa, remove_dots(add_dots(string)) çağrıldığında
herhangi bir string için, stringin kendisi dönmelidir.
(add_dots fonksiyonuna verdiğimiz stringin nokta içermediğini varsayıyoruz)

"""


# def add_dots(string):
#     counter = 1
#     letterList = []
#     for i in string:
#         if counter != len(string):
#             letterList.append(i + ".")
#         else:
#             letterList.append(i)
#         counter += 1
#     return "".join(letterList)


# def remove_dots(string):
#     letterList = []
#     for i in string:
#         if i == ".":
#             continue
#         else:
#             letterList.append(i)
#     return "".join(letterList)


# add_dots("test")
# remove_dots("t.e.s.t")


# the longer way
def add_dots(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1]


def remove_dots(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out


# the short way
def add_dots(s):
    return ".".join(s)


def remove_dots(s):
    return s.replace(".", "")
