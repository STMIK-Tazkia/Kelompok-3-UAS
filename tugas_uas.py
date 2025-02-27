import heapq

# Welcome Greeting
print(" ")
print("Selamat datang di game Forza Horizon 4")
print(" ")

# Daftar mobil yang bisa dipilih

print("-" * 70)
print("Mobil yg kamu punya: SUPRA, R35, R34, AE86, S2000, NSX, CIVIC, AVENTADOR")
mobil_yg_kamu_punya = {"SUPRA", "R35", "R34", "AE86", "S2000", "NSX", "CIVIC", "AVENTADOR"}

# Pilih Mobil
car_brand = input("Pilih mobil: ").strip()
print("-" * 70)
print(" ")

import sys

if car_brand not in mobil_yg_kamu_punya:
    print("Mobil Tidak Ditemukan!.")
    sys.exit()

else:
    print(f"Kamu memilih mobil {car_brand}!")
    print(" ")
    print("-" * 45)
    print("Perkiraan A Star dalam game Forza Horizon 4")
    print("-" * 45)

# Mencari Jalur Terbaik

    def a_star(peta, start, finish):
        baris, kolom = len(peta), len(peta[0])
        open_set = []  # Priority queue untuk A*
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}
        f_score = {start: manhattan(start, finish)}
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            if current == finish:
                return reconstruct_path(came_from, current)
            
            for neighbor in get_neighbors(current, peta):
                temp_g_score = g_score[current] + 1
                
                if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + manhattan(neighbor, finish)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        return None  # Tidak ada jalur
    
# Menghitung Jarak antara dua point grid

    def manhattan(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Mencari Jalur Yang Dapat Dilewati Dari Posisi Pemain Ke Finish

    def get_neighbors(pos, peta):
        x, y = pos
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Atas, bawah, kiri, kanan
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(peta) and 0 <= ny < len(peta[0]) and peta[nx][ny] == 0:
                neighbors.append((nx, ny))
        
        return neighbors

#Merekonstruksi Jalur Terbaik

    def reconstruct_path(came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

# Menampilkan Peta Grid Dan Output Jalur Terbaik

    def print_peta(peta, posisi_pemain, posisi_finish, path=[]):
        for i in range(len(peta)):
            row = []
            for j in range(len(peta[i])):
                if (i, j) == posisi_finish:
                    row.append('F')  # F untuk Garis FINISH
                elif (i, j) == posisi_pemain:
                    row.append('S')  # S untuk menandai Posisi START
                elif (i, j) in path:
                    row.append('*')  # Menandai jalur terbaik
                elif peta[i][j] == 1:
                    row.append('#')  # Rintangan
                elif (i, j) == posisi_finish:
                    row.append('F')  # F untuk Garis FINISH
                else:
                    row.append('.')  # Jalur kosong
            print(" ".join(row))

    grid = [
        [0, 0, 0, 0, 0, 0, 1],
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

    start_pos = (11, 6)
    finish_pos = (0, 0)

    path = a_star(grid, start_pos, finish_pos)
    if path:
        print("Jalur terbaik yang ditemukan:")
        print("-" * 20)
        print("Track Balap")
        print("-" * 20)
        print_peta(grid, start_pos, finish_pos, path)
        print("-" * 20)
        print("KETERANGAN SIMBOL:")
        print("-" * 20)
        print("Simbol S : Menandai Posisi Start Pemain")
        print("Simbol * : Menandai Jalur terbaik")
        print("Simbol # : Menandai Bangunan/pohon/tikungan")
        print("Simbol . : Menandai jalur Balap")
        print("Simbol F : Menandai Garis FINISIH")
        print("-" * 20)
    else:
        print("Tidak ada jalur yang ditemukan.")