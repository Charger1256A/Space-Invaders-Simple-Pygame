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
enemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    EnemyX.append(random.randint(0, 735))
    EnemyY.append(random.randint(50, 150))
    EnemyX_change.append(7)
    EnemyY_change.append(10)

# Bullet

# Ready - Can't see bullet
# Fire - bullet is currently moving
BulletImg = pygame.image.load('bullet.png')
BulletX = 0
BulletY = 480
BulletY_change = 25
Bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 16, y + 10))

def iscollision(EnemyX, EnemyY, BulletX, BulletY):
    distance = math.sqrt((math.pow(EnemyX - BulletX, 2)) + (math.pow(EnemyY - BulletY, 2)))
    if distance < 29:
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
    for i in range(num_of_enemies):
        EnemyX[i] += EnemyX_change[i]

        if EnemyX[i] < 0:
            EnemyX_change[i] = 7
            EnemyY[i] += EnemyY_change[i]
        elif EnemyX[i] >= 736:
            EnemyX_change[i] = -7
            EnemyY[i] += EnemyY_change[i]

        # Collision
        collision = iscollision(EnemyX[i], EnemyY[i], BulletX, BulletY)
        if collision:
            BulletY = 480
            Bullet_state = "ready"
            score_value += 1
            EnemyX[i] = random.randint(0, 800)
            EnemyY[i] = random.randint(50, 150)

        enemy(EnemyX[i], EnemyY[i], i)

    # Bullet movement
    if BulletY <= 0:
        BulletY = 480
        Bullet_state = "ready"

    if Bullet_state is "fire":
        fire_bullet(BulletX, BulletY)
        BulletY -= BulletY_change



    player(PlayerX, PlayerY)
    show_score(textX, textY)
    pygame.display.update()