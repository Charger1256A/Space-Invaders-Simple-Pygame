import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('space.jpg')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('alien.png')
PlayerX = 370
PlayerY = 480
PlayerX_change = 0

# Enemy
EnemyImg = pygame.image.load('enemy.png')
EnemyX = random.randint(0, 800)
EnemyY = random.randint(50, 150)
EnemyX_change = 7
EnemyY_change = 10

# Bullet

# Ready - Can't see bullet
# Fire - bullet is currently moving
BulletImg = pygame.image.load('bullet.png')
BulletX = 0
BulletY = 480
BulletY_change = 25
Bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(EnemyImg, (x, y))

def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 16, y + 10))

def iscollision(EnemyX, EnemyY, BulletX, BulletY):
    distance = math.sqrt((math.pow(EnemyX - BulletX,2)) + (math.pow(EnemyY - BulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# Game loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                PlayerX_change = -15
            if event.key == pygame.K_d:
                PlayerX_change = 15
            if event.key == pygame.K_SPACE:
                if Bullet_state is "ready":
                    BulletX = PlayerX
                    fire_bullet(BulletX, BulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                PlayerX_change = 0

    # Ensure player stays on the screen
    PlayerX += PlayerX_change

    if PlayerX < 0:
        PlayerX = 0
    elif PlayerX > 736:
        PlayerX = 736

    # Enemy movement
    EnemyX += EnemyX_change

    if EnemyX < 0:
        EnemyX_change = 7
        EnemyY += EnemyY_change
    elif EnemyX > 736:
        EnemyX_change = -7
        EnemyY += EnemyY_change

    # Bullet movement
    if BulletY <= 0:
        BulletY = 480
        Bullet_state = "ready"

    if Bullet_state is "fire":
        fire_bullet(BulletX, BulletY)
        BulletY -= BulletY_change

    # Collision
    collision = iscollision(EnemyX, EnemyY, BulletX, BulletY)
    if collision:
        BulletY = 480
        Bullet_state = "ready"
        score += 1
        print(score)

    player(PlayerX, PlayerY)
    enemy(EnemyX, EnemyY)

    pygame.display.update()