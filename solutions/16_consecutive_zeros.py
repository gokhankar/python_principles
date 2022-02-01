"""
Consecutive zeros
The goal of this challenge is to analyze a binary string consisting 
of only zeros and ones. Your code should find the biggest number of 
consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, 
which is the string of zeros and ones. Your function should return the 
number described above.
"""
"""
bu challenge için amacımız sadece sıfır ve birlerden oluşan ikili(binary)
bir stringi analiz etmek. Yazdığımız kod string içindeki en uzun ardışık 
sıfır grubunu bulmalı ve kaç sıfırdan oluştuğunu saymalı.
Mesela  "1001101000110" için
en büyük ardışık sıfır sayısı 3 dür.
consecutive_zeros adında, sıfır ve birlerden oluşan tek bir string parametre 
alan bir fonksiyon yazın. Fonksiyonunuz yukarıda açıklanan sayıyı dönmeli.
"""


def consecutive_zeros(string):
    my_list = string.split("1")
    my_len_list = []
    for i in my_list:
        my_len_list.append(len(i))
    return max(my_len_list)

# naive solution


def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

# shorter solution


def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])
