# 5. Sederhanakan conditional statement menjadi return function
siswa = ["Aldi","Dani","Deni"]
def siswa_terdaftar(param):
    return param in siswa or param == "Deni"
print(siswa_terdaftar("Aldi"))

## cara ini hanya bisa digunakan JIKA function me-return BOOLEAN
## dan kedua kondisinya adalah BOOLEAN