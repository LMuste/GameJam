import pygame
import random as rnd
import time

pygame.init()

class Spillobjekt:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.color = "grey"
        self.size = 5
        self.rect = pygame.Rect((self.x - self.size, self.y - self.size), (self.size * 2, self.size * 2))
    
    def tegn(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect((self.x - self.size, self.y - self.size), (self.size * 2, self.size * 2))

class Plattform(Spillobjekt):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.size = 5
        self.color = "gray"
        self.bredde = 50
        self.høyde = 100
        self.x = start_x
        self.y = start_y

    def tegn(self):
        self.rect = pygame.Rect((self.x - self.size, self.y - self.size), (self.size*screen.get_width(), self.size*3))
        pygame.draw.rect(screen, self.color, self.rect)

class Blokk(Spillobjekt):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.size = 5
        self.color = "gray"
        self.bredde = 50
        self.høyde = 100
        self.x = start_x
        self.y = start_y

    def tegn(self):
        self.rect = pygame.Rect((self.x, self.y), (self.size*10, self.size*3))
        pygame.draw.rect(screen, self.color, self.rect)

class Spiller1(Spillobjekt):
    def __init__(self, start_x, start_y, start_vx, start_vy):
        super().__init__(start_x, start_y)
        self.fart = 5
        self.size = 5
        self.color = "red"
        self.vx = start_vx
        self.vy = start_vy
        self.a = 0.05
        self.hopp_tid = 0
    
    def tegn(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect((self.x - self.size, self.y - self.size), (self.size * 3, self.size * 3))

    def oppdater(self):
        print(self.vy)
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a]:
            self.x -= self.fart
        if keys[pygame.K_d]:
            self.x += self.fart
        

        spiller1.y += spiller1.vy
        spiller1.vy += spiller1.a

        # Kollisjon med platform

        if pygame.Rect.colliderect(spiller1.rect, plattform.rect):
            #print("-----")
            if spiller1.vy > 0:
                spiller1.vy = 0
            if keys[pygame.K_w] and abs(time.time() - self.hopp_tid) > 0.1:
                self.hopp_tid = time.time()
                self.vy -= 2
        
        # Kollisjon med blokk
        if pygame.Rect.colliderect(spiller1.rect, blokk.rect):
            #print("-----")
            if spiller1.vy > 0:
                spiller1.vy = 0
            if keys[pygame.K_w] and abs(time.time() - self.hopp_tid) > 0.1:
                self.hopp_tid = time.time()
                self.vy -= 2
        


class Spiller2(Spillobjekt):
    def __init__(self, start_x, start_y, start_vx, start_vy):
        super().__init__(start_x, start_y)
        self.fart = 5
        self.size = 5
        self.color = "blue"
        self.vx = start_vx
        self.vy = start_vy
        self.a = 0.05
        self.hopp_tid = 0
    
    def tegn(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect((self.x - self.size, self.y - self.size), (self.size * 3, self.size * 3))

    def oppdater(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]:
            self.x -= self.fart
        if keys[pygame.K_RIGHT]:
            self.x += self.fart

        spiller2.y += spiller2.vy
        spiller2.vy += spiller2.a

        # Kollisjon med plattform
        if pygame.Rect.colliderect(spiller2.rect, plattform.rect):
            print("-----")
            if spiller2.vy > 0:
                spiller2.vy = 0
            if keys[pygame.K_UP] and abs(time.time() - self.hopp_tid) > 0.1:
                self.hopp_tid = time.time()
                self.vy -= 2

        # Kollisjon med blokk
        if pygame.Rect.colliderect(spiller2.rect, blokk.rect):
            print("-----")
            if spiller2.vy > 0:
                spiller2.vy = 0
            if keys[pygame.K_w] and abs(time.time() - self.hopp_tid) > 0.1:
                self.hopp_tid = time.time()
                self.vy -= 2

screen = pygame.display.set_mode((500, 500)) # Setter skjermen til 500x500 piksler.

clock = pygame.time.Clock()

spiller1 = Spiller1(screen.get_width()/2, screen.get_height()/2, 2, 2)
spiller2 = Spiller2(screen.get_width()/2, screen.get_height()/2, 2, 2)

plattform = Plattform(screen.get_width()/screen.get_width(), screen.get_height()-3)

blokk = Blokk(rnd.randint(0, screen.get_width()), rnd.randint(round(70*screen.get_height()/100), round(95*screen.get_height()/100)))

running = True

while running:
    # Avslutter løkken
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fyller skjermen med hvit farge
    screen.fill("white")

    """
    Her skal vi putte spillets logikk, som å tegne figurer og oppdatere posisjonen deres.
    """

    spiller1.y += spiller1.vy
    spiller2.y += spiller2.vy

    spiller1.tegn()
    spiller1.oppdater()

    spiller2.tegn()
    spiller2.oppdater()

    plattform.tegn()

    blokk.tegn()

    # Oppdaterer hele skjermen
    pygame.display.flip()

    # Forsikrer at spillet kjører i maksimalt 60 FPS.
    clock.tick(60)

# Avslutter spillet
pygame.quit()