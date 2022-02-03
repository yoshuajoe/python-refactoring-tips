# 7. Gunakan `yield from` daripada yield dalam for
siswa = ["Aldi", "Beni", "Hamid"]
def generator_siswa():
    for nama in iter(siswa):
        yield nama

generator = generator_siswa()
for i in generator:
    print(i)