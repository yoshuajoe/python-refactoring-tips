# 4. Hindari penggunaan loop counter secara manual 
siswa = ["Aldi","Dani","Deni"]
for i, nama in enumerate(siswa):
    print(i, nama)

## sama dengan poin ketiga
## sebaiknya pakai enumerate
## atau kalau mau hanya dapatkan panjang list
## (lanjutan) cukup pakai len(siswa)
jumlah_siswa = len(siswa)