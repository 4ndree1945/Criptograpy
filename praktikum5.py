class VigenereCipher:
    def __init__(self, key: str):
        self.key = key.upper()  # Kata kunci dimasukkan oleh pengguna

    def _format_text(self, text: str) -> str:
        """Membersihkan teks agar hanya huruf kapital tanpa spasi."""
        return ''.join(filter(str.isalpha, text.upper()))

    def _shift_char(self, char: str, key_char: str, mode: str) -> tuple:
        """Melakukan pergeseran karakter untuk enkripsi/dekripsi."""
        p = ord(char) - ord('A')
        k = ord(key_char) - ord('A')
        if mode == 'encrypt':
            c = (p + k) % 26
        else:
            c = (p - k + 26) % 26
        return chr(c + ord('A')), p, k, c

    def encrypt(self, plaintext: str) -> str:
        """Melakukan enkripsi teks menggunakan Vigenère Cipher."""
        plaintext = self._format_text(plaintext)
        ciphertext = ""
        print("\n=== PROSES ENKRIPSI VIGENÈRE ===")
        print(f"Plaintext : {plaintext}")
        print(f"Kunci     : {self.key}")
        print("-" * 50)

        for i, char in enumerate(plaintext):
            key_char = self.key[i % len(self.key)]
            encrypted_char, p, k, c = self._shift_char(char, key_char, mode='encrypt')
            ciphertext += encrypted_char
            print(f"[{i+1}] Huruf: {char} | Kunci: {key_char} "
                  f"| ({p} + {k}) % 26 = {c} → {encrypted_char}")

        print("-" * 50)
        print(f"Hasil Enkripsi: {ciphertext}\n")
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        """Melakukan dekripsi teks menggunakan Vigenère Cipher."""
        ciphertext = self._format_text(ciphertext)
        plaintext = ""
        print("\n=== PROSES DEKRIPSI VIGENÈRE ===")
        print(f"Ciphertext: {ciphertext}")
        print(f"Kunci     : {self.key}")
        print("-" * 50)

        for i, char in enumerate(ciphertext):
            key_char = self.key[i % len(self.key)]
            decrypted_char, c, k, p = self._shift_char(char, key_char, mode='decrypt')
            plaintext += decrypted_char
            print(f"[{i+1}] Huruf: {char} | Kunci: {key_char} "
                  f"| ({c} - {k} + 26) % 26 = {p} → {decrypted_char}")

        print("-" * 50)
        print(f"Hasil Dekripsi: {plaintext}\n")
        return plaintext


# ==== DEMONSTRASI PROGRAM INTERAKTIF ====
if __name__ == "__main__":
    print("===== PROGRAM VIGENÈRE CIPHER BERBASIS PBO =====")
    teks = input("Masukkan teks: ")
    kunci = input("Masukkan kata kunci: ")

    # Membuat objek cipher dengan kunci dari pengguna
    cipher = VigenereCipher(kunci)

    hasil_enkripsi = cipher.encrypt(teks)
    hasil_dekripsi = cipher.decrypt(hasil_enkripsi)
