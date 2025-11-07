def enkripsi_caesar(plaintext, kunci):
    kunci = kunci % 26  # Pastikan kunci berada dalam 0-25
    ciphertext = ""
    print("\n=== PROSES ENKRIPSI CAESAR CIPHER ===")
    print(f"Plaintext: {plaintext}")
    print(f"Kunci Geser: {kunci} (dari input asli {kunci_input})")
    print("-" * 50)
    
    for i, char in enumerate(plaintext):
        if 'a' <= char <= 'z':
            nilai_awal = ord(char) - ord('a')
            nilai_akhir = (nilai_awal + kunci) % 26
            encrypted_char = chr(nilai_akhir + ord('a'))
        elif 'A' <= char <= 'Z':
            nilai_awal = ord(char) - ord('A')
            nilai_akhir = (nilai_awal + kunci) % 26
            encrypted_char = chr(nilai_akhir + ord('A'))
        else:
            encrypted_char = char
            nilai_awal = nilai_akhir = None
        
        ciphertext += encrypted_char
        if nilai_awal is not None:
            print(f"[{i+1}] Huruf: {char} | ({nilai_awal} + {kunci}) % 26 = {nilai_akhir} → {encrypted_char}")
        else:
            print(f"[{i+1}] Karakter non-alfabet: {char} → {encrypted_char}")
    
    print("-" * 50)
    print(f"Hasil Enkripsi: {ciphertext}\n")
    return ciphertext

def dekripsi_caesar(ciphertext, kunci):
    kunci = kunci % 26
    plaintext = ""
    print("\n=== PROSES DEKRIPSI CAESAR CIPHER ===")
    print(f"Ciphertext: {ciphertext}")
    print(f"Kunci Geser: {kunci} (dari input asli {kunci_input})")
    print("-" * 50)
    
    for i, char in enumerate(ciphertext):
        if 'a' <= char <= 'z':
            nilai_awal = ord(char) - ord('a')
            nilai_akhir = (nilai_awal - kunci + 26) % 26
            decrypted_char = chr(nilai_akhir + ord('a'))
        elif 'A' <= char <= 'Z':
            nilai_awal = ord(char) - ord('A')
            nilai_akhir = (nilai_awal - kunci + 26) % 26
            decrypted_char = chr(nilai_akhir + ord('A'))
        else:
            decrypted_char = char
            nilai_awal = nilai_akhir = None
        
        plaintext += decrypted_char
        if nilai_awal is not None:
            print(f"[{i+1}] Huruf: {char} | ({nilai_awal} - {kunci} + 26) % 26 = {nilai_akhir} → {decrypted_char}")
        else:
            print(f"[{i+1}] Karakter non-alfabet: {char} → {decrypted_char}")
    
    print("-" * 50)
    print(f"Hasil Dekripsi: {plaintext}\n")
    return plaintext

# --- Bagian Utama Program ---
if __name__ == "__main__":
    print("===== CAESAR CIPHER DENGAN INPUT KUNCI =====")
    
    teks = input("Masukkan Plaintext: ")
    
    # Meminta input kunci geser dari pengguna
    while True:
        try:
            kunci_input = int(input("Masukkan Kunci Geser : "))
            if kunci_input < 0:
                print("Kunci harus bilangan bulat non-negatif. Coba lagi.")
            else:
                break
        except ValueError:
            print("Input kunci tidak valid. Masukkan bilangan bulat.")
    
    hasil_enkripsi = enkripsi_caesar(teks, kunci_input)
    hasil_dekripsi = dekripsi_caesar(hasil_enkripsi, kunci_input)
