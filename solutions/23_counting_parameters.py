"""
Counting parameters
Define a function param_count that takes a variable number of parameters. 
The function should return the number of arguments it was called with.

For example, param_count() should return 0, while param_count(2, 3, 4) 
should return 3.

"""
"""
param_count adında bir fonksiyon yazın. Bu fonksiyon değişken sayıda parametre
alabilsin. Ve fonksiyon bize çağrıldığı parametrelerin sayısını dönsün.

Mesela, param_count() çağrıldığında 0 dönsün. 
param_count(2, 3, 4) çağrıldığında 3 dönsün.

"""


def param_count(*args):
    return len(args)
