import pygame
pygame.font.init()

screenw = 1000
screenh = 600
screen = pygame.display.set_mode((screenw, screenh))

running = True
clock = pygame.time.Clock()

Font = pygame.font.SysFont("comicsans", 20)

p1height = 50
p1width = 50
p1velocity = 5
player1 = pygame.Rect(25, (screenh/2) - (p1height/2), p1width, p1height)
p1color = "white"
p1score = 0
p1canmove = True
p1wincolor = "black"

bvelocity = 10
bullets = []
hit = False
bullet = pygame.Rect(100, 100, 5, 5)

canshoot = True

p2height = 50
p2width = 50
p2velocity = 5
player2 = pygame.Rect((screenw - p2width) - 25, (screenh/2) - (p1height/2), p1width, p1height)
p2color = "white"
p2score = 0
p2canmove = True
p2wincolor = "black"

bullets2 = []
hit2 = False
bullet2 = pygame.Rect(100, 100, 5, 5)

canshoot2 = True

gameover = False

divider = pygame.Rect((screenw/2) - 2.5, 0, 5, screenh)


def draw(player1, player2):

    p1scoretext = Font.render(f"{p1score}", True, "white")
    screen.blit(p1scoretext, ((screenw / 2) / 2, 10))
    p2scoretext = Font.render(f"{p2score}", True, "white")
    screen.blit(p2scoretext, ((screenw / 2) + (screenw / 4), 10))

    p1wintext = Font.render("Player 1 Wins!", True, p1wincolor)
    screen.blit(p1wintext, ((screenw / 4) - (p1wintext.get_width() / 2), (screenh/2) - (p1wintext.get_height() / 2)))
    p2wintext = Font.render("Player 2 Wins!", True, p2wincolor)
    screen.blit(p2wintext, (((screenw / 2) + (screenw / 4)) - (p2wintext.get_width() / 2), (screenh/2) - (p2wintext.get_height() / 2)))

    pygame.draw.rect(screen, p1color, player1)
    pygame.draw.rect(screen, p2color, player2)

    pygame.draw.rect(screen, "white", divider)

    for bullet in bullets:
        pygame.draw.rect(screen, "white", bullet)

    pygame.display.update()

    for bullet2 in bullets2:
        pygame.draw.rect(screen, "white", bullet2)

    pygame.display.update()


def playermovement():
    if keys[pygame.K_w] and player1.y != 0 and p1canmove == True:
        player1.y -= p1velocity
    if keys[pygame.K_s] and player1.y != screenh - p1height and p1canmove == True:
        player1.y += p1velocity
    if keys[pygame.K_UP] and player2.y != 0 and p2canmove == True:
        player2.y -= p2velocity
    if keys[pygame.K_DOWN] and player2.y != screenh - p2height and p2canmove == True:
        player2.y += p2velocity


while running:

    clock.tick(90)
    screen.fill("black")
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    if keys[pygame.K_d] and canshoot == True:
        for _ in range(1):
            bulx = 25 + p1width
            buly = player1.y + (p1height/2)
            bullet = pygame.Rect(bulx, buly, 5, 5)
            bullets.append(bullet)
            canshoot = False

    for bullet in bullets[:]:
        bullet.x += bvelocity
        if bullet.x > screenw:
            bullets.remove(bullet)
        elif bullet.colliderect(player2):
            bullets.remove(bullet)
            hit = True
            break

    if bullet.colliderect(divider):
        canshoot = True

    if bullet2.colliderect(divider):
        canshoot2 = True

    if keys[pygame.K_LEFT] and canshoot2 == True:
        for _ in range(1):
            bul2x = (screenw - 25) - p2width
            bul2y = player2.y + (p2height/2)
            bullet2 = pygame.Rect(bul2x, bul2y, 5, 5)
            bullets2.append(bullet2)
            canshoot2 = False

    for bullet2 in bullets2[:]:
        bullet2.x -= bvelocity
        if bullet2.x < 0:
            bullets2.remove(bullet2)
        elif bullet2.colliderect(player1):
            bullets2.remove(bullet2)
            hit2 = True
            break

    if keys[pygame.K_r] and p1canmove == False and gameover == False:
        p1color = "white"
        p2color = "white"
        p1canmove = True
        p2canmove = True
        canshoot = True
        canshoot2 = True
        hit = False
        hit2 = False
        player2.y = (screenh/2) - (p1height/2)
        player1.y = (screenh / 2) - (p1height / 2)

    if p1score == 7:
        p1wincolor = "white"
        gameover = True
    if p2score == 7:
        p2wincolor = "white"
        gameover = True

    playermovement()

    if hit2 == True:
        p1color = "red"
        p2score += 1
        canshoot = False
        canshoot2 = False
        p1canmove = False
        p2canmove = False
        bullets.clear()
        bullets2.clear()
        hit2 = False
    if hit == True:
        p2color = "red"
        p1score += 1
        canshoot2 = False
        p1canmove = False
        p2canmove = False
        canshoot = False
        bullets.clear()
        bullets2.clear()
        hit = False

    draw(player1, player2)
    pygame.display.set_caption("Pong Shooter")
    pygame.display.flip()


pygame.quit()
