"""
Middle letter
Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return ""
"""
"""
mid() isimli bir fonksiyon yazın. 
parametre olarak bir string alsın.
fonksiyon çalıştırılınca ortadaki harfi dönmeli.
Eğer orta karakter yoksa, yani string çift harfliyse, fonksiyon boş string dönmeli.

Mesela mid("abc") fonksiyonu "b" dönmeli,
mid("aaaa") fonksiyonu "" dönmeli.
"""


def mid(text):
    if len(text) % 2 == 1:
        return text[int((len(text) - 1) / 2)]
    else:
        return ""


mid("abc")
