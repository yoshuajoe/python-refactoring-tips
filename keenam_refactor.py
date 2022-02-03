# 6. Rapikan code yang mirip
def payment(currency):
    if currency == "USD" or currency == "EUR":
        print("Standard payment")
    else:
        print("Special payment")

print(payment("USD"))

## if dan elif memiliki blok konten yang sama
## sehingga lebih baik jika menggunakan OR