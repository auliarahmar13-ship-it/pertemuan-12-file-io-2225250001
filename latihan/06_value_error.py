
try:
    nilai = float(input("Masukkan nilai mahasiswa: "))
    print(f"Nilai yang dimasukkan: {nilai}")

except ValueError:
    print("Error: Nilai harus berupa angka.")

print("Program selesai.")
