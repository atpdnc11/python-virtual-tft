import pygame
import math
import time

# Constants
WIDTH, HEIGHT = 320, 240
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = min(CENTER_X, CENTER_Y) - 10

# Initialize Pygame
pygame.init()

# Create the virtual TFT display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual TFT ILI9341")

# Function to draw the clock face
def draw_clock_face():
    pygame.draw.circle(screen, (255, 255, 255), (CENTER_X, CENTER_Y), RADIUS, 2)

    for i in range(12):
        angle = i * math.pi / 6
        x1 = CENTER_X + int(math.cos(angle) * (RADIUS - 5))
        y1 = CENTER_Y + int(math.sin(angle) * (RADIUS - 5))
        x2 = CENTER_X + int(math.cos(angle) * (RADIUS - 15))
        y2 = CENTER_Y + int(math.sin(angle) * (RADIUS - 15))
        pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 2)

# Function to draw clock hands
def draw_clock_hands(seconds, minutes, hours):
    draw_hand(seconds, 60, 2, (255, 0, 0))
    draw_hand(minutes, 60, 4, (0, 255, 0))
    draw_hand(hours * 5 + minutes // 12, 60, 6, (0, 0, 255))

# Function to draw a clock hand
def draw_hand(value, range, length, color):
    angle = math.radians(value * 360 / range - 90)
    x2 = CENTER_X + int(math.cos(angle) * (RADIUS - length))
    y2 = CENTER_Y + int(math.sin(angle) * (RADIUS - length))
    pygame.draw.line(screen, color, (CENTER_X, CENTER_Y), (x2, y2), 4)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get current time
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour % 12

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw clock face and hands
    draw_clock_face()
    draw_clock_hands(seconds, minutes, hours)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(1)

# Quit Pygame
pygame.quit()
