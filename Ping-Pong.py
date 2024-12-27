# Mengimpor semua modul dari Pygame
from pygame import *

'''Kelas yang diperlukan'''


# Kelas induk untuk sprite
class GameSprite(sprite.Sprite):
   # Inisialisasi objek sprite
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()  # Memanggil konstruktor dari kelas Sprite induk
       # Memuat gambar player dan mengubah ukurannya sesuai dengan parameter lebar dan tinggi
       self.image = transform.scale(image.load(player_image), (wight, height)) # Contoh: 55,55 - parameter lebar dan tinggi
       self.speed = player_speed  # Kecepatan gerak sprite
       self.rect = self.image.get_rect()  # Mendapatkan rectangle yang melingkupi gambar sprite
       self.rect.x = player_x  # Posisi x awal dari sprite
       self.rect.y = player_y  # Posisi y awal dari sprite

   # Fungsi untuk menggambar sprite pada jendela
   def reset(self): 
       window.blit(self.image, (self.rect.x, self.rect.y))  # Menampilkan gambar pada posisi yang ditentukan

# Kelas Player yang merupakan turunan dari GameSprite
class Player(GameSprite):
   # Update pergerakan pemain ke kanan
   def update_r(self):
       keys = key.get_pressed()  # Mendapatkan status tombol yang sedang ditekan
       # Jika tombol atas ditekan dan posisi sprite masih di atas layar
       if keys[K_UP] and self.rect.y > 5: 
           self.rect.y -= self.speed  # Menggerakan sprite ke atas
       # Jika tombol bawah ditekan dan posisi sprite masih bawah di layar
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed  # Menggerakan sprite ke bawah

   # Update pergerakan pemain ke kiri (dengan tombol W dan S)
   def update_l(self):
       keys = key.get_pressed()  # Mendapatkan status tombol yang sedang ditekan 
       # Jika tombol W ditekan dan posisi sprite masih di atas layar
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed  # Menggerakan sprite ke atas
       # Jika tombol S ditekan dan posisi sprite masih di bawah layar
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed  # Menggerakan sprite ke bawah



# Pengaturan untuk latar belakang dan ukuran layar
back = (200, 255, 255)  # Warna latar belakang (RGB: Biru muda)
win_width = 600  # Lebar layar permainan
win_height = 500  # Tinggi layar permainan
window = display.set_mode((win_width, win_height))  # Menetapkan ukuran layar permainan
window.fill(back)  # Mengisi layar dengan warna layar belakang


# Variabel untuk mengontrol status permainan
game = True  # Flag untuk status permainan, game dimulai
finish = False  # Flag untuk status selesai, permainan belum selesai
clock = time.Clock()  # Menyiapkan objek clock untuk mengontrol FPS
FPS = 60  # Frame per second, kecepatan permainan

# Membuat objek raket (Player) dan bola (GameSprite) 
racket1 = Player('racket.png', 30, 200, 4, 50, 150)  # Pemain 1
racket2 = Player('racket.png', 520, 200, 4, 50, 150)  # Pemain 2
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)  # Bola


# Inisialisasi font untuk menampilkan teks
font.init()  # Menginisialisasi modul font
font = font.Font(None, 35)  # Membuat font dengan ukuran 35
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0)) # Teks jika pemain 1 kalah
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0)) # Teks jika pemain 2 kalah
