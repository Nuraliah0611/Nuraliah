hewan = ("kucing","burung","ular","beruang")
for a in (hewan):
    print(a)

print("======tuple======")
a=0
while a < len (hewan):
    print(hewan[a])
    a += 1
#cara mengupdate isi tuple
#mengupdate tuple dengan cara konversi
lia = list(hewan)
lia [0]= "kelinci"
print(lia)

#cara menghapus isi tuple
#remove del pop
lia.remove("burung")
print(lia)

del lia[1]
print(lia)

lia.pop()
print(lia)

#cara menambahkan isi/nilai pada tuple
#append extend insert
lia.append("kucing")
print(lia)

lia.extend(["kupukupu","buaya"])
print(lia)

lia.insert(3,"labalaba")
print(lia)
