class Mhs(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

h0 = Mhs("Fahri", 23, "Karanganyar", 240000)
h1 = Mhs("Edi", 2, "Jumantono", 230000)
h2 = Mhs("Bachtiar", 31, "Karanganyar", 250000)
h3 = Mhs("Tito", 7, "Surakarta", 235000)
h4 = Mhs("Galih", 5, "Wonogiri", 240000)
h5 = Mhs("Satria", 1, "Wonogiri", 250000)
h6 = Mhs("Auzan", 5, "Karanganyar", 245000)
h7 = Mhs("Rifqi", 8, "Karanganyar", 245000)
h8 = Mhs("Rizzki", 32, "Surakarta", 245000)
h9 = Mhs("Afrizal", 22, "Surakarta", 270000)
h10 = Mhs("Pandu", 27, "Surakarta", 265000)

Daftar = [h0, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]

def binSeMass(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2, 4, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
print(binSeMass(kumpulan, 6))
