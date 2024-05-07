
#NOTE
#Menggunakan Fungsi DEF

#def swap_first_two_chars(word1, word2):
    # Membuat kata-kata baru dengan menukar dua karakter pertama
#    new_word1 = word2[:2] + word1[2:]
#    new_word2 = word1[:2] + word2[2:]
#    return new_word1, new_word2

#def main():
#    kata1 = input("Masukkan kata pertama: ")
#    kata2 = input("Masukkan kata kedua: ")
    
#   kata1_baru, kata2_baru = swap_first_two_chars(kata1, kata2)
#  print(kata1_baru, kata2_baru)

#main()


print ("\n========================== CODE KE 2 =======================\n")

kata1 = input("Masukan kata pertama: ")
kata2 = input("Masukan kata kedua: ")

kata_baru1 = kata2[:3] + kata1[3:]
kata_baru2 = kata1[:3] + kata2[3:]

print(kata_baru1, kata_baru2)


