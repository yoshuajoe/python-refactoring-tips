# 3. Replace range(len) dengan enumerate
siswa = ["Aldi","Dani","Deni"]
for i, nama in enumerate(siswa, start=1):
    print(i, nama)

## sebaiknya gunakan enumerate untuk lebih menghemat line
## enumerate juga mengembalikan index dan value
## enumerate juga menyediakan parameter `start`
## enumerate(siswa, start=1) -> index i akan dimulai dari 1 (bukan 0)
## (lanjutan) tapi tetap valuenya dari index ke 0 ("Aldi")