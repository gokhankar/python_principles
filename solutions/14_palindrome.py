"""
Palindrome
A string is a palindrome when it is the same when read backwards.

For example, the string "bob" is a palindrome. So is "abba". 
But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string
 as its parameter. Your function should return True if the string 
 is a palindrome, and False otherwise.
"""
"""
Palindrom: tersten okunuğunda, düzden okunmasıla aynı olan ifadeler.
Mesela, "bob" bir plandrome dur. "abba" da öyle. 
Ama "abcd" değildir. Çünkü "abcd" != "dcba"
Türkçe palindrome "ey edip adanada pide ye"
Şimdi, palindrome adında bir fonksiyon yazın. Tek bir string parametre alsın.
Fonksiyonunuz string bir palindrome ise True, yoksa False dönsün.

"""


def palindrome(str):
    return str == str[::-1]

# iterative solution:
# keep chopping off the head and tail of the string,
# and compare the two. If they are not equal, it's
# not a palindrome. Stop when the string gets too short.


def palindrome(string):
    while len(string) > 1:
        head = string[0]
        tail = string[-1]
        string = string[1:-1]
        if head != tail:
            return False
    return True

# recursive solution: equivalent to the above.


def palindrome(string):
    if len(string) < 2:
        return True
    return string[0] == string[-1] and palindrome(string[1:-1])

# smarter solution:
# check if reversing the string gives the same string.


def palindrome(string):
    return string == string[::-1]
