nilai1 = 6
nilai2 = 2
#+,-,*,%,/,//,**
print(nilai1 + nilai2)
print(nilai1 ** nilai2)

#contoh kasus
nama = " Nuraliah"
gaji_pokok = 2000000
lama_lembur = 72
gaji_lembur = 5000
total_gaji_lembur = lama_lembur * gaji_lembur
gaji_kotor = gaji_pokok + total_gaji_lembur
pajak = 9/100
potongan = gaji_kotor * pajak
gaji_bersih = gaji_kotor - potongan

print("nama :",nama)
print("gaji pokok : rp ",gaji_pokok)
print("gaji lembur : Rp", gaji_lembur)
print("total gaji lembur :rp ", total_gaji_lembur)
print("gaji kotor : rp ", gaji_kotor)
print("pajak :",pajak)
print("potongan : rp ", potongan)
print("gaji bersih : rp", gaji_bersih)
