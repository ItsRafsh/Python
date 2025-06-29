import sys
import random
import pygame
from pygame.locals import *

pygame.init()

#   IMAGES
player_ship = (r'game/img/plyship.png')
enemy_ship = (r'game/img/enemyship.png')
ufo_ship = (r'game/img/ufo.png')
player_bullet = (r'game/img/pbullet.png')
enemy_bullet = (r'game/img/enemybullet.png')
ufo_bullet = (r'game/img/enemybullet.png')

screen = pygame.display.set_mode((0,0), FULLSCREEN)
s_width, s_height = screen.get_size()
clock = pygame.time.Clock()   #untuk menghitng framerate per second
FPS = 60

background_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
ufo_group = pygame.sprite.Group()
playerbullet_group = pygame.sprite.Group()
enemybullet_group = pygame.sprite.Group()
ufobullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
particle_group = pygame.sprite.Group()

sprite_group = pygame.sprite.Group()

pygame.mouse.set_visible(False)     #hilangin kursor

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.Surface([x,y])
        self.image.fill('white')
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 2
        self.rect.x += 2
        if self.rect.y > s_height:
            self.rect.y = random.randrange(-10, 0)
            self.rect.x = random.randrange(-400, s_width)

class Particle(Background):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.rect.x = random.randrange(0, s_width)
        self.rect.y = random.randrange(0, s_height)
        self.image.fill('grey')
        self.vel = random.randint(3,8)

    def update(self):
        self.rect.y += self.vel
        if self.rect.y > s_height:
            self.rect.x = random.randrange(0, s_width)
            self.rect.y = random.randrange(0, s_height)




class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)  # untuk pesawatnya
        self.rect = self.image.get_rect() # posisi 
        self.image.set_colorkey('black') # membuat sudur nya jadi transparan, biar ga kotak
        self.alive = True
        self.count_to_live = 0
        self.activate_bullet = True
        self.alpha_duration = 0

    def update(self):
        if self.alive:
            self.image.set_alpha(80)    #player jadi transparan
            self.alpha_duration += 1
            if self.alpha_duration > 170:
                self.image.set_alpha(255)   #akan kambali normal lagi
            mouse = pygame.mouse.get_pos()
            self.rect.x = mouse[0] - 20 #atur posisi mouse
            self.rect.y = mouse[1] + 40 # 20 & 40 agar peluru ditengah mouse
        else:
            self.alpha_duration = 0
            expl_x = self.rect.x + 20
            expl_y = self.rect.y + 40
            explosion = Explosion(expl_x, expl_y)
            explosion_group.add(explosion)
            sprite_group.add(explosion)
            pygame.time.delay(15)   #slow saat meledak

            self.rect.y = s_height + 200
            self.count_to_live += 1
            if self.count_to_live > 100:
                self.alive = True
                self.count_to_live = 0
                self.activate_bullet = True #kalo gada ini, stalh mati gabisa kluar peluru

    def shoot(self):
        if self.activate_bullet:
            bullet = PlayerBullet(player_bullet)
            mouse = pygame.mouse.get_pos()
            bullet.rect.x = mouse[0]
            bullet.rect.y = mouse[1]
            playerbullet_group.add(bullet)
            sprite_group.add(bullet)

    def dead(self):
        self.alive = False
        self.activate_bullet = False


class Enemy(Player):
    def __init__(self, img):
        super().__init__(img)                       # yt part 2
        self.rect.x = random.randrange(50, s_width-50)  # menit 9 penjelasan x dan y screen
        self.rect.y = random.randrange(-500, 0)
        screen.blit(self.image, (self.rect.x, self.rect.y)) #artinya kita lukis di screen

    def update(self):
        self.rect.y += 1    # bergerak kebawah
        if self.rect.y > s_height:  #jika lebih dari layar nya kebawah
            self.rect.x = random.randrange(80, s_width-80) # maka akan kembalikan ke atas #50 itu agar ga mepet ke tembok screen 
            self.rect.y = random.randrange(-2000, 0)    #enemy di atas gerak ke bawah
        self.shoot()

    def shoot(self):
        if self.rect.y in (0,120,200,350,700):      #atur bnyk bullet yg keluar dari musuh
            enemybullet = EnemyBullet(enemy_bullet)
            enemybullet.rect.x = self.rect.x + 16
            enemybullet.rect.y = self.rect.y + 50
            enemybullet_group.add(enemybullet)
            sprite_group.add(enemybullet)


