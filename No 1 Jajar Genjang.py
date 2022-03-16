# Nama  : Nurma Sari Laras Aji
# NIM   : 20051397062
# Kelas : MI2020B

class hasil :
    def hitung (angka):
        print (' ')
        print ('panjang sisi a mendatar : ', angka.bil1)
        print ('panjang sisi b mendatar : ', angka.bil2)
        print ('Tinggi                  : ', angka.bil3)
        print (' ')
        print ('Luas Jajargenjang     :', angka.bil1*angka.bil3)
        print ('Keliling Jajargenjang :', 2* (angka.bil1+angka.bil2))
        
        
class nilai(hasil) :
    def __init__(self):
        self.bil1 = int(input('Masukan Panjang sisi a mendatar : '))
        self.bil2 = int(input('Masukan Panjang sisi b mendatar : '))
        self.bil3 = int(input('Masukan Tinggi                  : '))


coba = ('y')
while coba == ('y') or coba == ('Y') :
    print ("Menghitung Luas Dan Keliling Jajar Genjang")
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