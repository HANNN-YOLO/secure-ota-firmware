in this day i will create verify signature

so im done to create verify_signature.py
for we have project secure ota firmware
in week 1, i learned fundamental cryptography, sha-256, i create dumy firmware to use my generate_hash.py to produce hash-256 ,
i create generate_keys.py so get private_key.pem and public_key.pem
i create sign_firmware.py to use private_key.pem and use firmware.bin to produce digital.sig
i create verify_signature.py to use signature.sig, firmware.bin for sha-256 and public_key.pem to produce valid or invalid
in this case in sign_firmware.py and verify_signature.py use firmware_hash. if i use firmware_data so i just use firmware.bin and use private_key.pem, so just firmware.bin -> private key -> signature.bin, and now im use firmware hash because i just use my firmware and hash firmware again and use my private_key to produce signature.sig, so just firmware.bin-> sha-256-> private_key.pem->sign_firmare

so why in verify_signature.py i use again firmware hash because i pick firmware hash in sign_firmware.py. so for verify_signature.py and sign_firmware.py just only use firmware hash, so in verify_signature just use firmware.bin -> sha-256 -> signature.sig -> verify signature to produce valid or invalied
