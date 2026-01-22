# Deklarasi Menu
menu = {
  'Nasi Goreng' : [15000,20],
  'Mie Ayam' : [12000,20],
  'Es Teh' : [5000,20],
  'Es Jeruk' : [7000,20]
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
  choice = int(input('Masukkan pilihan menu anda: '))
  jumlah = int(input('Jumlah: '))

  if jumlah <= 0:
    print('Jumlah harus lebih dari 0')
    continue
  
  if choice == 1:
    total_item = menu['Nasi Goreng'][0]*jumlah
    total_harga += total_item
    menu['Nasi Goreng'][1] -= jumlah
    pesanan.append(['Nasi Goreng',jumlah,total_item])
  elif choice == 2:
    total_item = menu['Mie Ayam'][0]*jumlah
    total_harga += total_item
    menu['Mie Ayam'][1] -= jumlah
    pesanan.append(['Mie Ayam',jumlah,total_item])
  elif choice == 3:
    total_item = menu['Es Teh'][0]*jumlah
    total_harga += total_item
    menu['Es Teh'][1] -= jumlah
    pesanan.append(['Es Teh',jumlah,total_item])
  elif choice == 4:
    total_item = menu['Es Jeruk'][0]*jumlah
    total_harga += total_item
    menu['Es Jeruk'][1] -= jumlah
    pesanan.append(['Es Jeruk',jumlah,total_item])
  else:
    print('Input tidak valid')
  cek = input('Tambah pesanan? (y/n) : ')

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
  print(item[0],' x', item[1], ' = ', item[2])
print('---------------------------------')
print('Subtotal       : ', int(subtotal))
print('Diskon         : ', int(diskon))
print('Setelah diskon : ', int(total_setelah_diskon))
print('Pajak (5%)     : ', int(pajak))
print('Total Bayar    : ', int(total_bayar))