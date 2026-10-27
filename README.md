# Pertemuan 12 - File I/O dan Error Handling

**Nama:** Aulia Rahma Ramadhani  
**NIM:** 2225250001  
**Kelas:** 3A

## Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file dengan Python. Program ini menggunakan file I/O untuk membaca data nilai mahasiswa, menangani kesalahan input, menghitung statistik nilai, dan menyimpan hasil rekap ke dalam file.

## Struktur Folder

```text
pertemuan-12-file-io-2225250001/
├── README.md
├── .gitignore
├── data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
└── tugas/
    └── rekap_nilai_file.py
```

## Format File Input

Data nilai disimpan dalam file `data/nilai.txt` dengan format:

```text
NIM,nilai
```

Contoh:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Setiap baris berisi NIM dan nilai yang dipisahkan oleh tanda koma. Baris kosong dilewati, sedangkan data yang tidak valid dilaporkan dan tidak dimasukkan ke perhitungan.

## Hasil Rekap

Program menyimpan hasil pengolahan ke file `data/hasil_rekap.txt`, yang berisi:

- Jumlah data nilai yang valid.
- Rata-rata nilai.
- Nilai minimum.
- Nilai maksimum.
- Jumlah mahasiswa yang lulus dengan nilai minimal 60.

## Cara Menjalankan

Pastikan terminal berada di folder utama repository `pertemuan-12-file-io-2225250001`.

Jalankan program utama dengan perintah:

```powershell
python tugas/rekap_nilai_file.py
```

Hasil rekap dapat dilihat pada file `data/hasil_rekap.txt`.

## Error yang Ditangani

- **FileNotFoundError:** Menangani kondisi ketika file input tidak ditemukan dan menampilkan pesan kesalahan tanpa menghentikan program dengan traceback yang tidak ditangani.
- **ValueError:** Menangani format data yang tidak sesuai atau nilai yang tidak dapat dikonversi menjadi angka. Baris tidak valid dilaporkan dan dilewati agar data lainnya tetap dapat diproses.

## Test Case

| No. | Kondisi Pengujian | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Semua data valid | Semua data diproses dan rekap berhasil dibuat | Rekap 5 data berhasil dibuat dengan rata-rata 83,40 | Berhasil |
| 2 | File input tidak ditemukan | Pesan kesalahan ditampilkan tanpa traceback | Pesan file tidak ditemukan ditampilkan | Berhasil |
| 3 | Nilai berisi teks, misalnya `A004,abc` | Baris tidak valid dilaporkan dan dilewati | Baris tidak valid dilaporkan dan rekap tetap dibuat | Berhasil |
| 4 | Terdapat baris kosong | Baris kosong dilewati dan data lain tetap diproses | Isi sesuai hasil pengujian | Perlu disesuaikan |
| 5 | Nilai mahasiswa tepat 60 | Nilai 60 dihitung sebagai lulus | Isi sesuai hasil pengujian | Perlu disesuaikan |

## Refleksi

Melalui latihan ini, saya mempelajari cara membaca, menulis, dan menambahkan isi file menggunakan Python. Saya juga mempelajari penggunaan `try-except` untuk menangani `FileNotFoundError` dan `ValueError`.

Ketika terdapat nilai yang tidak dapat dikonversi menjadi angka, program melaporkan baris yang tidak valid dan melewatinya. Dengan demikian, data valid lainnya tetap dapat diproses dan hasil rekap dapat disimpan ke dalam file.