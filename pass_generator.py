import random

sandi = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang = int(input("berapa panjang karakter untuk kata sandi"))
hasil = ""

for i in range(panjang):
    hasil += random.choice(sandi)
print("kata sandi yang di hasilkan adalah",hasil)
