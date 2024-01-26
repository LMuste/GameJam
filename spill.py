import pygame

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

class Spiller1(Spillobjekt):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.fart = 5
        self.size = 5
        self.color = "red"
    
    def tegn(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect((self.x - self.size, self.y - self.size), (self.size * 3, self.size * 3))

    def oppdater(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a]:
            self.x -= self.fart
        if keys[pygame.K_d]:
            self.x += self.fart
        if keys[pygame.K_w]:
            self.y -= self.fart
        if keys[pygame.K_s]:
            self.y += self.fart

class Spiller2(Spillobjekt):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.fart = 5
        self.size = 5
        self.color = "blue"
    
    def tegn(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect((self.x - self.size, self.y - self.size), (self.size * 3, self.size * 3))

    def oppdater(self):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]:
            self.x -= self.fart
        if keys[pygame.K_RIGHT]:
            self.x += self.fart
        if keys[pygame.K_UP]:
            self.y -= 10
        if keys[pygame.K_DOWN]:
            self.y += self.fart

screen = pygame.display.set_mode((500, 500)) # Setter skjermen til 500x500 piksler.

clock = pygame.time.Clock()

spiller1 = Spiller1(screen.get_width()/2, screen.get_height()/2)
spiller2 = Spiller2(screen.get_width()/2, screen.get_height()/2)

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
    
    spiller1.y += 2
    spiller2.y += 2

    spiller1.tegn()
    spiller1.oppdater()

    spiller2.tegn()
    spiller2.oppdater()

    # Oppdaterer hele skjermen
    pygame.display.flip()

    # Forsikrer at spillet kjører i maksimalt 60 FPS.
    clock.tick(60)

# Avslutter spillet
pygame.quit()