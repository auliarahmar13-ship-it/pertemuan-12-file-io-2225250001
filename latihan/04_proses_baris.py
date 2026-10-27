
with open("data/catatan.txt", "r", encoding="utf-8") as file:
    for nomor, baris in enumerate(file, start=1):
        print(f"Baris {nomor}: {baris.strip()}")

print("Selesai membaca file.")
