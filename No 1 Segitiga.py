# Nama  : Nurma Sari Laras Aji
# NIM   : 20051397062
# Kelas : MI2020B

class hasil :
    def hitung (angka):
        print (' ')
        print ('Panjang alas          : ', angka.bil1)
        print ('Panjang sisi miring a : ', angka.bil2)
        print ('Panjang sisi miring b : ', angka.bil3)
        print ('Tinggi                : ', angka.bil4)
        print (' ')
        print ('Luas Segitiga     :', (angka.bil1*angka.bil4)*1/2)
        print ('Keliling Segitiga :', angka.bil1+angka.bil2+angka.bil3)
        
class nilai(hasil) :
    def __init__(self):
        self.bil1 = int(input('Masukan Panjang alas          : '))
        self.bil2 = int(input('Masukan Panjang sisi miring a : '))
        self.bil3 = int(input('Masukan Panjang sisi miring b : '))
        self.bil4 = int(input('Masukan Tinggi                : '))


coba = ('y')
while coba == ('y') or coba == ('Y') :
    print ("Menghitung Luas Dan Keliling Segitiga")
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