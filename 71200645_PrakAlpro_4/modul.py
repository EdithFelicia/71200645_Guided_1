# nama = input("Masukkan nama: ")
# hobi = input("Masukkan hobi: ")
# print("Hallo! Saya", nama, "\nHobi saya ", hobi, "\nSelamat pagi!")

# def kurang(a, b):
#     hasil = a - b
#     return hasil

# c = kurang(20, 15)
# print(c)

# RETURN VALUE
# def print_twice(message):
#     print(message)
#     print(message)
#     return message

# print(print_twice("Sin is unbelief in Jesus Christ"))

# def hitung_belanja(belanja, diskon=0):
#     bayar = int(belanja - (belanja * diskon)/100)
#     return bayar

# print(hitung_belanja(100000))
# print(hitung_belanja(100000, 10))
# print(hitung_belanja(100000, 50))
# print(hitung_belanja(diskon = 20, belanja = 120000))
# print(hitung_belanja(120000, 20))

# kurang = lambda a, b: a - b
# print(kurang(15, 12))

# def tagihan_listrik(pemakaian, golongan=3):
#     bayar = 0
#     pemakaian_100 = 100 if pemakaian > 100 else pemakaian
#     pemakaian_100_lebih = pemakaian - pemakaian_100
#     if golongan == 1:
#         bayar = pemakaian_100 * 1500 + pemakaian_100_lebih * 2000
#     elif golongan == 2:
#         bayar = pemakaian_100 * 2500 + pemakaian_100_lebih * 3000
#     elif golongan == 3:
#         bayar = pemakaian_100 * 4000 + pemakaian_100_lebih * 5000
#     elif golongan == 4:
#         bayar = pemakaian_100 * 5000 + pemakaian_100_lebih * 7000
#     return bayar

# print(tagihan_listrik(130))
# print(tagihan_listrik(80,4))
# print(tagihan_listrik(golongan=1, pemakaian=175))

# Lambda memakan sedikit ruang

def abc(a, b, c):
    a = b * c
    b = c // a
    c = a - b
    
angka_1 = 60
angka_2 = 100
angka_3 = 85
abc(angka_1, angka_2, angka_3)
print(angka_1)
print(angka_2)
print(angka_3)