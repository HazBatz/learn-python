import pygame
from sys import exit

pygame.init()

# --- Setup screen ---

# --- Health class ---
class Health:
    def __init__(self, max_health):
        self.max_health = max_health
        self.current_health = max_health
        self.bar_length = 200
        self.bar_height = 20
        self.health_color = (0, 255, 0)
        self.bg_color = (255, 0, 0)
        self.position = (20, 20)

    def take_damage(self, amount):
        self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, (*self.position, self.bar_length, self.bar_height))
        health_ratio = self.current_health / self.max_health
        current_bar_length = self.bar_length * health_ratio
        pygame.draw.rect(surface, self.health_color, (*self.position, current_bar_length, self.bar_height))



screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Nexo Knight Platformer")
clock = pygame.time.Clock()
FPS = 60

# --- Game control variables ---
run = True
doubleJumpUnlocked = True  # Change to False if you want to disable double jump


# --- NexoKnight Player Class ---
class NexoKnight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load images
        self.player_walk = [
            pygame.image.load('resources/walk1.png').convert_alpha(),
            pygame.image.load('resources/walk2.png').convert_alpha()
        ]
        self.jump_img = pygame.image.load('resources/jump.png').convert_alpha()
        self.double_jump_img = pygame.image.load('resources/double_jump.png').convert_alpha()

        # Setup animation
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))

        # Movement physics
        self.gravity = 0
        self.jumping = False
        self.jumpCount = 0
        self.time = 0
        self.timer = False
        self.yVel = 0
        self.GRAVITY = 1

        # Sound
        self.walking_sound = pygame.mixer.Sound("resources/walk.wav")

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.jumping = False
            self.jumpCount = 0

    def jump(self):
        if not self.jumping:
            self.gravity = -20
            self.jumping = True
            self.jumpCount = 1
            self.image = self.jump_img
            self.timer = True

    def double_jump(self):
        if self.jumpCount == 1 and self.time > 10:
            self.gravity = -20
            self.jumpCount = 2
            self.image = self.double_jump_img
            self.timer = False
            self.time = 0

    def loop(self):
        if self.timer:
            self.time += 1

    def update(self):
        self.apply_gravity()
        self.loop()


# --- Create player instance ---
player = NexoKnight()
player_group = pygame.sprite.GroupSingle(player)


# --- Game loop ---
while run:
    clock.tick(FPS)
    screen.fill('skyblue')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE, pygame.K_UP]:
                if player.jumpCount < 1:
                    player.jump()
                elif doubleJumpUnlocked and player.jumpCount == 1:
                    player.double_jump()

    # Update + draw
    player_group.update()
    player_group.draw(screen)

    pygame.display.update()

pygame.quit()
exit()
