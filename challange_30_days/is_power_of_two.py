"""
Berilgan sonni ikkini darajasimi yoki yo'qmi tekshirish
"""

"""
Logikasi:
    1) misol uchun 64 ni olaylik va ikkilik sanoq sistemasiga o'tkazaylik 64 = 2 ** 8 darajasi bu esa 8 chi indexdagi son 
    1 ga teng bo'ladi qolgan yetti ta indexdagi sonlar 0 bo'ladi (100000000)
    2) 8ni olaylik bu 2 ning uchinchi darajasi bu degani uchinchi indexdagi son 1 bo'ladi qolgan 2 tasi 0 bo'ladi (1000)
    3) 14 ni olaylik bu 8+4+2 yani 2 ning uchinchi darajasi + 2 ning ikkinchi darajasi + 2 ning birinchi darajasi (111)
    Xulosa:
        agar ikkining darajasi bo'lsa uni bitta bir qatnashadi qolgani nol bo'ladi shundan bilib olsak bo'ladi
"""


def is_power_of_two(num: int) -> bool:
    bit_count = 0
    while num != 0:
        bit_count += num & 1
        num = num >> 1

    return bit_count == 1

print(is_power_of_two(16))


