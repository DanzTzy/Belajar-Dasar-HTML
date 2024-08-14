
nama_list = [
    'Andi', 'Budi', 'Citra', 'Dina', 'Eka', 'Fahmi', 'Gita', 'Hadi',
    'Intan', 'Joko', 'Kiki', 'Lina', 'Maya', 'Nina', 'Omar', 'Putra',
    'Rina', 'Siti', 'Taufik', 'Umi', 'Vina'
]

panjang_nama = [len(nama) for nama in nama_list]

panjang_nama_terpanjang = max(panjang_nama)
panjang_nama_terpendek = min(panjang_nama)

print(panjang_nama_terpendek)
print(panjang_nama_terpanjang)

nama_3_huruf = [nama for nama in nama_list if len(nama) == 3]
nama_4_huruf = [nama for nama in nama_list if len(nama) == 4]
nama_5_huruf = [nama for nama in nama_list if len(nama) == 5]
nama_6_huruf = [nama for nama in nama_list if len(nama) == 6]

print("Yang Memiliki nama yang terdiri dari 3 huruf : " ,nama_3_huruf)
print("Yang Memiliki nama yang terdiri dari 4 huruf : " ,nama_4_huruf)
print("Yang Memiliki nama yang terdiri dari 5 huruf : " ,nama_5_huruf)
print("Yang Memiliki nama yang terdiri dari 6 huruf : " ,nama_6_huruf)
