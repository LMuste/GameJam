import pygame

pygame.init()

class Spillobjekt:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.color = "grey"
        self.size = 5
        self.rect = pygame.Rect((self.x - self.size, self.y - self.size), (self.size * 2, self.sie * 2))
    
    def tegn(self):
        pygame.draw.rect(screen, self.color, self.rect)
        self.rect = pygame.Rect((self.x - self.size, self.y - self.size), (self.size * 2, self.sie * 2))

class Spiller(Spillobjekt):
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

class Spiller2(Spillobjekt):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.fart = 5

screen = pygame.display.set_mode((500, 500)) # Setter skjermen til 500x500 piksler.

clock = pygame.time.Clock()

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

    Spiller.tegn()
    Spiller.oppdater()


    # Oppdaterer hele skjermen
    pygame.display.flip()

    # Forsikrer at spillet kjører i maksimalt 60 FPS.
    clock.tick(60)

# Avslutter spillet
pygame.quit()