# DroneVLM — catatan referensi

Mulai dari [[00-Graph-Start]]. Graph Obsidian membentuk jalur **bab → paragraf lengkap → paper → PDF lokal**. Buka sebuah note paper dan gunakan panel **Backlinks** untuk melihat seluruh paragraf yang merujuk paper tersebut.

[[00-Citation-Map-Bab-1-2]] tetap tersedia sebagai indeks cepat untuk penanda `SRC-B1-*` dan `SRC-B2-*`, citekey, serta halaman bukti.

## Alur kerja Mendeley

1. Impor PDF yang ditautkan pada note di `Papers/` ke Mendeley dan gunakan citekey yang tercantum sebagai `Citation key`.
2. Gunakan citekey yang sama di `pustaka.bib` dan dalam `\citep{...}` pada naskah.
3. Saat menambah paragraf bersitasi, buat satu note di `Paragraphs/` yang memuat paragraf lengkap, tautkan ke note paper di direktori `Papers/`, lalu tautkan note itu dari note bab terkait. Dengan begitu, edge dan backlink pada graph terbentuk otomatis.

> Catatan: tautan `file:///` mengarah ke koleksi PDF lokal di `/home/kyo/ws/robotics/thesis/references`. Jika lokasi koleksi berubah, perbarui tautan pada note paper.
