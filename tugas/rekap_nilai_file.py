
def baca_nilai(nama_file):
    data_nilai = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, nilai = baris.split(",")
                    nilai = float(nilai)
                    data_nilai.append((nim, nilai))

                except ValueError:
                    print(f"Baris {nomor} tidak valid: {baris}")

    except FileNotFoundError:
        print(f"Error: File {nama_file} tidak ditemukan.")
        return None

    return data_nilai


def tulis_rekap(nama_file, data_nilai):
    with open(nama_file, "w", encoding="utf-8") as file:
        if not data_nilai:
            file.write("Tidak ada data nilai yang valid.\n")
            return

        jumlah = len(data_nilai)
        total = sum(nilai for nim, nilai in data_nilai)
        rata_rata = total / jumlah
        nilai_min = min(nilai for nim, nilai in data_nilai)
        nilai_max = max(nilai for nim, nilai in data_nilai)
        jumlah_lulus = sum(
            1 for nim, nilai in data_nilai if nilai >= 60
        )

        file.write("=== REKAP NILAI MAHASISWA ===\n")
        file.write(f"Jumlah data valid: {jumlah}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {nilai_min:g}\n")
        file.write(f"Nilai maksimum: {nilai_max:g}\n")
        file.write(f"Jumlah mahasiswa lulus: {jumlah_lulus}\n")


def main():
    data_nilai = baca_nilai("data/nilai.txt")

    if data_nilai is None:
        return

    tulis_rekap("data/hasil_rekap.txt", data_nilai)
    print("Rekap nilai berhasil disimpan.")
    print("Silakan periksa data/hasil_rekap.txt.")


if __name__ == "__main__":
    main()
