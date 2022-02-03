# 2. Gunakan items() untuk unpack dictionary values
siswa_jurusan = {"ipa":["aldi", "beni"]}
for jurusan, siswa in siswa_jurusan.items():
    if jurusan == "ipa":
        print("Halo {siswa} dari jurusan {jurusan}".format(
            siswa=" dan ".join(siswa),
            jurusan=jurusan
        ))
        
## items() mengembalikan key dan value 
## code terlihat lebih rapi dan mudah dibaca