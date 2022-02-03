"""
Solution validation
The aim of this challenge is to write code that can analyze code submissions. 
We'll simplify things a lot to not make this too hard.
Write a function named validate that takes code represented as a string as its only parameter.
Your function should check a few things:
the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.
Here comes the twist: your solution must return True when validating itself.
"""
"""
validate adında bir fonksiyon yazın. Parametre olarak bir string alsın. (aslında bu string bir kod parçası olacak)
fonksiyonumuz birkaç şeyi kontrol edecek:
kod "def" kelimesini(keyword) içermeli
eğer yoksa "missing def" ifadesini dönmeli

kod : sembolü(iki nokta üst üste) içermeli
eğer yoksa "missing :" ifadesini dönmeli

kod parametre listesi için ( ve ) içermeli(parantez açma ve kapatma işaretleri)
eğer yoksa "missing paren" ifadesini dönmeli

kod () içermeli(parantez açma ve kapatma işaretleri)
eğer yoksa "missing param" ifadesini dönmeli

kod girinti için dört adet boşluk içermeli
eğer yoksa "missing indent" ifadesini dönmeli

kod "validate" ifadesi içermeli
eğer yoksa "wrong name" ifadesini dönmeli

kod return ifadesi(return statement) içermeli
eğer yoksa "missing return" ifadesini dönmeli

If all these conditions are satisfied, your code should return True.
Here comes the twist: your solution must return True when validating itself.
Eğer tüm bu gereklilikler sağlanmışsa fonksiyon True dönmelidir.
yani çözümünüz kendini onaylarken True dönmelidir:)

"""


def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True
