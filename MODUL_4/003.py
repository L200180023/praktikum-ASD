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

def cariUangSakuTerkecilObject(list):
    temp = [list[0]]
    for i in list[1:]:
        if i.uangSaku < temp[0].uangSaku:
            temp = [i]
        elif i.uangSaku == temp[0].uangSaku:
            temp.append(i)
    return temp

a = cariUangSakuTerkecilObject(Daftar)
print(a)
