print("Validasi dan Klasifikasi Nilai Akhir")
 
# 1. Masukan dibaca sebagai teks lalu dibersihkan spasinya.
teks_ujian = input("Nilai ujian (0-100): ").strip()
teks_tugas = input("Nilai tugas (0-100): ").strip()
teks_hadir = input("Kehadiran persen (0-100): ").strip()
 
# 2. Validasi tipe. Hanya baris yang berisiko gagal yang masuk ke blok try
#    agar jelas kesalahan mana yang sedang ditangani.
try:
    ujian = float(teks_ujian)
    tugas = float(teks_tugas)
    hadir = float(teks_hadir)
except ValueError:
    print("Masukan ditolak: seluruh data harus berupa angka.")
else:
    # 3. Validasi rentang. Rantai elif dipakai supaya pesan penolakan
    #    menyebutkan data mana yang bermasalah, bukan pesan umum.
    if not (0 <= ujian <= 100):
        print("Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.")
    elif not (0 <= tugas <= 100):
        print("Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.")
    elif not (0 <= hadir <= 100):
        print("Masukan ditolak: kehadiran di luar rentang 0 sampai 100.")
    else:
        # 4. Seluruh data sah, nilai akhir dihitung.
        akhir = 0.6 * ujian + 0.4 * tugas
        print(f"Nilai akhir = {akhir:.2f}")
 
        # 5. Syarat kehadiran diperiksa SEBELUM predikat, karena kehadiran
        #    kurang dari 80 persen menggugurkan berapa pun nilai akhirnya.
        if hadir < 80:
            print("Status: Tidak memenuhi syarat kehadiran.")
        else:
            # 6. Predikat ditentukan dengan rantai elif MENURUN dari
            #    kategori tertinggi, ditutup else agar menyeluruh.
            if akhir >= 85:
                predikat = "A"
            elif akhir >= 70:
                predikat = "B"
            elif akhir >= 60:
                predikat = "C"
            elif akhir >= 50:
                predikat = "D"
            else:
                predikat = "E"
 
            # 7. Status kelulusan diturunkan dari predikat.
            if predikat in ("A", "B", "C"):
                status = "Lulus"
            else:
                status = "Belum lulus"
 
            # 8. Keluaran akhir.
            print(f"Predikat: {predikat}")
            print(f"Status: {status}")
 