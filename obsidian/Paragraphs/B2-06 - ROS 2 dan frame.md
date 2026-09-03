# B2-06 — ROS 2 dan frame

ROS 2 menyediakan middleware robotika yang berpusat pada simpul, topik, layanan, aksi, parameter, dan transformasi. Jembatan pada penelitian ini menerbitkan citra kamera, *CameraInfo*, odometri, IMU, GPS, data jarak, dan transformasi objek; jembatan menerima perintah kecepatan serta tujuan posisi lokal. Perbedaan kerangka koordinat harus dikendalikan pada pembangun pengamatan dan adaptor pengendali. Adaptor VLM tidak boleh melakukan konversi koordinatnya sendiri.

**Sumber eksternal:** [[Papers/Macenski 2022 - ROS 2]]  
**Spesifikasi proyek:** rancangan jembatan dan kebijakan konversi koordinat DroneVLM.  
**Naskah:** `src/01-body/02-bab2.tex`, `SRC-B2-06`
