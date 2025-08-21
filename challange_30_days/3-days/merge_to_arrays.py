"""
Ikkita arrayda tartiblangan sonlar bor. Ularni tartiblanga ko'rinishda birlashtiring.
Misol uchun:
    merge_to_arrays([4, 5], [3]) -> [3, 4, 5]
    merge_to_arrays([1, 3], [2, 6]) -> [1, 2, 3, 6]
"""

"""
4 6 9 10

    *
2 5 12 

2 4 5 6 9 10 12

vaqt -> n+m oladi sababi ikkita arrayni ham ko'rib chiqishimiz kerak
xotira -> n+m sababi n va m o'zgaruvchilari bor biz yani ikki array

"""

# def merge_to_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
#     i = j = 0
#     n = len(arr1)
#     m = len(arr2)
#     result = []
#     while i < n and j < m:
#         if arr1[i] < arr2[j]:
#             result.append(arr1[i])
#             i += 1
#         else:
#             result.append(arr2[j])
#             j += 1
#
#     while i < n:
#         result.append(arr1[i])
#         i += 1
#
#     while j < m:
#         result.append(arr2[j])
#         j += 1
#
#     return result
#
# print(merge_to_arrays([4, 5], [3]))

#  Yuqoridagi yozilgan kodda result uchun bitta alohida hotiradan joy ajratadi endi shu joyni ham ishlatmaslik iloji bor u pasdagi yozilgan kodda

from typing import Iterable


def merge_to_arrays(arr1: list[int], arr2: list[int]) -> Iterable[int]:
    i = 0
    j = 0
    n = len(arr1)
    m = len(arr2)

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            yield arr1[i]
            i += 1
        else:
            yield arr2[j]
            j += 1

    while i < n:
        yield arr1[i]
        i += 1
    while j < m:
        yield arr2[j]
        j += 1

    return

print(list(merge_to_arrays([4, 5], [1, 3, 10])))

"""
ikkinchi yozilgan kodda umuman joy egalamaydi yani qo'shimcha joy. Constant extra space. Natijani qayergadir saqlamaydi shunchaki chiqarib beradi
"""