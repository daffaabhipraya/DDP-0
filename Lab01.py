# COLOR FORMATTINGS
col_input = "\033[1;0m{}:\033[1;31m ".format
col_output = "\033[1;34m{}\033[1;0m".format
col_warning = "\033[1;33m{}\033[1;0m".format

print("\033[1;0mWelcome to Dek Depe's Name Tag Store!\n" + "-" * 45)

# INPUT NAMA, TGL LAHIR, JURUSAN, MOTTO
nama = input(col_input("Nama\t".expandtabs(34)))
tanggal_lahir = input(col_input("Tanggal lahir\t".expandtabs(34)))
jurusan = input(col_input("Jurusan\t".expandtabs(34)))
motto_hidup = input(col_input("Motto hidup\t".expandtabs(34)))
while True: # INPUT JUMLAH NAME TAG (n)
    try:
        n = int(input(col_input("Silahkan masukkan banyak name tag\t".expandtabs(34))))
        if n <= 0:
            print(col_warning("Jumlah minimum pemesanan name tag adalah 1!"))
        else:
            break
    except ValueError:
        print(col_warning("Masukkan jumlah name tag dengan angka!"))

print("\033[1;0m-" * 45)

# 'FOR' UNTUK INPUT BENTUK & UKURAN
harga = 0
for i in range(1, n+1):
    print(f"\033[1;0mName Tag {i}:")
    # INPUT BENTUK
    bentuk = input(col_input("Silahkan masukan bentuk name tag anda\t".expandtabs(38))).upper()
    while bentuk != "SEGIEMPAT" and bentuk != "SEGITIGA" and bentuk != "SEGI EMPAT" and bentuk != "SEGI TIGA":
        print(col_warning("Bentuk yang bisa digunakan hanya segiempat atau segitiga!"))
        bentuk = input(col_input("Silahkan masukan bentuk name tag anda\t".expandtabs(38))).upper()
    if bentuk == "SEGIEMPAT" or bentuk == "SEGI EMPAT": # JIKA BENTUK SEGIEMPAT
        while True: # INPUT PANJANG (p)
            try:
                p = float(input(col_input("Masukan panjang (cm)\t".expandtabs(38))))
                if p <= 0:
                    print(col_warning("Nilai panjang harus lebih dari nol!"))
                else:
                    break
            except ValueError:
                print(col_warning("Masukkan nilai panjang dengan tepat!"))
        while True: # INPUT LEBAR (l)
            try:
                l = float(input(col_input("Masukan lebar (cm)\t".expandtabs(38))))
                if l <= 0:
                    print(col_warning("Nilai lebar harus lebih dari nol!"))
                else:
                    break
            except ValueError:
                print(col_warning("Masukkan nilai lebar dengan tepat!"))
        harga += p*l*100
    else: # JIKA BENTUK SEGITIGA
        while True: # INPUT PANJANG ALAS (a)
            try:
                a = float(input(col_input("Masukan panjang alas (cm)\t".expandtabs(38))))
                if a <= 0:
                    print(col_warning("Nilai panjang alas harus lebih dari nol!"))
                else:
                    break
            except ValueError:
                print(col_warning("Masukkan nilai panjang alas dengan tepat!"))
        while True: # INPUT TINGGI (t)
            try:
                t = float(input(col_input("Masukan tinggi (cm)\t".expandtabs(38))))
                if t <= 0:
                    print(col_warning("Nilai tinggi harus lebih dari nol!"))
                else:
                    break
            except ValueError:
                print(col_warning("Masukkan nilai tinggi dengan tepat!"))
        harga += a*t/2*100

print("\033[1;0m-" * 45)

# OUTPUT
print(
    f"Halo {col_output(nama)} dari {col_output(jurusan)}."
    + f'\nLahir pada {col_output(tanggal_lahir)} dengan motto "{col_output(motto_hidup)}."'
    + f"\nTotal biaya untuk memproduksi ke-{col_output(n)} name tag adalah: Rp{col_output(harga)}"
)

print(
    "\033[1;0m-" * 45 + "\nTerima kasih sudah berbelanja di Dek Depe's Name Tag Store!"
)

# END OF PROGRAM