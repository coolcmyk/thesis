# B2-07 — Benchmark yang dapat direproduksi

Benchmark *closed-loop* yang dapat direproduksi perlu mendefinisikan lebih dari sekadar kumpulan gambar. Setiap episode harus memuat adegan, *seed*, pose awal, instruksi, target, kondisi lingkungan, anggaran waktu dan keputusan, batasan, kondisi terminal, serta kebenaran dasar. Versi kode dan aset, konfigurasi model, *prompt*, perangkat keras, dan log mentah perlu dapat ditelusuri. Evaluator harus menghitung metrik dari log tersebut, bukan dari tabel yang diubah secara manual. Kebutuhan evaluasi spasial yang spesifik untuk UAV juga ditekankan oleh benchmark UAV berbasis VLM.

**Sumber:** [[Papers/Zhang et al 2025 - VLM Sky-Ready]]  
**Naskah:** `src/01-body/02-bab2.tex`, `SRC-B2-07`
