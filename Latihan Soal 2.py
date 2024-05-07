import math

r = int(input("Masukkan nilai jari-jari lingkaran: "))
satuan = str(input("Masukan Satuan cm/m/km: "))

diameter = 2 * r
luas = math.pi * (r ** 2)
keliling = 2 * math.pi * r


print(f"Lingkarang Tersebut Memiliki Jari - Jari lingkaran: {r} {satuan}")
print(f"Lingkarang Tersebut Memiliki Diameter lingkaran: {diameter} {satuan}")
print(f"Lingkarang Tersebut Memiliki Luas lingkaran: {round(luas,2)} {satuan}^2")
print(f"Lingkarang Tersebut Memiliki Keliling lingkaran: {round(keliling,2)} {satuan}")


luas_setengah_lingkaran = luas / 2
keliling_setengah_lingkaran = (keliling + diameter) / 2

print(f"\nLuas setengah lingkaran: {luas_setengah_lingkaran:.3f} {satuan}^2")
print(f"Keliling setengah lingkaran: {keliling_setengah_lingkaran:.2f} {satuan}")


