#def ganti_karakter(string, karakter_pengganti):
#    karakter_awal = string[0]
#    return karakter_awal + string[1:].replace(karakter_awal, karakter_pengganti)

#def main():
#    string_input = input("Masukkan Sebuah Kalimat: ")
#    karakter_pengganti = input("Masukkan Karakter Pengganti: ")
    
#    hasil = ganti_karakter(string_input, karakter_pengganti)
#    print(hasil)

#main()


print ("\n======================== CODE KE 2 =========================\n")

a = str(input("Masukan Sebuah Kalimat: "))
b = str(input("Masukan Karakter Pengganti: "))

karakter_awal = a[0] 
#{[0] = index} => Index artinya urutan dan selalu di mulai dari 0
#artinya mengambil huruf pertama dari sebuah kata
    # S A Y A _ M A N U S  I  A
    # 0 1 2 3 4 5 6 7 8 9 10 11
    # x[7] = N
    # x[:7] = SAYA_MA
    # x[1:] = AYA_MANUSIA
    # x[1:8] = AYA_MAN

hasil_kalimat = karakter_awal + a[1:].replace(karakter_awal, b)

print(hasil_kalimat)

print ("\n======================== CODE KE 3 =========================\n")

text = input('Masukan sebuah kalimat: ')
rep = input('Masukan karakter pengganti: ')
a = text[0]
ganti = text.replace(a, rep)
final = a+ganti[1:]
print(final)

print ("\n======================== CODE CONTOH =========================\n")

#NOTE
#Fungsi Replace

print ('='*80)
text = 'Ahmadio Hermanu'
print(text.replace('a', '@'))

print ('='*80)
text 

