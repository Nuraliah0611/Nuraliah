makanan = {"nasi","ikan","tempe","sayur"}
print(makanan)

for a in (makanan):
    print(a)

#cara meupdate isi/nilai pada set dengan cara konversi
makan = list (makanan)
makan[3]= "ayam"
print(makan)
#menghapus isi/nilai pada set
#remove discard clear
makanan.remove("ikan")
print(makanan)

makanan.discard("tempe")
print(makanan)

makanan.clear()
print(makanan)

#cara menambahkan isi/nilai pada set
#add update
makanan.add("mie ayam")
print(makanan)

makanan.update(["bakso","mie","nasi goreng"])
print(makanan)
