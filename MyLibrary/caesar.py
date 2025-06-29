# aku menulis catatan ini di 25-4-2025
# dari grup ka ojan, pembahasan reza tentang enkripsi dan dekripsi caesar
# blum ada kupelajari beginia simpan saja dulu


def enkripsi_caesar(text, key):
    cipher_text = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                cipher_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                cipher_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            cipher_text += char
    return cipher_text
 
def dekripsi_caesar(cipher_text, key):
    text = ""
    for char in cipher_text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            text += char
    return text

while True :
    print("=== Caesar Cipher ===")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")
    choice = input("Pilih opsi (1/2/3): ")
    if choice == '1':
        text = input("Masukkan teks asli: ")
        key = int(input("Masukkan kunci (0-25): "))
        if key < 0 or key > 25:
            print("Kunci harus antara 0 dan 25.")
            continue
        cipher_text = enkripsi_caesar(text, key)
        print("Teks terenkripsi:", cipher_text)
    elif choice == '2':
        cipher_text = input("Masukkan teks terenkripsi: ")
        key = int(input("Masukkan kunci (0-25): "))
        if key < 0 or key > 25:
            print("Kunci harus antara 0 dan 25.")
            continue
        text = dekripsi_caesar(cipher_text, key)
        print("Teks asli:", text)
    elif choice == '3':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

