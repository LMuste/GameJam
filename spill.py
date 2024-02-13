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
        self.color = "SeaGreen"
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
        self.color = "SeaGreen"
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
        self.rect = pygame.Rect((self.x - self.size, self.y - self.size), (self.size * 3, self.size * 3))
        self.headingy = pygame.Rect((self.x - self.size, self.y -self.size + 3*self.vy), (self.size * 3, self.size * 3))
        self.headingx = pygame.Rect((self.x - self.size + self.vx, self.y - self.size), (self.size * 3, self.size * 2))
        screen.blit(player1, (self.x - self.size, self.y - self.size))
        #pygame.draw.rect(screen, self.color, self.rect)

    def oppdater(self):
        print(self.vy)
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a] and self.x > 0:
            self.vx = -5
        elif keys[pygame.K_d] and self.x < screen.get_width() -self.size:
            self.vx = 5
        else:
            self.vx = 0
        
        spiller1.y += spiller1.vy
        spiller1.x += spiller1.vx
        spiller1.vy += spiller1.a
        
        # Kollisjon med plattform
        if pygame.Rect.colliderect(spiller1.headingy, plattform.rect):
            if spiller1.vy > 0:
                spiller1.vy = 0
            if keys[pygame.K_w] and abs(time.time() - self.hopp_tid) > 0.1:
                self.hopp_tid = time.time()
                self.vy -= 2
        
        # Kollisjon med blokk i Y
        for x in blokker:
            if pygame.Rect.colliderect(spiller1.headingy, x.rect):
                if spiller1.vy > 0:
                    spiller1.vy = 0
                if spiller1.vy < 0:
                    spiller1.vy *= -1
                if keys[pygame.K_w] and abs(time.time() - self.hopp_tid) > 0.1:
                    self.hopp_tid = time.time()
                    self.vy -= 2
        
        # Kollisjon med blokk i X
        for x in blokker:
            if pygame.Rect.colliderect(spiller1.headingx, x.rect) and abs(time.time() - self.hopp_tid) > 0.1:
                if spiller1.vx > 0:     #mot høyre
                    spiller1.x -= 10
                if spiller1.vx < 0:     #mot venstre
                    spiller1.x += 10

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
        self.rect = pygame.Rect((self.x - self.size, self.y - self.size), (self.size * 3, self.size * 3))
        self.headingy = pygame.Rect((self.x - self.size, self.y -self.size + 3*self.vy), (self.size * 3, self.size * 3))
        self.headingx = pygame.Rect((self.x - self.size + self.vx, self.y - self.size), (self.size * 3, self.size * 2))
        "screen.blit(player2, (self.x - self.size, self.y - self.size))"
        #pygame.draw.rect(screen, "green", self.headingx)
        pygame.draw.rect(screen, self.color, self.rect)

    def oppdater(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT] and self.x > 0:
            self.vx = -5
        elif keys[pygame.K_RIGHT] and self.x < screen.get_width() - self.size:
            self.vx = 5
        else:
            self.vx = 0

        spiller2.y += spiller2.vy
        spiller2.x += spiller2.vx
        spiller2.vy += spiller2.a

        # Kollisjon med plattform
        if pygame.Rect.colliderect(spiller2.headingy, plattform.rect):
            #print("-----")
            if spiller2.vy > 0:
                spiller2.vy = 0
            if keys[pygame.K_UP] and abs(time.time() - self.hopp_tid) > 0.1:
                self.hopp_tid = time.time()
                self.vy -= 2

        # Kollisjon med blokk i Y
        for x in blokker:
            if pygame.Rect.colliderect(spiller2.headingy, x.rect):
                #print("-----")
                if spiller2.vy > 0:
                    spiller2.vy = 0

                if spiller2.vy < 0:
                    spiller2.vy *= -1
                                        
                if keys[pygame.K_UP] and abs(time.time() - self.hopp_tid) > 0.1:
                    self.hopp_tid = time.time()
                    self.vy -= 2

        # Kollisjon med blokk i X
        for x in blokker:
            if pygame.Rect.colliderect(spiller2.headingx, x.rect) and abs(time.time() - self.hopp_tid) > 0.1:
                if spiller2.vx > 0:     #mot høyre
                    spiller2.x -= 10
                if spiller2.vx < 0:     #mot venstre
                    spiller2.x += 10
          

screen = pygame.display.set_mode((500, 500)) # Setter skjermen til 500x500 piksler.

clock = pygame.time.Clock()

spiller1 = Spiller1(screen.get_width()/3, screen.get_height()-30, 2, 2)
spiller2 = Spiller2(screen.get_width()/2, screen.get_height()-30, 2, 2)

plattform = Plattform(screen.get_width()/screen.get_width(), screen.get_height()-3)

#blokk = Blokk(rnd.randint(0, screen.get_width()), rnd.randint(round(80*screen.get_height()/100), round(90*screen.get_height()/100)))

blokker = []

for n in range(100):
    #start_x = rnd.randint(0, screen.get_width())
    #start_y = rnd.randint(round(80*screen.get_height()/100), round(90*screen.get_height()/100))
    start_x = rnd.randint(1, screen.get_width())
    start_y = 500 - 40*n
    blokk = Blokk(start_x, start_y)
    blokker.append(blokk)

running = True

# Bilder
player1 = pygame.image.load("figur.png")
play1_rect = player1.get_rect()
"""player2 = pygame.image.load("figur2.png")
play2_rect = player2.get_rect()
"""
bakgrunn = pygame.image.load("bakgrunn.png")

# Font
pygame.font.init() # Font (initialiserer teks, eller font)
font = pygame.font.SysFont("Arial", int(screen.get_height()/28)) # Font (int: er størrelsen på teksten)

# Score spiller 1 og 2
score1 = 0
score2 = 0

topp_tid = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if (spiller1.y < screen.get_height()/6 or spiller2.y < screen.get_height()/6) and abs(time.time() - topp_tid) > 3:
        topp_tid = time.time()
        print("-")
        for x in blokker:
            x.y += 100
            spiller1.y += 0.1
            spiller1.vy = 20
            spiller2.y += 0.1
            spiller2.vy = 20
            plattform.y += 100

    #print((spiller2.x, spiller2.y))

    screen.blit(bakgrunn, (0, 0))

    # Score spiller 1
    tekst1 = font.render(f"Score:", True, "black") # Inputen måtte være str
    tekst1_rect = tekst1.get_rect(center=(screen.get_width() - 470, screen.get_height() - 470))
    screen.blit(tekst1, tekst1_rect) # Tegner teksten
    # Score Spiller 2
    tekst2 = font.render(f"Score:", True, "black") # Inputen måtte være str
    tekst2_rect = tekst2.get_rect(center=(screen.get_width() - 50, screen.get_height() - 470))
    screen.blit(tekst2, tekst2_rect) # Tegner teksten

    spiller1.y += spiller1.vy
    spiller2.y += spiller2.vy

    spiller1.tegn()
    spiller1.oppdater()

    spiller2.tegn()
    spiller2.oppdater()

    plattform.tegn()

    for x in blokker:
        x.tegn()

    # Oppdaterer hele skjermen
    pygame.display.flip()

    # Forsikrer at spillet kjører i maksimalt 60 FPS.
    clock.tick(60)

# Avslutter spillet
pygame.quit()