# Audit dan Penyuntingan Gaya Penulisan

Tanggal: 6 November 2026. Acuan: `RULES.md`. Audit ini mencakup abstrak Indonesia dan Inggris, Bab I–V, lampiran, kata pengantar, daftar notasi, dan daftar singkatan. Halaman pernyataan serta pengesahan diperiksa sebagai bagian administratif; teks formulirnya dipertahankan.

## Temuan dan tindakan

| Aturan | Temuan pada draf | Penyuntingan |
| --- | --- | --- |
| 1. Pokok pikiran di awal | Beberapa paragraf membuka dengan rincian atau status yang sulit dikenali. | Kalimat pembuka kini menyebutkan model, komponen, tujuan pengujian, atau status hasil. |
| 2. Pemisahan gagasan | Prosedur, alasan, dan batas interpretasi sering berada dalam satu kalimat atau paragraf padat. | Kalimat serta paragraf dipisahkan menurut fungsi. Urutan langkah dipertahankan. |
| 3. Verba dan rujukan jelas | Terdapat frasa tidak langsung dan rujukan seperti “ia”, “mereka”, atau “hal ini” untuk komponen dan hasil. | Pelaku disebutkan kembali jika rujukan berpotensi ambigu. Verba langsung digunakan pada prosedur. |
| 4. Satu gagasan per paragraf | Penjelasan GRPO mencampur sampling, probabilitas, kegagalan, dan pembaruan. | Setiap prosedur atau batas pembuktian mendapat paragraf tersendiri. |
| 5. Definisi pertama | Beberapa singkatan, checkpoint, rollout, dan seed belum dijelaskan saat diperlukan. | Singkatan dijelaskan pada abstrak dan isi. Checkpoint, rollout, seed, dan bantuan kemajuan diperjelas. Label M0/M1/M2 dan kontrol SFT lanjutan dijelaskan per model. |
| 6. Konsistensi istilah | “Pengaman” berganti dengan “gerbang keselamatan”; terdapat “test set beku”, “persentase poin”, dan istilah campuran lain. | Komponen disebut “gerbang keselamatan”, tindakannya “intervensi keselamatan”. Digunakan “set uji yang telah ditetapkan”, “poin persentase”, serta “kombinasi instruksi yang tidak digunakan untuk pelatihan”. Nama model, pengenal kode, dan simbol dipertahankan. |
| 7. Tujuan sebelum notasi | Penjelasan masukan dan urutan eksekusi terselip dalam definisi simbol. Beberapa persamaan serta tabel belum diikuti petunjuk pembacaan. | Lingkar keputusan dijelaskan sebelum simbol. Persamaan dan tabel diikuti penjelasan. Satuan analisis tingkat keberhasilan adalah episode; penyebutnya dinyatakan. |
| 8. Status pekerjaan | Beberapa kalimat prosedur dapat terbaca sebagai pekerjaan yang sudah selesai. | Rencana memakai “dirancang” atau “akan”. Bukti pengembangan tetap dilaporkan sebagai catatan yang sudah tersedia. Integrasi UAV π₀-FAST dan hasil utama tetap dinyatakan belum selesai. |
| 9. Dasar perbandingan | Beberapa penyebutan “manfaat” belum menyatakan pembanding atau ukuran hasil. | Perbandingan utama menyebut M2 terhadap M1 dan kontrol SFT lanjutan di dalam setiap model, dengan tingkat keberhasilan sebagai ukuran utama. Tabrakan dan intervensi keselamatan tetap dilaporkan. |
| 10. Alur bagian | Abstrak padat oleh rincian, sedangkan Bab IV mencampur pengamatan dengan batas maknanya. | Abstrak mengikuti masalah–tujuan–metode–status hasil–batas. Bab III mengikuti prosedur. Bab IV menyajikan pengamatan sebelum interpretasi. Bab V hanya merencanakan jawaban sejauh bukti tersedia. |

## Perubahan per bagian

- **Abstrak Indonesia dan Inggris:** menyamakan ruang lingkup kedua model, mendefinisikan singkatan, dan menyatakan bahwa manfaat GRPO belum dapat disimpulkan.
- **Bab I:** memecah latar belakang, memperjelas tiga rumusan masalah, serta menyelaraskan tujuan dan batas penelitian.
- **Bab II:** menjelaskan istilah dan fungsi metode sebelum notasi; menjaga sitasi dekat dengan klaimnya; menambahkan penjelasan pembacaan tabel posisi penelitian.
- **Bab III:** menjelaskan masukan–prediksi–gerbang keselamatan–eksekusi–pengamatan sebelum simbol; memisahkan konfigurasi OpenVLA yang tersedia dari rencana FAST; memperjelas hasil dan ketidakpastian per model.
- **Bab IV:** memisahkan uji integrasi, pengembangan OpenVLA, dan rancangan eksperimen utama. Angka pengembangan tidak diubah menjadi hasil pelatihan utama.
- **Bab V:** menghapus pengulangan dan mempertahankan kesimpulan empiris sebagai belum tersedia. Saran dikaitkan dengan pekerjaan yang belum selesai atau kegagalan yang perlu diuji.
- **Lampiran:** menggunakan “sumber bukti”, memecah daftar artefak menjadi paragraf menurut fungsi, dan menjaga path implementasi.
- **Bagian pendukung:** memperjelas kata pengantar, menambahkan singkatan yang digunakan, dan menyelaraskan keterangan notasi dengan istilah gerbang keselamatan.

## Contoh hasil penyuntingan

**Rumusan masalah kedua** kini menanyakan peningkatan tingkat keberhasilan pada model yang sama sebelum membahas hubungannya dengan tabrakan dan intervensi keselamatan. Dua pertanyaan tersebut tidak lagi dimuat dalam satu kalimat panjang.

**Urutan aksi** kini dijelaskan sebagai: model memprediksi token; dekoder menghasilkan aksi usulan; gerbang keselamatan menentukan aksi aktual; sistem menjalankan aksi; simulator menghasilkan pengamatan berikutnya. Simbol diperkenalkan sesudah pembaca memahami urutan tersebut.

**Status Bab IV** kini menyatakan secara langsung bahwa hasil pelatihan penuh M1 dan M2 serta perbandingan set uji belum tersedia. Catatan oracle, inferensi statis, dan pembaruan LoRA awal tetap dibedakan dari hasil eksperimen utama.

## Pemeriksaan makna dan ketertelusuran

Seluruh kemunculan kunci sitasi, lima persamaan bernomor, dan 18 penanda paragraf sumber dibandingkan dengan salinan draf sebelum penyuntingan. Ketiganya dipertahankan. Angka hasil pengembangan, nilai konfigurasi, satuan aksi, kedua model, serta status pekerjaan juga ditinjau dalam penyuntingan.

Pemeriksaan sumber memastikan bahwa kunci sitasi dan sasaran rujukan tersedia serta label tidak ganda. Catatan Obsidian disinkronkan dari sumber LaTeX. `RULES.md` tetap diabaikan oleh Git. Kompilasi PDF berhasil. Halaman abstrak, persamaan GRPO, dan bukti pengembangan diperiksa secara visual. Tidak ditemukan sitasi atau rujukan yang tidak terdefinisi maupun kotak teks melampaui batas halaman pada log kompilasi. Peringatan template yang tersisa mencakup encoding paket, kotak teks kurang penuh, dan jangkar halaman pertama yang ganda. PDF terverifikasi disalin ke `out/thesis.pdf`.
