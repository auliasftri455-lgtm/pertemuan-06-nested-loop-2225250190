# Pertemuan 06 - Nested Loop, Pola, Akumulasi, dan Pencacahan

## Identitas
- Nama: Aulia Safitri
- NIM: 2225250190
- Kelas: 3B

## Tujuan
Mempelajari penggunaan nested loop, pola, akumulasi, dan pencacahan menggunakan Python.

## Daftar Program
1. 01_pasangan_indeks.py
2. 02_pola_segitiga.py
3. 03_jumlah_per_baris.py
4. 04_hitung_pasangan.py
5. tabel_perkalian_dan_statistik.py

## Hasil Pengujian Tugas Utama

| Nilai n | Total seluruh hasil | Banyak hasil genap |
|---|---:|---:|
| 1 | 1 | 0 |
| 2 | 9 | 3 |
| 3 | 36 | 5 |

## Kesimpulan
Nested loop dapat digunakan untuk membuat tabel perkalian. Akumulasi digunakan untuk menghitung jumlah hasil, sedangkan pencacahan digunakan untuk menghitung banyaknya hasil genap.

## Pengujian Program Nomor 04

Program menghitung banyak pasangan bilangan `(i, j)` yang memenuhi syarat `i + j <= n`.

Hasil pengujian:
- `n = 2` menghasilkan 1 pasangan.
- `n = 3` menghasilkan 3 pasangan.
- `n = 5` menghasilkan 10 pasangan.

## Kuis Formatif

1. Berapa banyak pasangan yang diperiksa oleh nested loop dengan 4 iterasi pada loop luar dan 6 iterasi pada loop dalam?
   Jawaban: 24 pasangan.

2. Apa yang terjadi pada loop dalam setiap kali loop luar melakukan iterasi baru?
   Jawaban: Loop dalam dimulai kembali dari nilai awalnya.

3. Apa fungsi "print()" setelah loop dalam selesai?
   Jawaban: Memindahkan output ke baris berikutnya.

4. Di mana variabel "total_baris" harus diinisialisasi?
   Jawaban: Di dalam loop luar, sebelum loop dalam dimulai.

5. Di mana variabel "total_semua" harus diinisialisasi?
   Jawaban: Sebelum loop luar dimulai.

6. Apa perbedaan counter dan accumulator?
   Jawaban: Counter menghitung kejadian, sedangkan accumulator menjumlahkan nilai.

7. Berapa banyak pasangan yang diperiksa jika kedua loop berjalan 3 kali?
   Jawaban: 9 pasangan.

8. Apa fungsi "if" di dalam nested loop?
   Jawaban: Memeriksa setiap pasangan dan menambah counter jika memenuhi kondisi.

9. Apa arti working tree bersih (clean) pada Git?
   Jawaban: Tidak ada perubahan file yang belum disimpan sebagai commit.

10. Perintah Git apa yang digunakan untuk mengirim commit ke GitHub?
    Jawaban: "git push".