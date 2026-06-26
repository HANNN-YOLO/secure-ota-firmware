# Secure OTA Firmware Update & Code Signing Infrastructure

## Gambaran Proyek

Secure OTA Firmware Update & Code Signing Infrastructure merupakan proyek keamanan yang dirancang untuk melindungi proses pembaruan firmware dari modifikasi yang tidak sah, serangan rollback, dan distribusi firmware berbahaya.

Proyek ini mengimplementasikan beberapa mekanisme keamanan seperti hashing firmware, digital signature, firmware versioning, anti rollback, serta sistem logging sehingga hanya firmware yang terpercaya yang dapat dipasang pada perangkat client.

---

# Fitur

- Verifikasi Integritas Firmware menggunakan SHA-256
- Verifikasi Digital Signature menggunakan ECDSA
- Distribusi Firmware OTA yang Aman
- Firmware Versioning (Semantic Versioning)
- Anti Rollback Protection
- Verifikasi Signature Version
- Verifikasi Signature Firmware
- Activity Logging
- OTA Server berbasis Docker

---

# Struktur Proyek

```
secure-ota-firmware/

├── docs/
├── firmware/
├── keys/
├── output/
├── scripts/
├── Dockerfile
├── README.md
└── requirements.txt
```

---

# Arsitektur Sistem

Sistem terdiri dari tiga komponen utama.

- Developer
- OTA Server
- Client

Developer membuat firmware beserta seluruh file keamanan seperti hash, digital signature, version, dan version signature.

OTA Server mendistribusikan seluruh file update.

Client melakukan seluruh proses validasi sebelum firmware dipasang.

---

# Alur OTA Update

```
Developer

↓

Generate Firmware

↓

Generate SHA256

↓

Sign Firmware

↓

Generate Version

↓

Sign Version

↓

Publish ke OTA Server

↓

Client Download Version

↓

Verifikasi Signature Version

↓

Anti Rollback

↓

Download Firmware

↓

Verifikasi Hash

↓

Verifikasi Signature Firmware

↓

Install Firmware

↓

Update installed_version.json
```

---

# Teknologi

- Python
- Flask
- Docker
- Cryptography
- SHA256
- ECDSA
- Requests
- JSON

---

# Instalasi

Clone repository

```bash
git clone https://github.com/your-repository.git
```

Install dependency

```bash
pip install -r requirements.txt
```

Jalankan Server

```bash
python server.py
```

Jalankan Client

```bash
python download_firmware.py
```

---

# Cara Kerja

Developer akan menghasilkan firmware beserta file keamanan.

Client menjalankan:

```
download_firmware.py
```

Kemudian sistem secara otomatis akan melakukan:

- Download version.json
- Verifikasi Signature Version
- Anti Rollback
- Download Firmware
- Verifikasi Hash Firmware
- Verifikasi Signature Firmware
- Install Firmware
- Memperbarui installed_version.json

---

# Fitur Keamanan

| Mekanisme           | Fungsi                              |
| ------------------- | ----------------------------------- |
| SHA-256             | Memastikan integritas firmware      |
| ECDSA               | Memastikan keaslian firmware        |
| Semantic Versioning | Manajemen versi firmware            |
| Anti Rollback       | Mencegah downgrade firmware         |
| Version Signature   | Memastikan keaslian informasi versi |
| Logging             | Mencatat seluruh aktivitas OTA      |

---

# Threat Model

Proyek ini dirancang untuk menghadapi ancaman berikut.

- Firmware Tampering
- Rollback Attack
- Replay Attack
- Key Theft

Dokumentasi lengkap terdapat pada

```
Threat_Model.md
```

---

# Pengujian

Update berhasil

```
Version Signature VALID

Rollback Check PASSED

Firmware Hash VALID

Firmware Signature VALID

Firmware Ready To Install
```

Rollback berhasil dideteksi

```
Rollback Detected

Update Rejected
```

Signature tidak valid

```
Signature INVALID

Installation Aborted
```

---

# Output Proyek

```
version.json

version.sig

firmware.bin

firmware_hash.md

firmware.sig

installed_version.json
```

---

# Pengembangan Selanjutnya

