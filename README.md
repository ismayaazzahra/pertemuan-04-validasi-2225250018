# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input 
Nama: Ismaya Catur Dewi Azzahra
NIM: 2225250018
Kelas: 3A

## Tujuan

Membangun program validasi dan klasifikasi dengan rantai `if-elif-else`, serta menerapkan validasi tipe dan rentang input.


## Cara Menjalankan

Pastikan terminal berada pada folder utama repositori.

Contoh menjalankan latihan:

```bash
python latihan/01_predikat_nilai.py
```

```bash
python latihan/02_kategori_bilangan.py
```

```bash
python latihan/03_validasi_rentang.py
```

```bash
python latihan/04_validasi_tipe.py
```

```bash
python latihan/05_klasifikasi_segitiga_sudut.py
```

Untuk menjalankan Praktik 1:

```bash
python praktik/validasi_klasifikasi_nilai.py
```

## Tabel Keputusan Praktik 1

| Kondisi                               | Keputusan                                      |
| ------------------------------------- | ---------------------------------------------- |
| Nilai ujian bukan angka               | Masukan ditolak karena tipe tidak valid        |
| Nilai tugas bukan angka               | Masukan ditolak karena tipe tidak valid        |
| Kehadiran bukan angka                 | Masukan ditolak karena tipe tidak valid        |
| Nilai ujian di luar 0 sampai 100      | Masukan ditolak karena nilai ujian tidak valid |
| Nilai tugas di luar 0 sampai 100      | Masukan ditolak karena nilai tugas tidak valid |
| Kehadiran di luar 0 sampai 100        | Masukan ditolak karena kehadiran tidak valid   |
| Seluruh data valid dan kehadiran < 80 | Tidak memenuhi syarat kehadiran                |
| Kehadiran >= 80 dan nilai akhir >= 85 | Predikat A, Lulus                              |
| Kehadiran >= 80 dan nilai akhir >= 70 | Predikat B, Lulus                              |
| Kehadiran >= 80 dan nilai akhir >= 60 | Predikat C, Lulus                              |
| Kehadiran >= 80 dan nilai akhir >= 50 | Predikat D, Belum lulus                        |
| Kehadiran >= 80 dan nilai akhir < 50  | Predikat E, Belum lulus                        |

Nilai akhir dihitung dengan rumus:

```text
nilai akhir = 0.6 × nilai ujian + 0.4 × nilai tugas
```

## Hasil Pengujian Praktik 1

| No. | Ujian | Tugas | Kehadiran | Keluaran Aktual                                             | Status |
| --: | ----: | ----: | --------: | ----------------------------------------------------------- | ------ |
|   1 |    90 |    80 |        95 | Nilai akhir = 86.00; Predikat A; Status Lulus               | Sesuai |
|   2 |    75 |    70 |        85 | Nilai akhir = 73.00; Predikat B; Status Lulus               | Sesuai |
|   3 |    60 |    60 |        80 | Nilai akhir = 60.00; Predikat C; Status Lulus               | Sesuai |
|   4 |    55 |    50 |        90 | Nilai akhir = 53.00; Predikat D; Status Belum lulus         | Sesuai |
|   5 |    40 |    30 |       100 | Nilai akhir = 36.00; Predikat E; Status Belum lulus         | Sesuai |
|   6 |    90 |    90 |        75 | Nilai akhir = 90.00; Status Tidak memenuhi syarat kehadiran | Sesuai |
|   7 |   105 |    80 |        90 | Penolakan nilai ujian di luar rentang                       | Sesuai |
|   8 |    80 |    -5 |        90 | Penolakan nilai tugas di luar rentang                       | Sesuai |
|   9 |    80 |    80 |       abc | Penolakan karena seluruh data harus berupa angka            | Sesuai |

## Refleksi

Pada awalnya, masukan yang bukan angka seperti `abc` dapat menyebabkan program berhenti karena proses konversi ke `float` menghasilkan `ValueError`. Masalah tersebut ditangani dengan `try-except ValueError`, sehingga program dapat memberikan pesan penolakan yang sesuai.

Selain validasi tipe, program juga memeriksa rentang nilai ujian, nilai tugas, dan kehadiran dari 0 sampai 100. Setelah semua data dinyatakan valid, program menghitung nilai akhir dan melakukan klasifikasi menggunakan rantai `if-elif-else`.

Dari latihan ini saya memahami bahwa validasi harus dilakukan sebelum proses klasifikasi agar data yang tidak valid tidak ikut diproses.

## Sumber

1. Bahan Ajar Algoritma dan Pemrograman Pertemuan 04: Seleksi Multi-Kondisi dan Validasi Input dalam Python, Untirta, Tahun Ajaran 2026/2027 Ganjil.
2. Python Software Foundation. Python Tutorial: More Control Flow Tools.
3. Python Software Foundation. Python Tutorial: Errors and Exceptions.
4. Visual Studio Code. Python Tutorial dan Python Debugging.

## Bantuan yang Digunakan

Dokumentasi resmi Python dan bahan ajar Pertemuan 04 digunakan sebagai referensi dalam memahami struktur `if-elif-else`, validasi input, dan `try-except ValueError`.