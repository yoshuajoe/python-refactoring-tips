# 5. Sederhanakan conditional statement menjadi return function
siswa = ["Aldi","Dani","Deni"]
def siswa_terdaftar(param):
    if param in siswa or param == "Deni":
        return True
    return False
print(siswa_terdaftar("Aldi"))