print ('\n\n================== QUESTION 8 (EXTRA) ====================\n\n')\
    
    
# Input bulan kelahiran
month = input("Masukkan bulan kelahiran (January - December): ").capitalize()
day = int(input("Masukkan tanggal kelahiran: "))


# Menentukan zodiak
if month == 'January':
    if day < 20:
        zodiac = "Capricorn"
    else:
        zodiac = "Aquarius"
elif month == 'February':
    if day < 19:
        zodiac = "Aquarius"
    else:
        zodiac = "Pisces"
elif month == 'March':
    if day < 21:
        zodiac = "Pisces"
    else:
        zodiac = "Aries"
elif month == 'April':
    if day < 20:
        zodiac = "Aries"
    else:
        zodiac = "Taurus"
elif month == 'May':
    if day < 21:
        zodiac = "Taurus"
    else:
        zodiac = "Gemini"
elif month == 'June':
    if day < 21:
        zodiac = "Gemini"
    else:
        zodiac = "Cancer"
elif month == 'July':
    if day < 23:
        zodiac = "Cancer"
    else:
        zodiac = "Leo"
elif month == 'August':
    if day < 23:
        zodiac = "Leo"
    else:
        zodiac = "Virgo"
elif month == 'September':
    if day < 23:
        zodiac = "Virgo"
    else:
        zodiac = "Libra"
elif month == 'Oktober':
    if day < 23:
        zodiac = "Libra"
    else:
        zodiac = "Scorpio"
elif month == 'November':
    if day < 22:
        zodiac = "Scorpio"
    else:
        zodiac = "Sagittarius"
elif month == 'December':
    if day < 22:
        zodiac = "Sagittarius"
    else:
        zodiac = "Capricorn"
else:
    zodiac = "Bulan tidak valid"

print("Zodiak Anda adalah:", zodiac)