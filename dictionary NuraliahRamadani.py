identitas = {"nama":"nuraliah","lengkap":"ramadani sofyan"}
print(identitas)

for key in (identitas):
    print(key,identitas[key])
    
#mengupdate nilai/isi pada dictionary
identitas["nama"] = "nur aliah"
print(identitas)

#menghapus isi/nilai pada dictionary
identitas.pop("lengkap")
print(identitas)

#menambahkan isi/nilai pada dictionary
identitas["semua"] = "sofyan arfah"
print(identitas)
