import heapq

# Daftar mobil yang bisa dipilih
print ("Mobil yg kamu punya: Supra, GTR R35, GTR R34, AE 86, S2000, NSX, Civic")
mobil_yg_kamu_punya = {"Supra", "GTR R35", "GTR R34", "AE 86", "S2000", "NSX", "Civic", "Aventador"}

car_brand = input("Pilih mobil: ").strip()
if car_brand not in mobil_yg_kamu_punya:
    print("Mobil masih di kunci.")
else:
    print(f"Mobil {car_brand}, sabar beliau sedang berada di jalur balap")

    print("-" * 40)
    print("Perkiraan a star dalam game Forza Horizon 4")
    print("-" * 40)
    print("\n")

    # Fungsi menampilkan peta
    def print_peta(peta, posisi_pemain, posisi_musuh):
        for i in range(len(peta)):
            row = []
            for j in range(len(peta[i])):
                if (i, j) == posisi_pemain:
                    row.append('M')  # M untuk mobil
                elif (i, j) == posisi_musuh:
                    row.append('F')  # F untuk Garis FINISH
                elif peta[i][j] == 1:
                    row.append('#')  # Tikungan atau belokan
                else:
                    row.append('.')  # Jalur balap
            print(" ".join(row))
        print()

    # Fungsi untuk menggerakkan pemain
    def gerak_player(peta, posisi_pemain):
        print("MULAIIII")
        print("Gerakan Mobil: W (maju), A (belok kiri), S (mundur), D (belok kanan), O (quit)")
        gerakan = input("Masukkan gerakan (W/A/S/D/O): ").upper()

        if gerakan == "O":
            return "keluar"
        
        x, y = posisi_pemain

        if gerakan == "W" and x > 0 and peta[x-1][y] != 1:
            return (x-1, y)
        elif gerakan == "S" and x < len(peta) - 1 and peta[x+1][y] != 1:
            return (x+1, y)
        elif gerakan == "A" and y > 0 and peta[x][y-1] != 1:
            return (x, y-1)
        elif gerakan == "D" and y < len(peta[0]) - 1 and peta[x][y+1] != 1:
            return (x, y+1)
        else:
            print("Gerakan tidak valid! Coba lagi.")
            return posisi_pemain

    # Fungsi utama
    def main():
        peta = [
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1], 
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0],
        ]

        posisi_pemain = (11, 6)
        posisi_musuh = (0, 0)

        while True:
            print_peta(peta, posisi_pemain, posisi_musuh)
            posisi_pemain = gerak_player(peta, posisi_pemain)
            
            if posisi_pemain == "keluar":
                print("Anda keluar dari permainan.")
                break

            if posisi_pemain == posisi_musuh:
                print("FINISH, selamat kamu juara satu, karna cuma kamu yang ikut balapan!")
                break

    if __name__ == "__main__":
        main()