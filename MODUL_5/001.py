class Mahasiswa(object):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        
def BubbleSort(value):
    for passnum in range(len(value)-1,0,-1):
        for i in range(passnum):
            if value[i]>value[i+1]:
                temp = value[i]
                value[i] = value[i+1]
                value[i+1] = temp

        
c0 = Mhs("Fahri", 23, "Karanganyar")
c1 = Mhs("Edi", 2, "Jumantono")
c2 = Mhs("Bachtiar", 31, "Karanganyar")
c3 = Mhs("Tito", 7, "Surakarta")
c4 = Mhs("Galih", 5, "Wonogiri")
c5 = Mhs("Satria", 1, "Wonogiri")
c6 = Mhs("Auzan", 5, "Karanganyar")
c7 = Mhs("Rifqi", 8, "Karanganyar")
c8 = Mhs("Rizzki", 32, "Surakarta")
c9 = Mhs("Afrizal", 22, "Surakarta")
c10 = Mhs("Pandu", 27, "Surakarta")

DaftarAngka = [c0.NIM,c1.NIM,c2.NIM,c3.NIM,c4.NIM,c5.NIM,c6.NIM,c7.NIM,c8.NIM,c9.NIM,c10.NIM]
BubbleSort(DaftarAngka)
print(DaftarAngka)
