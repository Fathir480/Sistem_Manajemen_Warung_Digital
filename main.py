# Deklarasi Menu
menu = {
  1 : ['Nasi Goreng',15000,20],
  2 : ['Mie Ayam',12000,20],
  3 : ['Es Teh',5000,20],
  4 : ['Es Jeruk',7000,20]
}

pilihan = 0
total_harga = 0
pesanan = []
while True :
  print("1. Tambah Pesanan")
  print("2. Lihat Pesanan")
  print("3. Hapus Pesanan")
  print("4. Checkout")
  print("=================")

  pilihan = int(input('Pilih Opsi (1..4): '))

  if pilihan == 1:
    pesan_ulang = 'y'
    while pesan_ulang == 'y':
      print('==== MENU ====')
      print('1. Nasi Goreng')
      print('2. Mie Ayam')
      print('3. Es TEh')
      print('4. Es Jeruk')
      print('==============')

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
      pesan_ulang = input('Tambah Pesanan (y/n): ').lower()

  elif pilihan == 2:
    if not pesanan:
      print('Anda belum memiliki pesanan')
      continue
    else:
      print('=========== Pesanan Anda ===========')
      print('====================================')
      for item in pesanan:
        nama_menu = menu[item[0]][0]
        print(f"{nama_menu} x{item[1]} = {item[2]}")
  
  elif pilihan == 3:
    if not pesanan:
      print('Anda belum memiliki pesanan')
      continue

    hapus = int(input('pilih item yang ingin dihapus: '))
    berapa = int(input('Jumlah dihapus: '))

    temp = False

    for item in pesanan:  
      if hapus == item[0]:
        temp = True
        if item[1] < berapa:
          print('Kamu tidak pesan sebanyak itu')
          break

        harga_satuan = menu[hapus][1]
        harga_kurang = harga_satuan*berapa
        total_harga -= harga_kurang
        menu[hapus][2] += berapa

        if item[1] == berapa:
          pesanan.remove(item)
          nama_menu = menu[item[0]][0]
          print(f"Pesanan {nama_menu} sudah dihapus")

        elif item[1] > berapa:
          item[1] -= berapa
          item[2] -= harga_kurang
          nama_menu = menu[item[0]][0]
          print(f"Pesanan {nama_menu} dikurangi {berapa} porsi")
        break

    if not temp: 
      print('Menu tersebut tidak anda pesan')
      continue
  
  elif pilihan == 4:
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
    break


