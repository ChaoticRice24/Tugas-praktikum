'''
x = 11
Y = 17
i = 0
'''
'''Arithmetic Operations
print(x - Y)
print(x + Y)
print(x * Y)
print(x / Y)
print(x // Y)
print(x % Y)
print (x ** Y)
print (x > Y)
print (x < Y)
print (x == Y)
'''
'''
angka1 = float(input("Masukkan angka pertama : "))
Operator = input("Masukkan operator (+, -, *, /, //, %, **): ") 
rata2 = print("masukan 'o' untuk menghitung rata-rata")
angka2 = float(input("Masukkan angka kedua : "))

hasil = { 
    '+': angka1 + angka2,
    '-': angka1 - angka2,   
    '*': angka1 * angka2,
    '/': angka1 / angka2,
    '//': angka1 // angka2,
    '%': angka1 % angka2,
    '**': angka1 ** angka2,
    'o': (angka1 + angka2) / 2
}

print(f"hasil nya adalah : {hasil[Operator]}")
'''

print("======= Kalkulator Patungan Makan =======")

nama = input("Masukkan nama anda : ")
tagihan = float(input("Masukkan total tagihan : "))
persen = float(input("Masukkan persen yang ingin dibayarkan : "))
jumlahOrang = float(input("Masukkan jumlah orang yang ikut patungan : "))

nominalTip = tagihan * (persen / 100)
totalTagihan = tagihan + nominalTip
PembayaranPerOrang  = totalTagihan / jumlahOrang
print(f"\n======= Ringkasan Tagihan =======")
print(f"Halo {nama}!")
print(f"total tagihan : Rp {totalTagihan:,.2f}")
print(f"Pembayaran yang harus dilakukan per orang : Rp {PembayaranPerOrang:,.2f} ")

'''
print("=== Sistem Simulasi Pertarungan Game ===")
Karakter = input('masukan nama karekter : ')
HealthMonster = int(input('masukan Monster health (lebih dari 1000): '))
Damage = int(input("masukan damage serangan (diatas 100):"))
Combo = int(input('masukan combo serangan : '))
Skill = input('masukan nama skill : ')

damageAkhir = (Damage * Combo) + 500
Healthsisa = HealthMonster - damageAkhir

kondisiMonster = Healthsisa <= 0
overkill = damageAkhir > HealthMonster
KondisiMonsterHidup = HealthMonster > 0

print(f"\n=== Ringkasan Pertarungan ===")
print(f"Nama karekter : {Karakter}")
print(f"total Damage yang Diberikan dari skill {Skill}: {damageAkhir}")
print(f"Sisa HP Monster: {Healthsisa}")

print(f"\n=== Hasil Pertarungan ===")
print(f"Apakah Monster telah dikalahkan: {kondisiMonster}")
print(f"apakah terjadi overkill: {overkill}")
print(f"apakah monster masih hidup: {KondisiMonsterHidup}")
'''

