"""
Berilgan sooni teskari qilib beradigan algoritm yozishimiz kerak
Misol uchun:
154 -> 451
710 -> 17
"""
from unittest import result

"""
logikasi quidagicha bo'ladi:
berilgan son 17 bo'lsin
oxirgi raqamni olamiz va sonni o'zidan, olgan raqamimizni o'chirib tashlaymiz  shift(//) bilan va undan oldingi raqamga o'tamiz
biz yettini olgan edik endi uni oldiga birni qo'shishimiz kerak uning uchun 7 * 10 = 70 bo'ladi ana endi boyagi birni 70 ga qo'shsak bo'ladi 
va natija 71 bo'ladi yani 17 ni teskarisi
"""

def reverse_digit(num: int):
    result = 0
    if num == 0:
        print(0)
        return
    while num != 0:
        result *= 10
        digit = num % 10
        result += digit
        num //= 10
    return result

print(reverse_digit(710))
