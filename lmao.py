import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 1
PLATFORM_HEIGHT = 20
PLATFORM_WIDTH = 80
PLATFORM_COLOR = (0, 255, 0)
PLAYER_SIZE = 40
PLAYER_COLOR = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()

# Player
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - PLAYER_SIZE - 20, PLAYER_SIZE, PLAYER_SIZE)
player_velocity = 0

# Platforms
platforms = []

# Functions
def draw_platforms():
    for platform in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player.x += keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]

    # Apply gravity
    player_velocity += GRAVITY
    player.y += player_velocity

    # Jump when player hits a platform
    for platform in platforms:
        if player.colliderect(platform) and player_velocity > 0:
            player_velocity = 0
            player.y = platform.y - PLAYER_SIZE

    # Spawn new platforms
    if random.randint(0, 100) < 5 and len(platforms) < 10:
        platform_x = random.randint(0, WIDTH - PLATFORM_WIDTH)
        platform_y = random.randint(0, HEIGHT - PLATFORM_HEIGHT)
        new_platform = pygame.Rect(platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        platforms.append(new_platform)

    # Remove platforms that go off-screen
    platforms = [platform for platform in platforms if platform.y < HEIGHT]

    # Draw background
    screen.fill((255, 255, 255))

    # Draw platforms
    draw_platforms()

    # Draw player
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)



























class Account:
    def __init__(self, naam, balans, type):
        self.naam = naam
        self.balans = balans
        self.type = type

    def overzicht(self):
        print(f"{self.naam} ({self.type}): {self.balans} euro.")

    def stort(self, bedrag):
        if isinstance(bedrag, (int, float)):
            self.balans += bedrag
            print(f"Nieuwe balans: {self.balans} euro.")
        else:
            print("Ongeldig bedrag ontvangen.")

    def afhalen(self, bedrag):
        if isinstance(bedrag, (int, float)):
            if self.balans - bedrag >= 0:
                self.balans -= bedrag
                print(f"Nieuwe balans: {self.balans} euro.")
            else:
                print("Ontoereikende balans.")
        else:
            print("Ongeldig bedrag ontvangen.")

# Voorbeeld van het gebruik van de Account-klasse
if __name__ == "__main__":
    account1 = Account("Jan", 1000, "EUR")
    account2 = Account("Piet", 2000, "USD")

    account1.overzicht()
    account1.stort(500)
    account1.afhalen(2000)

    account2.overzicht()
    account2.afhalen(3000)
