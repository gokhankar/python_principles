"""
Min-maxing
Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and 
smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.
"""
"""
largest_difference adında bir fonksiyon yazın, bu fonksiyon tek parametre alsın ve 
bu parametre sayılardan oluşan bir liste olsun.
Fonksiyonumuz listedeki en büyük ve en küçük sayı arasındaki farkı hesaplayıp dönsün.

mesela, largest_difference([1, 2, 3]) çağrıldığında, fonksiyon 2 dönmelidir, çünkü
3-1=2 dir.

Listedeki sayılarımız ise -100 den küçük olmasın ve 100 den büyük olmasın.
"""


# def largest_difference(myList):
#     return sorted(myList)[-1] - sorted(myList)[0]


# print(largest_difference([1, 2, 3]))


# short solution
def largest_difference(numbers):
    return max(numbers) - min(numbers)

# naive solution


def largest_difference(numbers):
    smallest = 100
    for n in numbers:
        if n < smallest:
            smallest = n

    largest = -100
    for n in numbers:
        if n > largest:
            largest = n

    difference = largest - smallest
    return difference
