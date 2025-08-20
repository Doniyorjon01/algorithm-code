"""
palindromlikka tekshirish yani bir so'zni oldidan ham orqadan ham o'qiganda bir xil chiqishi
masalan:
    kiyik = True
    aka = True
    maymun = False
"""


# def is_palindrome(word: str) -> bool:
#     return word == word[::-1]
"""
bu logika ham to'g'ri yani bizga bitta so'z berilgan uni har bir harfini tekshirib chiqamiz uning uchun bizni dasturmiz 
yana bitta string uchun xotiradan joy ajratadi.  shunday qilib ikkita stringni har bir elementini taqqoslab chiqadi 
bu esa xotiradan O(n) foydalanish 
vaqtdan esa O(2n) yutqazish sababi bir marta joy ajratadi, keyin tekshirishga ham vaqt ketadi
"""




"""
bu usulda esa ikkita o'zgaruvxhi ochamiz integer uchun yani mingta element bo'lsa ham 3 ta element bo'lsa ham faqatgina 2 ta joy ajratadi shuning uchun 
xotira - O(1), vaqt esa - o(n/2) sababi so'zni yarmigacha boramiz low birinchi yarmigacha boradi high orqadan yarmigacha keladi yani vaqt ikki marta qisqaradi
"""
def is_palindrome(word: str) -> bool:
    low, high = 0, len(word) - 1
    while low < high:
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1
    return True

print(is_palindrome("kiyik"))