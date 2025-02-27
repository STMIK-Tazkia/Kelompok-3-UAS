import heapq

# Welcome Greeting
print(" ")
print("Selamat datang di game Forza Horizon 4")
print(" ")

# Daftar mobil yang bisa dipilih

print("-" * 70)
print("Mobil yg kamu punya: Supra, GTR R35, GTR R34, AE 86, S2000, NSX, Civic")
mobil_yg_kamu_punya = {"Supra", "GTR R35", "GTR R34", "AE 86", "S2000", "NSX", "Civic", "Aventador"}

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
