# NOTE
#Modul 1 File 5
lyric = ('Cicak Cicak Di Dinding \n\t Diam Diam Merayap \n\t\t Datang Seekor Nyamuk \n\t\t\t HAP HAP HAP \nLalu Di Tangkap \n\t YEAY!')

print (lyric)

# NOTE 
# \n = Enter 
# \t = Tab 
# \b = Backslash

print ('='*80)
print ('\n=================================Contoh Code Ke 2===============================\n')
print ('='*80)


lyrics = '''Cicak Cicak Di Dinding
    Diam Diam Merayap
        Data Seekor Nyamuk
            Hap Hap Hap!
Lalu Di Tangkap
    YEAY!'''

# NOTE
# Apapun yang ada di ''' ... ''' isinya akan ter-record automatically, termasuk Spasi, Enter, dan Tab

print(lyrics)

#NOTE
#Fungsi FORMAT

nilai = 100
usia = 22
name = 'Dio'

print (f'Nama Saya Adalah {name}, Usia Saya {usia}, Tahun Ini Saya Berumur {usia+1}, Saya Mendapatkan Nilai {nilai}')
print ("Nama Saya Adalah {}, Usia Saya {}, Tahun Ini Saya Berumur {}, Saya Mendapatkan Nilai {} " .format(name, usia, usia+1, nilai))

#NOTE
#FUNGSI INPUT
name = input('Masukkan Nama Anda : ')
age = input('Masukkan Usia Anda : ')
uang = float(input('Masukkan Jumlah Uang: '))

print (f'Nama Saya Adalah {name}, Usia Saya {age}, Tahun Ini Saya Berumur {int(age)+1}, Uang saya {uang} juta')