class Ufo(Enemy):
    def __init__(self, img):
        super().__init__(img)
        self.rect.x = -200
        self.rect.y = 200
        self.move = 1

    def update(self):
        self.rect.x += self.move    #akan gerak dari kiri-kana
        if self.rect.x > s_width + 200:  #x melebihi batas screen, dia akan kmbli kekiri
            self.move *= -1
        elif self.rect.x < -200:
            self.move *= -1         #agar bergerak dari kiri kenana
        self.shoot()
    
    def shoot(self):
        if self.rect.x % 50 == 0:       #bikin jarak bola kluar
            ufobullet = EnemyBullet(ufo_bullet)
            ufobullet.rect.x = self.rect.x + 50
            ufobullet.rect.y = self.rect.y + 100
            enemybullet_group.add(ufobullet)
            sprite_group.add(ufobullet)

class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.image.set_colorkey('black')

    def update(self):
        self.rect.y -= 16       #10 itu atur speed peluru. 20 sangat kencang
        if self.rect.y < 0:     #jika posisi kurang dri 0
            self.kill()         #maka akan hapus bullet nya
    
class EnemyBullet(PlayerBullet):
    def __init__(self, img):
        super().__init__(img)
        self.image.set_colorkey('white')

    def update(self):
        self.rect.y += 3
        if self.rect.y > s_height:
            self.kill()

