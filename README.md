# Warung Digital – Sistem Kasir Sederhana (Python)

Project ini adalah program **kasir berbasis terminal** yang dibuat menggunakan **Python dasar**.  
Program ini mensimulasikan sistem pemesanan di warung makan, mulai dari memilih menu, menghitung total belanja, diskon, pajak, hingga menampilkan struk belanja.

Project ini dibuat untuk **melatih logika pemrograman**, khususnya penggunaan:
- `if / elif / else`
- `while`
- `for`
- list dan dictionary

---

## 📌 Fitur Utama
- Menampilkan opsi sistem (tambah,lihat,hapus,checkout)
- Sinkron fitur hapus ke pesanan dan stok menu
- Menampilkan daftar menu dan harga
- Pemesanan lebih dari satu item
- Penyimpanan detail pesanan
- Perhitungan subtotal
- Diskon otomatis 10% untuk pembelian di atas Rp50.000
- Pajak 5% setelah diskon
- Menampilkan struk belanja akhir

---

## Daftar Menu
|    Menu    |  Harga   |
|------------|----------|
| Nasi Goreng| Rp15.000 |
|  Mie Ayam  | Rp12.000 |
|   Es Teh   | Rp5.000  |
|  Es Jeruk  | Rp7.000  |

---

## Alur Program

1. Program menampilkan menu utama
2. User memilih opsi
3. Jika tambah pesanan:
   - User memilih menu
   - User memasukkan jumlah
   - Pesanan disimpan / diperbarui di list
4. User dapat:
   - Menambah pesanan
   - Melihat pesanan
   - Menghapus pesanan
5. Saat checkout, program menghitung:
   - Subtotal
   - Diskon
   - Pajak
   - Total bayar
6. Struk belanja ditampilkan


---

## Improve

Membuat perhitungan subtotal berdasarkan pesanan bukan looping