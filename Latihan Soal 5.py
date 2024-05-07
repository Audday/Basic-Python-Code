import math

h = float(input("Masukan Tinggi Silinder: "))
r = float(input("Masukan Jari-Jari Silinder: "))


luasPermukaan = (2 * math.pi * r * (r + h))
volume = (math.pi * (r**2) * h)

print(f"Luas Permukaan Cylinder Dengan Tinngi {h} dan Jari - Jari {r} adalah {luasPermukaan} ")
print(f"Volume Cylinder Dengan Tinggi {h} dan Jari - Jari {r} adalah {volume} ")