# 7. Gunakan `yield from` daripada yield dalam for
siswa = ["Aldi", "Beni", "Hamid"]
def generator_siswa():
    yield from iter(siswa) 

generator = generator_siswa()
for i in generator:
    print(i)

## https://www.python.org/dev/peps/pep-0380/
## code lebih pendek
## membuang manual looping dari iterable
## meningkatkan performance