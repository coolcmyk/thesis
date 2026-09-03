# B1-05 — ROS 2 dan integrasi

CoSyS-AirSim dipilih sebagai lingkungan simulasi karena menyediakan kendaraan multirotor, citra, kedalaman, segmentasi instans, serta lapisan anotasi. Pada konfigurasi penelitian ini, CoSyS-AirSim dihubungkan ke ROS 2 untuk menyediakan citra kamera, informasi kamera, odometri, IMU, GPS, data jarak, dan transformasi objek serta untuk menerima perintah kecepatan atau tujuan posisi lokal. ROS 2 sendiri menyediakan abstraksi simpul, topik, layanan, aksi, parameter, dan transformasi yang relevan bagi integrasi sistem robotika.

**Sumber eksternal:** [[Papers/Macenski 2022 - ROS 2]]  
**Spesifikasi proyek:** konfigurasi CoSyS-AirSim dan ROS 2 pada repositori penelitian.  
**Naskah:** `src/01-body/01-bab1.tex`, `SRC-B1-05`
