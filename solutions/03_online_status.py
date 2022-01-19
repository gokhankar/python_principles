"""
Online status
The aim of this challenge is, given a dictionary of people's online status,
to count the number of people who are online.
For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.
Write a function named online_count that takes one parameter. 
The parameter is a dictionary that maps from strings of names to the string 
"online" or "offline", as seen above.
Your function should return the number of people who are online.
"""
"""
Bu bölümde size kişilerin online durumlarını gösteren bir dictionary verilecektir.
Ve sizden toplamda online olan kişilerin sayısı istenecektir.
Mesela aşağıdaki dictionary i inceleyin:
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
bu örnek için online kişi sayısı 2 dir.
online_count adında tek parametre alan bir fonksiyon yazın.
Parametre yukarıdaki gibi isimlere göre "online" veya "offline" olma durumlarını gösterecektir.
Sizin yazdığınız fonksiyon da, toplam "online" kişi sayısını dönmelidir.
"""


def online_count(myDict):
    counter = 0
    for i, j in myDict.items():
        if j == "online":
            counter += 1
    # print(counter)
    return counter


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
online_count(statuses)