# di yt part 5
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.img_list = []
        for i in range(1,6):
            img = pygame.image.load(f'game/img/exp{i}.png').convert_alpha()  #pake alpha,biar bisa
            img.set_colorkey('black')
            img = pygame.transform.scale(img, (120,120))
            self.img_list.append(img)
        self.index = 0
        self.image = self.img_list[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.count_delay = 0

    def update(self):
        self.count_delay +=1
        if self.count_delay >= 12:
            if self.index < len(self.img_list) -1:
                self.count_delay = 0
                self.index += 1
                self.image = self.img_list[self.index]
        if self.index >= len(self.img_list) -1:
            if self.count_delay >= 12:
                self.kill()


class Game:
    def __init__(self):
        self.count_hit = 0
        self.count_hit2 = 0
        self.lives = 3
        self.score = 0
        self.init_create = True
        self.start_screen()
    
    def start_text(self):
        font = pygame.font.SysFont('Calibri', 50)    #sysFont menggunakan font pc kita
        text = font.render('Space Ngising Shoot', True, 'green')
        text_rect = text.get_rect(center=(s_width/2, s_height/2))   #letakin di tengah teks nya
        screen.blit(text, text_rect)

        font2 = pygame.font.SysFont('Calibri', 20)
        text2 = font2.render('RafGame', True, 'white')
        text2_rect = text2.get_rect(center=(s_width/2, s_height/2+60 ))   #letakin di tengah teks nya
        screen.blit(text2, text2_rect)

    def start_screen(self):
        self.lives = 3
        sprite_group.empty()
        while True:
            screen.fill('black')
            self.start_text()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_RETURN:
                        self.run_game()
            pygame.display.update()

    def pause_text(self):
        font = pygame.font.SysFont('Calibri', 50)    #sysFont menggunakan font pc kita
        text = font.render('PAUSE', True, 'green')
        text_rect = text.get_rect(center=(s_width/2, s_height/2))   #letakin di tengah teks nya
        screen.blit(text, text_rect)

    def pause_screen(self):
        self.init_create = False
        while True:
            self.pause_text()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_SPACE:
                        self.run_game()
            pygame.display.update()


    def game_over_text(self):
        font = pygame.font.SysFont('Calibri', 50)    #sysFont menggunakan font pc kita
        text = font.render('GAME OVER WKWK', True, 'red')
        text_rect = text.get_rect(center=(s_width/2, s_height/2))   #letakin di tengah teks nya
        screen.blit(text, text_rect)

    def game_over_screen(self):
        while True:
            screen.fill('black')
            self.game_over_text()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.start_screen()
            pygame.display.update()

    def create_background(self):
        for i in range(80):
            x = random.randint(3, 7)
            background_image = Background(x,x)
            background_image.rect.x = random.randrange(0, s_width)
            background_image.rect.y = random.randrange(0, s_height)
            background_group.add(background_image)
            sprite_group.add(background_image)

    def create_particles(self):
        for i in range(40):     #pengen sbanyak apa partikel nya
            x = 1
            y = random.randint(1,7)
            particle = Particle(x,y)
            particle_group.add(particle)
            sprite_group.add(particle)

    
    def create_player(self):
        self.player = Player(player_ship)   #tampilakn player
        player_group.add(self.player) #buat grup
        sprite_group.add(self.player)

    def create_enemy(self):
        for i in range(40):     # setting jumlah musuh nya
            self.enemy = Enemy(enemy_ship)
            enemy_group.add(self.enemy)
            sprite_group.add(self.enemy)
    
    def create_ufo(self):
        for i in range(1):
            self.ufo = Ufo(ufo_ship)
            ufo_group.add(self.ufo)
            sprite_group.add(self.ufo)
    
    def playerbullet_hits_enemy(self):      #yt part 4 awal
        hits = pygame.sprite.groupcollide(enemy_group, playerbullet_group, False, True)
        for i in hits:
            self.count_hit += 1
            if self.count_hit == 2:         # 2 kali hit musuh mati
                self.score += 10            #score bunuh croco dpt
                expl_x = i.rect.x + 20
                expl_y = i.rect.y + 40
                explosion = Explosion(expl_x, expl_y)
                explosion_group.add(explosion)
                sprite_group.add(explosion)

                i.rect.x = random.randrange(0, s_width)
                i.rect.y = random.randrange(-3000, -100)
                self.count_hit = 0
    

    def playerbullet_hits_ufo(self):
        hits = pygame.sprite.groupcollide(ufo_group,playerbullet_group, False, True)
        for i in hits:
            self.count_hit2 += 1
            if self.count_hit2 == 15:       #15x hit ufo mati
                self.score += 100           #dapat score 100
                expl_x = i.rect.x + 50
                expl_y = i.rect.y + 60
                explosion = Explosion(expl_x, expl_y)
                explosion_group.add(explosion)
                sprite_group.add(explosion)
                i.rect.x = -199
                self.count_hit2 = 0

    def enemyBullet_hits_player(self):
        if self.player.image.get_alpha() == 255:
            hits = pygame.sprite.spritecollide(self.player, enemybullet_group, True)
            if hits:
                self.lives -= 1
                self.player.dead()      #bug mnt 9.20 ga muncul player
                if self.lives < 0:
                    self.game_over_screen()

    def ufobullet_hits_player(self):
        if self.player.image.get_alpha() == 255:
            hits = pygame.sprite.spritecollide(self.player, ufobullet_group, True)
            if hits:
                self.lives -= 1
                self.player.dead()
                if self.lives < 0:
                    self.game_over_screen()

    def player_enemy_crash(self):
        if self.player.image.get_alpha() == 255:
            hits = pygame.sprite.spritecollide(self.player, enemy_group, False)
            if hits:
                for i in hits:
                    i.rect.x = random.randrange(0, s_width)
                    i.rect.y = random.randrange(-3000, -100)
                    self.lives -= 1
                    self.player.dead()
                    if self.lives < 0:
                        self.game_over_screen()

    def player_ufo_crash(self):
        if self.player.image.get_alpha() == 255:
            hits = pygame.sprite.spritecollide(self.player, ufo_group, False)
            if hits:
                for i in hits:
                    i.rect.x = -199
                    self.lives -= 1
                    self.player.dead()
                    if self.lives < 0:
                        self.game_over_screen()

    def create_lives(self):
        self.lives_img = pygame.image.load(player_ship)
        self.lives_img = pygame.transform.scale(self.lives_img, (40,30)) #img nyawa ini. 40 lebar, 30 tingi
        n = 0
        for i in range(self.lives):
            screen.blit(self.lives_img, (0+n, s_height-765))    #-760 itu nyawa naik ke atas kiri
            n += 60 #atur jarak sesama nyawa

    def create_score(self):
        score = self.score
        font = pygame.font.SysFont('Calibri', 30)
        text = font.render('Score: '+ str(score), True, 'green')
        text_rect = text.get_rect(center=(s_width-150, s_height-750))
        screen.blit(text, text_rect)


    def run_update(self):
        sprite_group.draw(screen)
        sprite_group.update()

    def run_game(self):
        if self.init_create:
            self.create_background()
            self.create_particles()
            self.create_player()
            self.create_enemy()
            self.create_ufo()
        while True:
            screen.fill('black')
            self.playerbullet_hits_enemy()
            self.playerbullet_hits_ufo()
            self.enemyBullet_hits_player()
            self.ufobullet_hits_player()
            self.player_enemy_crash()
            self.player_ufo_crash()
            self.run_update()
            pygame.draw.rect(screen, 'black', (0,0,s_width,35)) #35 itu atur warna putih nya
            self.create_lives()
            self.create_score()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == KEYDOWN:
                    self.player.shoot()
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_SPACE:
                        self.pause_screen()

            pygame.display.update()
            clock.tick(FPS)

def main():
    game = Game()

if __name__ == "__main__":
    main()

