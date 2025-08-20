"""
n ga n bo'lgan shaxmat doskasi berilgan va berilgan savol rux ni nechta o'rincda joylashtirish mumkin va ruxlar bir biriga hujum qilolmasin
"""
from math import factorial

"""
yechim:
    R * *
    * * R
    * R *
    birinchi qatorda istalgan joyiga qo'ysa bo'ladi yani n ta o'ringa, ikkinchi qatorga  endi birinchi qatorga qo'ygan 
    joyimizga qo'yolmaymiz sababi bir birini uroladi, demak n-1 ta joyga qo'ysa bo'ladi, 3-qatorga esa birinchi va 
    ikkinchi qatorga qo'ygan joyga qo'yolmaymiz demak n-3 bo'ladi
    Ya'ni: n*(n-1)*(n-1)=n!
"""

def Solution(num :int):
    return factorial(num)

print(Solution(4))