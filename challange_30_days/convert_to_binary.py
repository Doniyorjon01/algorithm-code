"""
bizga son berilgan uni ikkilik sanoq sistemasiga o'tkazishimiz kerak
bunign uchun sonni avval 2 ga qoldiqli bolamiz(%) shunda bizga qoldig'ini olib ber keyin sonni biz shift qilib butun qismini olamiz
13 % 2 = 1 bu birni saqlab qo'yamiz
13 // 2 = 6
6 % 2 = 0 buni ham saqlaymiz
6 // 2 = 3
3 % 2 = 1 buni ham saqlaymiz
3 // 2 = 1
1 % 2 = 1 buni ham saqlaymiz
1 // 2 = 0
natija = 1011
"""

def convert_to_binary(num: int) -> str:
    result = ""
    while num != 0:
        digit = num % 2
        result += str(digit)
        num = num // 2

    return result

print(convert_to_binary(13))