# Threat Model - Secure OTA Firmware Update & Code Signing Infrastructure

## Project Overview

Proyek ini bertujuan untuk mengamankan proses distribusi firmware menggunakan mekanisme:

- SHA256 Hash Verification
- ECDSA Digital Signature
- Firmware Versioning
- Version Signature Validation
- Anti Rollback Protection

Threat model ini mengidentifikasi ancaman yang mungkin terjadi selama proses distribusi firmware dan menjelaskan mitigasi yang telah diterapkan pada sistem.

---

# 1. Firmware Tampering

## Description

Firmware Tampering terjadi ketika attacker memodifikasi isi firmware sebelum firmware diterima oleh client.

Contoh:

Developer
↓
Firmware.bin
↓
Attacker memodifikasi firmware
↓
Client mengunduh firmware yang telah diubah

## Risk

Firmware yang telah dimodifikasi dapat berisi malware atau backdoor yang memungkinkan attacker mengendalikan perangkat.

## Impact

- Eksekusi kode berbahaya
- Pengambilalihan perangkat
- Kebocoran data
- Kerusakan sistem

## Mitigation

Sistem menerapkan:

- SHA256 Hash Verification
- ECDSA Digital Signature Verification

Client akan menghitung ulang hash firmware dan memverifikasi digital signature sebelum firmware diinstal.

## Affected Components

- firmware.bin
- firmware_hash.md
- firmware.sig
- verify_hash.py
- verify_signature_firmware.py

---

# 2. Version Metadata Tampering

## Description

Attacker mencoba memodifikasi informasi versi firmware yang dikirimkan oleh OTA Server.

Contoh:

Version Asli

{
"version": "1.2.0"
}

Menjadi:

{
"version": "9.9.9"
}

atau

{
"version": "0.1.0"
}

## Risk

Client dapat menerima informasi versi yang salah sehingga proses update menjadi tidak valid.

## Impact

- Salah mendeteksi update
- Anti rollback dapat terganggu
- Client menerima metadata palsu

## Mitigation

Sistem menerapkan:

- Version Signature Verification

Setiap file version.json ditandatangani menggunakan private key dan diverifikasi menggunakan public key yang tersimpan di client.

## Affected Components

- version.json
- version.sig
- verify_signature_version.py
- public_key.pem

---

# 3. Replay Attack

## Description

Replay Attack terjadi ketika attacker mengirim ulang paket OTA lama yang sebelumnya pernah valid.

Contoh:

Firmware v1.0.0
↓
Firmware v2.0.0 telah dirilis
↓
Attacker mengirim ulang firmware v1.0.0

## Risk

Client kehilangan patch keamanan terbaru.

## Impact

- Sistem kembali menggunakan firmware lama
- Patch keamanan terbaru tidak diterapkan
- Potensi eksploitasi meningkat

## Mitigation

Sistem menerapkan:

- Firmware Versioning
- Version Validation
- Version Signature Verification

Client akan memeriksa versi firmware yang diterima sebelum melanjutkan proses update.

## Affected Components

- version.json
- version.sig
- verify_signature_version.py

---

# 4. Rollback Attack

## Description

Rollback Attack terjadi ketika attacker memaksa perangkat untuk menginstal firmware versi yang lebih lama.

Contoh:

Installed Version : 2.0.0

Attacker mengirim:

Incoming Version : 1.0.0

## Risk

Firmware lama dapat memiliki kerentanan yang telah diperbaiki pada versi terbaru.

## Impact

- Vulnerability lama muncul kembali
- Device menjadi rentan dieksploitasi
- Kehilangan patch keamanan

## Mitigation

Sistem menerapkan:

- Semantic Versioning
- Anti Rollback Mechanism
- Installed Version Tracking

Logika:

if incoming_version < current_version:
reject()

Update akan ditolak apabila versi yang diterima lebih rendah dibanding versi yang telah terpasang.

## Affected Components

- installed_version.json
- version.json
- anti_rollback.py

---

# 5. Private Key Theft

## Description

Attacker berhasil memperoleh private key yang digunakan untuk menandatangani firmware.

## Risk

Attacker dapat membuat firmware berbahaya yang memiliki digital signature valid.

## Impact

- Seluruh rantai kepercayaan sistem OTA runtuh
- Firmware berbahaya dianggap resmi
- Kompromi penuh terhadap perangkat

## Mitigation

- Private key tidak disimpan di client
- Private key tidak dipublikasikan ke OTA Server
- Private key hanya digunakan pada lingkungan developer
- Public key digunakan untuk proses verifikasi

## Affected Components

- private_key.pem
- signing process

---

# 6. Man-In-The-Middle (MITM) Attack

## Description

Attacker berada di antara OTA Server dan Client lalu mencoba memodifikasi file yang sedang ditransmisikan.

Contoh:

Client
↓
Attacker
↓
OTA Server

## Risk

File OTA dapat diganti selama proses distribusi.

## Impact

- Firmware palsu dikirim ke client
- Metadata palsu dikirim ke client
- Integritas distribusi terganggu

## Mitigation

Saat ini sistem menggunakan:

- SHA256 Hash Verification
- Digital Signature Verification

Walaupun attacker dapat memodifikasi file selama transmisi, hash dan signature tidak dapat dipalsukan tanpa private key.

## Future Improvement

- HTTPS / TLS
- Certificate Pinning
- Mutual Authentication

## Affected Components

- OTA Server
- Client Network Communication

---

# Security Architecture Summary

Developer
↓
Firmware.bin
↓
Generate SHA256 Hash
↓
Generate ECDSA Signature
↓
OTA Server
↓
Client Download
↓
Verify Version Signature
↓
Anti Rollback Check
↓
Verify Firmware Hash
↓
Verify Firmware Signature
↓
Install Firmware

---

# Security Controls Implemented

| Security Control                | Status             |
| ------------------------------- | ------------------ |
| SHA256 Hash Verification        | Implemented        |
| Firmware Signature Verification | Implemented        |
| Version Signature Verification  | Implemented        |
| Semantic Versioning             | Implemented        |
| Anti Rollback Protection        | Implemented        |
| Installed Version Tracking      | Implemented        |
| Public Key Verification         | Implemented        |
| HTTPS/TLS                       | Future Improvement |

---

# Conclusion

Sistem Secure OTA Firmware Update yang dikembangkan telah menerapkan beberapa lapisan keamanan untuk melindungi integritas firmware, keaslian firmware, validitas metadata versi, serta mencegah rollback ke firmware yang lebih lama.

Pendekatan ini memberikan perlindungan terhadap Firmware Tampering, Version Metadata Tampering, Replay Attack, Rollback Attack, Key Theft, dan Man-In-The-Middle Attack sehingga proses distribusi firmware menjadi lebih aman dan dapat dipercaya.
