"""
1 dan N gacha bo'lgan toq sonlar yig'indisini O(1) da hisoblang
O(1) da hisoblang degani hamma sonlar uchun bir xil vaqtda hisoblansiz degani yani 10 gacha bo'lgan sonlar uchun boshqa vaqt
1000 gacha bo'lgan sonlar uchun boshqa vaqt bo'lmasin degani.
Masalan:
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a[3]) bu holatda agar a ning qiymati million gacha bo'lsa ham hamma vaqt bir xil vaqtda malumot olib keladi.
"""
import time
import timeit


def sum_of_odd_numbers(num: int):
    k = (num + 1) // 2
    return k * k


# start = time.time()
execution_time = timeit.timeit(lambda: sum_of_odd_numbers(1000000000), number=1000) # bunda number ga necha marta hisoblashlaigini aytish mumkin yani aniqroq vaqtni ko'rish uchun
print(sum_of_odd_numbers(1000000000))
print(execution_time)
# end = time.time()
# print(end - start) bu faqat bir marta ishlab to'xtaydi
