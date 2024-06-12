import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player properties
player_size = 50
player_color = BLACK
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_size
player_velocity_x = 0
player_velocity_y = 0
gravity = 9.8 * 20  # Gravity in pixels/s^2
jump_strength = -100  # Initial jump velocity in pixels/s
ground_y = SCREEN_HEIGHT - player_size
is_jumping = False

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gravity Simulation")

# Clock to control frame rate and measure time
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Calculate delta time in seconds
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    
    # Horizontal movement
    if keys[pygame.K_LEFT]:
        player_velocity_x = -200  # Velocity in pixels/s
    elif keys[pygame.K_RIGHT]:
        player_velocity_x = 200  # Velocity in pixels/s

    # Jumping
    if keys[pygame.K_SPACE] and not is_jumping:
        player_velocity_y = jump_strength
        is_jumping = True

    # Apply gravity
    player_y += player_velocity_y * dt
    player_x += player_velocity_x * dt
    player_velocity_y += gravity * dt

    # Prevent falling through the ground
    if player_y >= ground_y:
        player_y = ground_y
        player_velocity_y = 0
        is_jumping = False

    # Prevent moving out of screen horizontally
    if player_x < 0:
        player_x = 0
    elif player_x > SCREEN_WIDTH - player_size:
        player_x = SCREEN_WIDTH - player_size

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
