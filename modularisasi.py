print ('\nMenghitung rumus cara 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print (f'segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas {luas_segitiga} ')

print ('\nMenghitung rumus cara 2')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print (f'segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas {luas_segitiga} ')

def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga
hitung_luas_segitiga(10,6)
hitung_luas_segitiga(20,2)

print ('\nMenghitung rumus cara 3')
print(f'menghitung sgitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(10,6)}')
print(f'menghitung sgitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20,2)}')
