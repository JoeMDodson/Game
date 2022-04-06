import pygame
import os
pygame.init()

simp_path = "Jimwalkforward-1.png.png"
abs_path = os.path.abspath(simp_path)

print(abs_path)

win = pygame.display.set_mode((400,400))

pygame.display.set_caption("First Game")

WalkLeft = False

walkForward = [pygame.image.load("home/runner/Game/Jimwalkfoward-1.png.png"), pygame.image.load("home/runner/Game/Jimwalkforward-2.png.png")]

x=50
y=50
width=24
height=24
vel=10

pygame.bg_color = (0, 0, 0)
clock = pygame.time.Clock()
FPS = 10

run=True
while run:
  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  keys = pygame.key.get_pressed()

  
  
  if keys[pygame.K_RIGHT] and x < 400 - width-vel:
    x +=vel
  if keys[pygame.K_LEFT] and x > vel:
    x -=vel
  if keys[pygame.K_UP] and y > vel: 
    y -=vel
  if keys[pygame.K_DOWN] and y < 400 - width - vel:
    y +=vel

  win.fill((0,0,0))
  
  pygame.draw.rect(win, (255,0,0), (x,y,width, height))
  pygame.display.update()
  clock.tick(FPS)
pygame.quit()
