Today, I'll create a hash verification hash file for the client running download_firmware.py.

The Dev Server workflow will publish three files: firmware.bin, signature.sig, and hash_result.md. The client must download the firmware.bin, signature.sig, and hash_result.md files by running download_firmware.py. It includes logger.py to log activity and verify hashes so the hash server can compare the downloaded hashes.
