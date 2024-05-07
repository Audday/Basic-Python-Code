


totHari = 485
hari = totHari

tahun = (hari//360)
hari %= 360

bulan = (hari//30)
hari %= 30

minggu = (hari//7)
hari %= 7

print (str(totHari) + ' Hari adalah')
print ('{} Tahun' .format(tahun))
print ('{} Bulan' .format(bulan))
print ('{} Minggu' .format(minggu))
print ('{} Hari' .format(hari))

print (str(totHari) + ' Hari Adalah ')
print (str(tahun)+ ' Tahun ' + str(bulan) +  ' Bulan ' + str(minggu) +  ' Minggu ' + str(hari) + ' Hari ')

