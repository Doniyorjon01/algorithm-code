"""
bizga list berilgan va target berilgan. listni ischidagi ikkita sonni qo'shganda targetni hosil qilsa True qaytarsin aks holda False qaytarsin
masalan:
    to_sum([2, 7, 11, 15], 9) -> True 2+7
    to_sum([2, 7, 11, 15], 8) -> False
"""

"""
bitta compliments degan dect yaratvolamiz u bizda  key (target-num)	value (index) 
key       value
7	      0
2	      1
-2	      2
-6	      3
nolinchi indexdagi raqamga 7 kerak yani 7=9-2 key=(target-num) 
keyin for da aylanamiz yani listni index va num larini aylanamiz keyin compliments ga saqlaymiz target-num = index yani birorta indexdagi raqam bizga kerak bo'lgan ramaga teng bo'lsa 

ikkinchi forda esa uni tekshiramiz agar compliments da num  bo'lsa va listni ichidagi usha num ni o'zini olmasligimiz kerak huddi futbolchilar misolini
oladigan bo'lsak futbolchilar o'zidan boshqalar bilan so'rashadi o'zi bilan o'zi so'rashmaydi 
"""


def two_sum_hash_table(arr: list[int], target: int) -> bool:
    compliments = {}
    for index, num in enumerate(arr):
        compliments[target - num] = index

    for index, num in enumerate(arr):
        if num in compliments and compliments[num] != index:
            return True

    return False

print(two_sum_hash_table([2, 7, 11, 15], 9))