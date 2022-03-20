random = ["nama","buah","hewan","tanaman"]
#perulangan
for a in (random):
    print (a)
print("========list========")
a = 0
while a < len (random) :
    print (random[a])
    a += 1

#memgupdate isi list
random [2] = "benda"
print (random)

#menghapus isi list
#del remove pop
del random[0]
print(random)

random.remove("buah")
print(random)

random.pop()
print(random)

#cara menambahkan isi list
#append extend insert
random.append("langit")
print(random)

random.extend(["rumah"])
print(random)

random.insert(2,"lapangan")
print(random)
