---
title: Peta sitasi Bab I--II DroneVLM
tags:
  - skripsi
  - dronevlm
  - literature-review
  - mendeley
---

# Peta sitasi Bab I--II

Peta ini menghubungkan **kalimat di LaTeX** dengan **sumber primer** yang mendukungnya. Penanda seperti `SRC-B1-01` muncul sebagai komentar tepat setelah kalimat terkait di `src/01-body/01-bab1.tex` atau `src/01-body/02-bab2.tex`. Kunci `citekey` harus sama dengan kunci pada `pustaka.bib` dan *Citation key* di Mendeley.

## Bab I — Pendahuluan

| Penanda | Lokasi dan klaim | Citekey Mendeley/BibTeX | Bukti yang dipakai | PDF lokal |
|---|---|---|---|---|
| `SRC-B1-01` | §1.1, paragraf 1: keputusan selama penerbangan berdasarkan informasi lingkungan memengaruhi lintasan UAV. | `vivaldini2025decision` | Abstrak, hlm. 3: keputusan berdasarkan informasi lingkungan memengaruhi perilaku masa depan yang diekspresikan sebagai rencana lintasan. | [2508.09304v1.pdf](file:///home/kyo/ws/robotics/thesis/references/2508.09304v1.pdf) |
| `SRC-B1-02` | §1.1, paragraf 2: navigasi tujuan-objek memerlukan pencarian, pengenalan, dan pelokalan sasaran. | `ayala2024uav` | Abstrak, hlm. 1: pencarian dan identifikasi target menjadi pusat navigasi tujuan-objek. | [s10462-024-10758-7.pdf](file:///home/kyo/ws/robotics/thesis/references/s10462-024-10758-7.pdf) |
| `SRC-B1-03` | §1.1, paragraf 3: instruksi bahasa membutuhkan penambatan objek/relasi dan pelacakan kemajuan subtujuan. | `zhang2022explicit`; `ma2019selfmonitoring` | Zhang & Kordjamshidi, hlm. 1: landmark dan relasi spasial perlu ditambatkan ke visual. Ma dkk., hlm. 1: agen perlu mengetahui instruksi selesai, berikutnya, arah, dan kemajuan. | [2022.acl-srw.24.pdf](file:///home/kyo/ws/robotics/thesis/references/2022.acl-srw.24.pdf); [669_self_monitoring_navigation_age.pdf](file:///home/kyo/ws/robotics/thesis/references/669_self_monitoring_navigation_age.pdf) |
| `SRC-B1-04` | §1.1, paragraf 4: CLIP dapat mentransfer representasi gambar--teks di luar kelas objek yang tetap; pembangkitan keterangan gambar menghubungkan visi dan bahasa. | `radford2021clip`; `vinyals2015show` | Radford dkk., hlm. 1, abstrak: kelas tetap membatasi generalitas dan data berlabel tambahan diperlukan. Vinyals dkk., hlm. 1, abstrak: deskripsi gambar menghubungkan visi komputer dan pemrosesan bahasa alami. | [radford21a.pdf](file:///home/kyo/ws/robotics/thesis/references/radford21a.pdf); [1411.4555v2.pdf](file:///home/kyo/ws/robotics/thesis/references/1411.4555v2.pdf) |
| `SRC-B1-05` | §1.1, paragraf 7: ROS 2 menyediakan simpul, topik, layanan, aksi, parameter, dan transformasi untuk integrasi robotika. | `macenski2022ros2` | Macenski dkk., hlm. 1 dan pembahasan arsitektur ROS 2. | [2211.07752v1.pdf](file:///home/kyo/ws/robotics/thesis/references/2211.07752v1.pdf) |
| `SRC-B1-06` | §1.1, paragraf 9: benchmark UAV perlu mengevaluasi kecerdasan spasial dari perspektif dan karakteristik UAV. | `zhang2025skyready` | Abstrak dan pendahuluan, hlm. 1: benchmark difokuskan pada kecerdasan spasial untuk navigasi UAV. | [2511.13269v1.pdf](file:///home/kyo/ws/robotics/thesis/references/2511.13269v1.pdf) |

## Bab II — Tinjauan Pustaka

| Penanda | Lokasi dan klaim | Citekey Mendeley/BibTeX | Bukti yang dipakai | PDF lokal |
|---|---|---|---|---|
| `SRC-B2-01` | §2.1.1: UAV membutuhkan keputusan selama penerbangan; tumpukan kendali meneruskan target ke pengendali. | `vivaldini2025decision`; `meier2011pixhawk` | Vivaldini dkk., abstrak hlm. 3, tentang keputusan berdasarkan informasi selama penerbangan. Meier dkk., hlm. 1, tentang sistem penerbangan otonom dengan visi komputasi. | [2508.09304v1.pdf](file:///home/kyo/ws/robotics/thesis/references/2508.09304v1.pdf); [meier2011.pdf](file:///home/kyo/ws/robotics/thesis/references/meier2011.pdf) |
| `SRC-B2-02` | §2.1.1: pencarian dan identifikasi target merupakan bagian pokok navigasi tujuan-objek. | `ayala2024uav` | Abstrak, hlm. 1. | [s10462-024-10758-7.pdf](file:///home/kyo/ws/robotics/thesis/references/s10462-024-10758-7.pdf) |
| `SRC-B2-03` | §2.1.2: CLIP menggunakan supervisi bahasa alami untuk representasi yang dapat ditransfer; *Show and Tell* menghubungkan visi dan bahasa. | `radford2021clip`; `vinyals2015show` | Kedua abstrak pada hlm. 1. | [radford21a.pdf](file:///home/kyo/ws/robotics/thesis/references/radford21a.pdf); [1411.4555v2.pdf](file:///home/kyo/ws/robotics/thesis/references/1411.4555v2.pdf) |
| `SRC-B2-04` | §2.1.3: penambatan landmark dan relasi spasial pada instruksi ke visual penting untuk navigasi visi-bahasa. | `zhang2022explicit` | Abstrak dan pendahuluan, hlm. 1. | [2022.acl-srw.24.pdf](file:///home/kyo/ws/robotics/thesis/references/2022.acl-srw.24.pdf) |
| `SRC-B2-05` | §2.1.3: agen multilangkah perlu mengetahui instruksi selesai, berikutnya, arah, dan kemajuan. | `ma2019selfmonitoring` | Abstrak, hlm. 1. | [669_self_monitoring_navigation_age.pdf](file:///home/kyo/ws/robotics/thesis/references/669_self_monitoring_navigation_age.pdf) |
| `SRC-B2-06` | §2.1.5: ROS 2 adalah middleware berbasis simpul, topik, layanan, aksi, parameter, dan transformasi. | `macenski2022ros2` | Ringkasan arsitektur, hlm. 1--2. | [2211.07752v1.pdf](file:///home/kyo/ws/robotics/thesis/references/2211.07752v1.pdf) |
| `SRC-B2-07` | §2.1.7: evaluasi spasial perlu mempertimbangkan karakteristik khusus UAV. | `zhang2025skyready` | Abstrak dan pendahuluan, hlm. 1. | [2511.13269v1.pdf](file:///home/kyo/ws/robotics/thesis/references/2511.13269v1.pdf) |
| `SRC-B2-08` | §2.2.1: eksplorasi aktif berpemandu VLM relevan untuk inspeksi anomali UAV. | `wal2026active` | Judul, abstrak, dan pernyataan masalah pada bagian awal tesis. | [1_Active_Exploration_for_VLM-Guided_Anomly_Inspection.pdf](file:///home/kyo/ws/robotics/thesis/references/1_Active_Exploration_for_VLM-Guided_Anomly_Inspection.pdf) |
| `SRC-B2-09` | §2.2.2: navigasi UAV tujuan-objek terdiri atas subtugas yang saling bergantung dan memerlukan standardisasi evaluasi. | `ayala2024uav` | Abstrak, hlm. 1: masalah perencanaan, kendali, pelokalan, pemetaan, serta celah standardisasi kerangka kerja. | [s10462-024-10758-7.pdf](file:///home/kyo/ws/robotics/thesis/references/s10462-024-10758-7.pdf) |

## Klaim yang berasal dari rancangan/repository penelitian

Pernyataan tentang paket yang sudah tersedia, nama kamera, kontrak `CanonicalObservation`, kosakata aksi, gerbang keselamatan, dan konfigurasi eksperimen adalah **spesifikasi DroneVLM atau hasil inspeksi repositori**, bukan klaim yang dipinjam dari artikel. Kelak, simpan bukti teknisnya (commit SHA, berkas konfigurasi, dan tangkapan konfigurasi simulator) sebagai catatan eksperimen terpisah.

## Pemeriksaan sebelum menulis

- [ ] Setiap `\citep{...}` baru memiliki citekey yang sama di `pustaka.bib` dan Mendeley.
- [ ] Setiap klaim penting memiliki penanda `SRC-B1-*` atau `SRC-B2-*` di `.tex` dan satu baris pada peta ini.
- [ ] Halaman bukti telah diperiksa dari PDF, bukan hanya dari metadata Mendeley.
- [ ] Jika sumber atau lokasi PDF berubah, perbarui tautan dan jangan mengubah citekey tanpa memperbarui `.tex`.
