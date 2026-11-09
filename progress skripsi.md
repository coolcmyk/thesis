# Progress Skripsi — Draft 10 Catatan Bimbingan

Disusun berdasarkan naskah skripsi dan bukti implementasi di `/home/kyo/ws/robotics/thesis` sampai 3 November 2026. Setiap bagian **Catatan** dapat disalin ke kolom pada sistem bimbingan. Urutan berikut mengikuti tahapan pekerjaan, bukan tanggal pertemuan yang telah diverifikasi. Tanggal bimbingan dan feedback dosen diisi sesuai kegiatan sebenarnya.

## 1. Studi Literatur dan Penyusunan Bab I

**Catatan:** Melakukan pencarian dan pengkajian referensi mengenai navigasi UAV berbasis bahasa, Vision-Language Model (VLM), dan Vision-Language-Action Model (VLA). Menyusun latar belakang, rumusan masalah, tujuan, dan batasan penelitian dengan fokus pada adaptor agnostik-model untuk navigasi UAV semantik.

## 2. Penyusunan Tinjauan Pustaka dan Metodologi

**Catatan:** Menyusun Bab II mengenai navigasi semantik, penalaran spasial, ROS 2, simulator AirSim/CoSyS-AirSim, serta metode adaptasi LoRA dan GRPO. Menyusun rancangan Bab III yang membagi evaluasi menjadi perbandingan VLM, portabilitas VLA, dan adaptasi OpenVLA melalui kondisi M0, M1, dan M2.

## 3. Penyiapan Infrastruktur Simulasi

**Catatan:** Menyiapkan skrip deployment simulator CoSyS-AirSim pada GPU RunPod, akses desktop melalui noVNC, serta konfigurasi UAV multirotor. Menyiapkan jalur integrasi ROS 2 dan skrip misi waypoint sebagai dasar pengembangan sistem navigasi dan pengujian penerbangan simulasi.

## 4. Implementasi Kerangka DroneVL

**Catatan:** Mengimplementasikan episode runner modular yang memisahkan pengamatan sensor, kebijakan atau model, pengurai aksi, gerbang keselamatan, pengendali, dan evaluator. Menambahkan manifest episode, validasi perintah, pengelolaan urutan subtujuan, serta prosedur lepas landas, penyelesaian misi, dan pendaratan.

## 5. Pengujian Penerbangan Dasar pada Blocks

**Catatan:** Melaksanakan pengujian integrasi pada lingkungan Blocks menggunakan baseline waypoint oracle untuk misi pergi-kembali dan lintasan persegi. Kedua misi berhasil menyelesaikan seluruh waypoint tanpa tabrakan selama misi, sehingga alur komunikasi simulator, kendali, dan evaluasi geometris telah terverifikasi pada pengujian tersebut.

## 6. Pencatatan dan Pengolahan Hasil Pengujian

**Catatan:** Mengembangkan pencatatan manifest, log keputusan, citra RGB dan kedalaman, trajektori, serta ekspor metrik ke CSV untuk mendukung analisis yang dapat ditelusuri. Menambahkan mekanisme perekaman video dan pengambilan artefak dari RunPod, serta memeriksa bahwa perhitungan ulang log pengujian Blocks menghasilkan metrik yang sama.

## 7. Pengembangan Adaptor VLM dan VLA

**Catatan:** Mengimplementasikan adaptor VLM beserta konfigurasi backend yang direncanakan, serta antarmuka VLA dengan validasi checkpoint, satuan, kerangka koordinat, dan horizon aksi. Melakukan penelusuran kandidat checkpoint UAV dan mengidentifikasi kebutuhan penyesuaian keluaran model sebelum dapat digunakan sebagai perintah navigasi.

## 8. Uji Inferensi Model pada GPU

**Catatan:** Melaksanakan uji inferensi awal Qwen3.6, OpenVLA-7B, dan OpenPI π0.5 menggunakan citra RGB tersimpan dari AirSimNH. Qwen menghasilkan aksi terstruktur yang berhasil diurai, sedangkan OpenVLA dan OpenPI berhasil menjalankan inferensi native; hasil ini memverifikasi jalur inferensi awal dan belum merupakan evaluasi penerbangan model secara closed-loop.

## 9. Persiapan Adaptasi OpenVLA dan Uji Awal LoRA

**Catatan:** Mengembangkan pipeline data, decoder aksi UAV, pelatihan LoRA, serta komponen GRPO untuk eksperimen adaptasi OpenVLA. Melaksanakan uji awal decoder dan satu langkah pembaruan LoRA menggunakan enam aksi oracle dari data pengembangan, dilanjutkan uji inferensi statis; pelatihan penuh dan perbandingan kinerja M0–M1–M2 masih perlu dilakukan.

## 10. Pengembangan Skenario Misi Semantik AirSimNH

**Catatan:** Menyusun sepuluh episode pengembangan pada AirSimNH yang mencakup penambatan visual, relasi spasial, pencarian objek, pemilihan simbol semantik, dan instruksi multilangkah. Mengimplementasikan marker visual, aturan inspeksi dan urutan subtujuan, serta pencatatan metrik semantik; melakukan pengujian integrasi kinematik dan preflight visual marker pada simulator sebagai persiapan evaluasi model secara closed-loop.

## Dasar Penyusunan

Bagian ini merupakan catatan pendukung pribadi, bukan teks yang harus disalin ke formulir bimbingan.

| Entri | Bukti utama |
| --- | --- |
| 1–2 | Naskah `src/01-body/01-bab1.tex`, `02-bab2.tex`, `03-bab3.tex`, dan catatan literatur pada `obsidian/` di repositori naskah. |
| 3–4 | `README.md`, `docs/episode-runner.md`, skrip deployment/ROS 2, dan implementasi `src/dronevl/` di repositori robotics. |
| 5–6 | `docs/runpod-smoke-2026-10-05.md` dan `docs/episode-metrics-table.md`: dua misi oracle berhasil; hasil dan artefak tersimpan pada `runs/runpod-smoke-20261005T150518Z/`. |
| 7 | `docs/model-adapters.md`, `docs/vla-checkpoints.md`, dan `configs/adapters/`. Konfigurasi backend dan template VLA tidak berarti seluruh model sudah diuji dalam penerbangan. |
| 8–9 | `docs/runpod-native-inference-2026-10-13.md`: probe model, decoder empat dimensi, serta satu pembaruan LoRA pada enam aksi pengembangan. Belum menjadi hasil pelatihan atau evaluasi ilmiah penuh. |
| 10 | `docs/airsimnh-mission-families.md`, sepuluh manifest misi, hasil pada `runs/mission-family-kinematic/` dan `runs/mission-suite-check-20261103/`, serta dokumentasi preflight visual pada 3 November 2026. |

Perbandingan model pada test set beku, pengujian robustness/generalization, pelatihan LoRA penuh, dan eksperimen GRPO penuh belum dicatat sebagai pekerjaan selesai dalam draft ini. Dokyo masih memerlukan aset peta; kemajuan lingkungan suburban di atas merujuk pada AirSimNH.
