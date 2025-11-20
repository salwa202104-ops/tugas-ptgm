class alatmusik :
     pass
     
alatmusik1 = alatmusik()
alatmusik2 = alatmusik()

print(type(alatmusik1))
print(type(alatmusik2))

alatmusik1 = alatmusik()
alatmusik1.nama = "gitar" 
alatmusik1.jenis = "string"
alatmusik1.bahan = "kayu"
alatmusik1.cara_main = "dipetik"
alatmusik1.warna = "coklat"

alatmusik2 = alatmusik()
alatmusik2.nama = "drum" 
alatmusik2.jenis = "perkursi" 
alatmusik2.bahan = "bambu"
alatmusik2.cara_main = "dipukul"
alatmusik2.warna = "putih"

print(alatmusik1.nama)
print(alatmusik1.jenis)
print(alatmusik1.bahan)
print(alatmusik1.cara_main)
print(alatmusik1.warna)
print(alatmusik2.nama)
print(alatmusik2.jenis)
print(alatmusik2.bahan)
print(alatmusik2.cara_main)
print(alatmusik2.warna)