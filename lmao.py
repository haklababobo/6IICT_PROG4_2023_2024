import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.5
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
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
player_velocity = 0

# Platforms
platforms = []

# Functions
def draw_platforms():
    for platform in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.x += keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]

    # Limit player's movement within the screen
    if player.left < 0:
        player.left = 0
    elif player.right > WIDTH:
        player.right = WIDTH

    # Apply gravity
    player_velocity += GRAVITY
    player.y += player_velocity

    # Lock the camera on the player
    camera_offset_y = HEIGHT // 2 - player.y - PLAYER_SIZE // 2

    # Move platforms based on camera offset
    for platform in platforms:
        platform.y += player_velocity

    # Spawn new platforms
    if random.randint(0, 100) < 5 and len(platforms) < 10:
        platform_x = random.randint(0, WIDTH - PLATFORM_WIDTH)
        platform_y = random.randint(0, HEIGHT - PLATFORM_HEIGHT)
        new_platform = pygame.Rect(platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        platforms.append(new_platform)

    # Remove platforms that go off-screen
    platforms = [platform for platform in platforms if platform.y < HEIGHT]

    # Jump when player hits a platform 
    for platform in platforms:
        if player.colliderect(platform) and player_velocity > 0:
            player_velocity = -10  # Adjust this value for jump height
            player.y = platform.y - PLAYER_SIZE

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

# Quit Pygame
pygame.quit()
sys.exit()
