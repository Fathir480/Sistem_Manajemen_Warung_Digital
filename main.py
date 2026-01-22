# Deklarasi Menu
menu = {
  1 : ['Nasi Goreng',15000,20],
  2 : ['Mie Ayam',12000,20],
  3 : ['Es Teh',5000,20],
  4 : ['Es Jeruk',7000,20]
}

print('==== MENU ====')
print('1. Nasi Goreng')
print('2. Mie Ayam')
print('3. Es TEh')
print('4. Es Jeruk')
print('==============')

total_harga = 0
cek = 'y'
pesanan = []
while cek == 'y' :
  nama = int(input('Masukkan pilihan menu anda: '))
  jumlah = int(input('Jumlah: '))

  if nama not in menu:
    print("Menu tidak valid")
    continue

  if jumlah <= 0:
    print('Jumlah harus lebih dari 0')
    continue

  if menu[nama][2] < jumlah:
    print("stok tidak cukup")
    continue
  
  harga = menu[nama][1]
  total_item = harga*jumlah
  menu[nama][2] -= jumlah

  ketemu = False
  for item in pesanan:
    if item[0] == nama:
      item[1] += jumlah
      item[2] += total_item
      ketemu = True
      break

  if not ketemu:
    pesanan.append([nama,jumlah,total_item])
  total_harga += total_item
  cek = input('Tambah pesanan? (y/n) : ').lower()

print()
subtotal = total_harga

diskon = 0
if subtotal > 50000:
  diskon = subtotal*0.1
total_setelah_diskon = subtotal - diskon

pajak = total_setelah_diskon * 0.05
total_bayar = total_setelah_diskon + pajak

print('========= STRUK BELANJA =========')
for item in pesanan:
  nama_menu = menu[item[0]][0]
  print(f"{nama_menu} x{item[1]} = {item[2]}")
print('---------------------------------')
print('Subtotal       : ', int(subtotal))
print('Diskon         : ', int(diskon))
print('Setelah diskon : ', int(total_setelah_diskon))
print('Pajak (5%)     : ', int(pajak))
print('Total Bayar    : ', int(total_bayar))