# Nama  : Nurma Sari Laras Aji
# NIM   : 20051397062
# Kelas : MI2020B

class hasil :
    def hitung (angka):
        print (' ')
        print ('Jari-jari     : ', angka.bil1)
        print ('Tinggi tabung : ', angka.bil2)
        print (' ')
        print ('Volume Tabung :', (22/7*angka.bil1*angka.bil1*angka.bil2))
        print (' ')

        
class nilai(hasil) :
    def __init__(self):
        self.bil1 = int(input('Masukan Jari-jari     : '))
        self.bil2 = int(input('Masukan Tinggi tabung : '))
        



coba = ('y')
while coba == ('y') or coba == ('Y') :
    print ("Menghitung Volume Tabung")
    print (' ')
    
    objek = nilai()
    objek.hitung()
    print(' ')
    coba = input('Mau Menghitung Lagi : ')
    if coba == ('y') or coba == ('Y') :
        print (' ')
        continue
    elif coba == ('n') or coba == ('N') :
        print ('Terima Kasih')
        break
    else :
        print ('Pilihan yang Anda Masukan Salah')
        break