import pygame

# initialize Pygame
pygame.init()

# set the size of the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# set the caption of the window
pygame.display.set_caption("Super Pygame")

# set up the clock
clock = pygame.time.Clock()

# define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# set up the player
player_width = 40
player_height = 60
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
player_jump_height = 100
player_jump = False
player_jump_count = 0
player = pygame.Rect(player_x, player_y, player_width, player_height)

# set up the ground
ground_height = 50
ground = pygame.Rect(0, screen_height - ground_height, screen_width, ground_height)

# set up the obstacles
obstacle_width = 30
obstacle_height = 40
obstacle_speed = 5
obstacles = []

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_SPACE] and not player_jump:
        player_jump = True
        player_jump_count = 0

    # apply gravity to the player
    if player_jump:
        player_y -= player_jump_height - player_jump_count
        player_jump_count += 5
        if player_jump_count == player_jump_height:
            player_jump = False

    # spawn obstacles
    if len(obstacles) < 3:
        obstacle_x = screen_width + obstacle_width
        obstacle_y = screen_height - ground_height - obstacle_height
        obstacle = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        obstacles.append(obstacle)

    # move the obstacles
    for obstacle in obstacles:
        obstacle.x -= obstacle_speed

    # remove obstacles that have gone off the screen
    if obstacles:
        if obstacles[0].x < -obstacle_width:
            obstacles.pop(0)

    # check for collisions
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            pygame.quit()
            quit()

    # draw everything
    screen.fill(black)
    pygame.draw.rect(screen, white, player)
    pygame.draw.rect(screen, red, ground)
    for obstacle in obstacles:
        pygame.draw.rect(screen, white, obstacle)
    pygame.display.update()

    # set the frame rate
    clock.tick(60)

# quit Pygame
pygame.quit()
quit()
