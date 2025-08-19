"""
Berilgan sonni raqamllarini ekranga chiqaring
Misol uchun print(154) qilinganda:
4
5
1
"""
"""
description:
    154 % 10 = 4  (% oxirgi sonini olib beradi)
    154 / 10 = 15 (/ bo'lib butun qismini qaytaradi, yani qolgan qismini olib beradi)
    15 % 10 = 5
    15 / 10 = 5
    5 % 10 = 1
    5 / 10 = 1
    1 % 10 = 1
    1 / 10 = 0
    
logikasi shu ko'rinishda bo'ladi yani 154 ni 10 ga foizli bo'lganda oxirgi sonni olib beradi yani birinchi chiqishi 
kerak bo'lgan sonni keyin 154 ni (/) bo'lganda oxirgi sondan buyog'ini olib beradi yani 15 ni shu tariqa davom etadi
"""

def print_digit(num: int):
    if num == 0:
        print(0)
        return
    while num != 0:
        digit = num %10
        print(digit)
        num //= 10

print_digit(154)