- TLS Communication
- Secure Boot
- Hardware Security Module
- Automatic Firmware Recovery
- Certificate Authentication
- CI/CD OTA Pipeline
- Delta OTA Update

---

# Kontributor

| Anggota  | Tanggung Jawab                                                      |
| -------- | ------------------------------------------------------------------- |
| Member 1 | OTA Server                                                          |
| Member 2 | Client Download dan Logging                                         |
| Member 3 | Cryptography                                                        |
| Member 4 | Versioning, Anti Rollback, Threat Modeling, Dokumentasi, Arsitektur |

## 📅 Bootcamp Preparation

- June 06, 2026 : On Boarding
- June 07, 2026 : Division of Tasks

## Week 1 : June 08 - June 13

| Date          | Activity                                     | Commit                                                               |
| ------------- | -------------------------------------------- | -------------------------------------------------------------------- |
| June 08, 2026 | Day 1 - Fundamental Cryptography             | docs: add cryptography fundamentals notes                            |
| June 09, 2026 | Day 2 - Hashing & SHA256                     | feat: add sha256 hashing script                                      |
| June 10, 2026 | Day 3 - Library Cryptography                 | feat: implement ecdsa key generation                                 |
| June 11, 2026 | Day 4 - Simulation Firmware                  | feat: add dummy firmware and hash generation                         |
| June 12, 2026 | Day 5 - Digital Signing                      | feat: implement firmware signing process                             |
| June 13, 2026 | Day 6 & Day 7- Verify Test and Documentation | feat: add signature verification testing and Documentation in Week 1 |

## Week 2 : June 14 - June 21

| Date          | Activity                                 | Commit                                                       |
| ------------- | ---------------------------------------- | ------------------------------------------------------------ |
| June 14, 2026 | Day 8 - Fundamental Git WorkFlow         | docs: github workflow notes                                  |
| June 15, 2026 | Day 9 - Fundamental GitHUb Actions       | docs: github actions notes                                   |
| June 16, 2026 | Day 10 - Build Github Actions            | feat: add first github action                                |
| June 17, 2026 | Day 11 - Fundamental Github Secret       | feat: configure github secrets                               |
| June 18, 2026 | Day 12 - Integration with python-app.yml | feat: automate firmware signing                              |
| June 19, 2026 | Day 13 & Day 14 - Use Docker OTA Server  | test: validate automated signing and Documentation in Week 2 |

## Week 3 : June 21 - June 28

| Date          | Activity                                   | Commit                                                       |
| ------------- | ------------------------------------------ | ------------------------------------------------------------ |
| June 21, 2026 | Day 15 - Fundamental OTA Server            | docs: ota update notes                                       |
| June 22, 2026 | Day 16 - Create requests client            | feat: add firmware download script                           |
| June 23, 2026 | Day 17 - Build log for OTA Server Client   | feat: add verification logging                               |
| June 24, 2026 | Day 18 - build verify hash for client      | feat: add firmware hash verification                         |
| June 25, 2026 | Day 19 - build verify signature for client | feat: add signature verification                             |
| June 26, 2026 | Day 20 & Day 21 - Testing Scenario Client  | test: add verification scenarios and Documentation in week 3 |

## Week 4 : June 28 - June 28

| Date          | Activity                                                            | Commit                               |
| ------------- | ------------------------------------------------------------------- | ------------------------------------ |
| June 28, 2026 | Day 22 - Fundamental Semantic Versioning                            | docs: semantic versioning notes      |
| June 29, 2026 | Day 23 - Firmware Versioning                                        | feat: add firmware versioning        |
| June 30, 2026 | Day 24 - Fundamental Anti Rollback                                  | docs: anti rollback research         |
| July 01, 2026 | Day 25 - build logic Anti Rollback                                  | feat: implement rollback protection  |
| July 02, 2026 | Day 26 - Threate Model Notes                                        | docs: add threat model               |
| July 03, 2026 | Day 27 - Creating a security diagram for secure OTA server updates. | docs: add architecture diagram       |
| July 04, 2026 | Day 28 - Creating a security diagram for secure OTA server updates. | docs: complete project documentation |

---

# Lisensi

Proyek ini dibuat untuk tujuan pembelajaran dan penelitian.
