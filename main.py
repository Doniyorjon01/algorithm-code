# a=10110
# print(a>>3)
'''
shallow copy tashqi obyekt o'zgaradi ichki obyekt esa eski manzilda qoladi
deep copy tashqi obyekt ham ichki obyekt ham eski o'zgaradi

'''
# import copy
#
# list1 = [[1, 2], [3, 4]]
# shallow = copy.copy(list1)
#
# print(id(list1), id(shallow))
# print(id(list1[0]), id(shallow[0]))
#
#
# deep = copy.deepcopy(list1)
#
# print(id(list1), id(deep))
# print(id(list1[0]), id(deep[0]))

'''
== qiymatlarni tekshiradi
is obyektning xotiradagi manzilini taqqoslaydi
'''

"""
*args o'zida oddiy tartib bo'yicha berilgan qiymatlar qabul qiladi yani o'zida tuple sifatida saqlaydi
*kwargs dict qiymatlarni qabul qiladi
"""

"""
iterator pythonda iterable obyektlar ustida for bilan aylanib chiqish uchun ishlatiladi
iterator bu __iter__() va __next__() metrolariga ega bo'lgan obyekt
har safar __next__() chaqirilganda keyin elemenni olib keladi oxirida StopIteration xatosini beradi

generator iterator yaratishni soddalshagan usuli 
odatda yield kalit so'zi bilan yaratiladi
generator xotiradan tejamkor foydalanadi chunki hamma elemntlarni birdaniga yaratmaydi kerak bo'lganda birma bir yaratadi(lazy evaluation)

"""

"""
decorator funksiyadagi xatti-harakatini kodni o'zgartirmasdan kengaytirish va o'zgartrish imkonini beradi
"""

"""
obyekt yaratish:
    a = [1, 2, 3]
    a list uchun  RAM da joy ajratildi
    bu obyektni python HEAP hotirasiga joylashtiradi
    
reference counting 
    har bir obyectga o'zgaruvchi necha marta foydalanayotganini tekshiradi
    a = [1, 2, 3]
    b = a
    endi [1, 2, 3] obyekt ni ikkita o'zgaruvchi ishlatyapti
    
garbage collector
    agar reference count 0 ga teng bo'lsa obyekt kerak emas deb hisoblarnib python uni xotiradan ovtomatic o'zchirb tashlaydi
    
HEAP operatsion tizim tomonidan boshqariadigan xotira. dastur ishlashi davomida obyektlarni dinamic ajratish uchun ishlatiladi

RAM komputer operativ xotirasi yani katta omborxona. ramni ichida stack va heap kabi bo'limlar bor. biz yaratgan obyektlar shular uchida saqlanadi
misol uchun biz bir obyekt yaratsak uni python heap hotirada saqlaydi stack esa funksiya chqirilganda vaqtinchalik o'zgaruvchilarni shu yerga yozadi. juda tez ishlaydi, kichik hotira ajratadi
heap bilan stackni farqi 
heap katta obyetklar ni saqlaydi. hajmi ham katta bo'ladi sekin ishlaydi va tartibsiz joylahtiradi va uni garbage collector nazorat qiladi. stackni esa hech nima nazorat qilmaydi o'zi o'chib ketadi
"""

"""
asyncio bu pythonda asinxron dastrurlash uchun ishlatiladi. 
"""

arr = list(input().replace(" ", "").split(","))
summ = 0
for i in arr:
    if i == i:
        summ += 1
    if i != 2:
        print(i)
    print(summ)
