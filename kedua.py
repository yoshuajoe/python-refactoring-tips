# 2. Gunakan items() untuk unpack dictionary values
siswa_jurusan = {"ipa":["aldi", "beni"]}
for jurusan in siswa_jurusan:
    siswa = siswa_jurusan[jurusan]
    if jurusan == "ipa":
        print("Halo {siswa} dari jurusan {jurusan}".format(
            siswa=" dan ".join(siswa),
            jurusan=jurusan
        ))
