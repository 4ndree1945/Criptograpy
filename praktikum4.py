# ==============================
# Program Substitusi Cipher (PBO)
# ==============================

class SubstitusiCipher:
    def __init__(self, aturan_substitusi):
        # aturan_substitusi = dictionary pengganti huruf
        self.aturan = aturan_substitusi

    def enkripsi(self, plaintext):
        ciphertext = ""
        print("=== PROSES ENKRIPSI ===")
        for char in plaintext:
            if char.lower() in self.aturan:
                huruf_baru = self.aturan[char.lower()]
                if char.isupper():
                    huruf_baru = huruf_baru.upper()
                print(f"{char} → {huruf_baru}")
                ciphertext += huruf_baru
            else:
                print(f"{char} → (tidak diubah)")
                ciphertext += char
        return ciphertext

    def dekripsi(self, ciphertext):
        plaintext = ""
        print("=== PROSES DESKRIPSI ===")
        # Balik dictionary agar huruf terenkripsi bisa dikembalikan
        balik_aturan = {v: k for k, v in self.aturan.items()}
        for char in ciphertext:
            if char.lower() in balik_aturan:
                huruf_asli = balik_aturan[char.lower()]
                if char.isupper():
                    huruf_asli = huruf_asli.upper()
                print(f"{char} → {huruf_asli}")
                plaintext += huruf_asli
            else:
                print(f"{char} → (tidak diubah)")
                plaintext += char
        return plaintext


# ==============================
# Bagian utama program
# ==============================
if __name__ == "__main__":
    # Aturan substitusi bisa dibuat sesuai kreativitas
    aturan = {
        'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c', 'f': 'x', 'g': 'z',
        'h': 'a', 'i': 's', 'j': 'd', 'k': 'f', 'l': 'g', 'm': 'h', 'n': 'j',
        'o': 'k', 'p': 'l', 'q': 'p', 'r': 'o', 's': 'i', 't': 'u', 'u': 'y',
        'v': 't', 'w': 'r', 'x': 'e', 'y': 'w', 'z': 'q'
    }

    cipher = SubstitusiCipher(aturan)

    print("===== SUBSTITUSI CIPHER =====")
    teks_asli = input("Masukkan teks asli (plaintext): ")
    hasil_enkripsi = cipher.enkripsi(teks_asli)
    print("\nHasil Enkripsi:", hasil_enkripsi)

    hasil_dekripsi = cipher.dekripsi(hasil_enkripsi)
    print("\nHasil Dekripsi:", hasil_dekripsi)