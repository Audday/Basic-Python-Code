#Question 2
print ('================== QUESTION 2 ====================')

# massa = float(raw_input('Masukan Massa (kg): '))
# tinggi = float (raw_input('Masukan Tinggi (cm): '))

#NOTE
#GUNAKAN INI UNTUK PYTHON 3.12
massa = float(input('Masukan Massa (kg): '))
tinggi = float (input('Masukan Tinggi (cm): '))

#FORMULA
kon_tinggi = tinggi/100

print ('Massa {} kg dan TInggi {} m'.format(massa, kon_tinggi))
IMT = massa / kon_tinggi**2

if (IMT < 18.5) :
    print('{}, Berat Badan Kurang'.format(IMT))
elif (IMT >= 18.5 and IMT <= 24.9):
    print ('{}, Berat Badan Ideal'.format(IMT))
elif (IMT >= 25.0 and IMT <= 29.9) :
    print ('{}, Berat Badan Berlebih'.format(IMT))
elif (IMT >= 30.0 and IMT <= 39.9) :
    print ('{}, Berat Badan Sangat Berlebih'.format(IMT))
else:
    print ('{}, Obesitas'.format())
    
    
print ('\n\n================== QUESTION 3 ====================\n\n')

# apel = int(raw_input('Masukan Jumlah Apel: '))
# jeruk = int(raw_input('Masukan Jumlah Jeruk: '))
# anggur = int(raw_input('Masukan Jumlah Anggur: '))

# NOTE
# GUNAKAN INI UNTUK PYTHON 3.12
apel = int(input('Masukan Jumlah Apel: '))
jeruk = int(input('Masukan Jumlah Jeruk: '))
anggur = int(input('Masukan Jumlah Anggur: '))


#FORMULA
cal_apel = apel * 10000
cal_jeruk = jeruk * 15000
cal_anggur = anggur * 20000

total = cal_apel + cal_jeruk + cal_anggur

print('''Detail Belanja
Apel: {} x 10000 = {}
Jeruk: {} x 15000 = {}
Anggur: {} x 20000 = {}

Total = {}
'''.format(apel, cal_apel, jeruk, cal_jeruk, anggur, cal_anggur, total))

# uang = int(raw_input('Masukan Jumlah Uang: '))

#NOTE
#GUNAKAN INI UNTUK PYTHON 3.12
uang = int(input('Masukan Jumlah Uang: '))
kurang = total - uang
kembalian = uang - total

if (uang < total) :
    print('''Transaksi anda di batalkan
Uangnya Kurang Sebesar: {}''' .format(kurang))
elif (uang > total) :
    print ('''Terima Kasih
Uang Kembalian anda: {}'''.format(kembalian))
else :
    print('Terima Kasih')


print ('\n\n================== QUESTION 8 (EXTRA) ====================\n\n')\
    
    
# Input bulan kelahiran
month = input("Masukkan bulan kelahiran (1-12): ")
day = int(input("Masukkan tanggal kelahiran: "))


# Menentukan zodiak
if month == 1:
    if day < 20:
        zodiac = "Capricorn"
    else:
        zodiac = "Aquarius"
elif month == 2:
    if day < 19:
        zodiac = "Aquarius"
    else:
        zodiac = "Pisces"
elif month == 3:
    if day < 21:
        zodiac = "Pisces"
    else:
        zodiac = "Aries"
elif month == 4:
    if day < 20:
        zodiac = "Aries"
    else:
        zodiac = "Taurus"
elif month == 5:
    if day < 21:
        zodiac = "Taurus"
    else:
        zodiac = "Gemini"
elif month == 6:
    if day < 21:
        zodiac = "Gemini"
    else:
        zodiac = "Cancer"
elif month == 7:
    if day < 23:
        zodiac = "Cancer"
    else:
        zodiac = "Leo"
elif month == 8:
    if day < 23:
        zodiac = "Leo"
    else:
        zodiac = "Virgo"
elif month == 9:
    if day < 23:
        zodiac = "Virgo"
    else:
        zodiac = "Libra"
elif month == 10:
    if day < 23:
        zodiac = "Libra"
    else:
        zodiac = "Scorpio"
elif month == 11:
    if day < 22:
        zodiac = "Scorpio"
    else:
        zodiac = "Sagittarius"
elif month == 12:
    if day < 22:
        zodiac = "Sagittarius"
    else:
        zodiac = "Capricorn"
else:
    zodiac = "Bulan tidak valid"

print("Zodiak Anda adalah:", zodiac)

