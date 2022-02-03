# 6. Rapikan code yang mirip
def payment(currency):
    if currency in ("USD","EUR"):
        print("Standard payment")
    else:
        print("Special payment")

print(payment("USD"))

## if dan elif memiliki blok konten yang sama
## sehingga lebih baik jika menggunakan OR
## atau bisa menggunakan IN dan LIST
## akan lebih cepat ketika menggunakan `set`
## (lanjutan) karena `set` pasti unik
