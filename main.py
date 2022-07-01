'''
import random
import pygame
import sys
pygame.init()
pygame.display.init()



black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
turq = (0, 123, 64)
X = 600
Y = 350
display_surface = pygame.display.set_mode([X, Y])
display_surface.fill(white)
pygame.display.set_caption('Show Text')
pygame.display.update()

font = pygame.font.Font(None, 32)
text = font.render('Mastermind', True, green)
textRect = text.get_rect()
textRect.center = (300, 160)

font = pygame.font.Font(None, 32)
text2 = font.render('Press 1 to play', True, blue)
text2Rect = text2.get_rect()
text2Rect.center = (300, 190)

font = pygame.font.Font(None, 32)
text3 = font.render('Press 2 for rules', True, turq)
text3Rect = text3.get_rect()
text3Rect.center = (300, 220)

while startscreen == True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        startcode = True
        startscreen = False
      if event.key == pygame.K_2:
        rulecode = True
        startscreen = False
  pygame.display.update()
  display_surface.fill(white)
  display_surface.blit(text, textRect)
  display_surface.blit(text2, text2Rect)
  display_surface.blit(text3, text3Rect)

if rulecode == True:
  font = pygame.font.Font(None, 15)
  text4 = font.render('This is Mastermind. You are trying to guess a 4-digit code using digits 1-8.', True, black)        
  text6 = font.render('"White" represents that one of the inputted digits is in the code you are trying to guess, but in the wrong place.', True, black) 
  text7 = font.render('"Black" represents that one of the inputted digits is in the code you are trying to guess, and in the right place', True, black)
  text4Rect = text4.get_rect()
  text4Rect.center = (300, 70)
  text6Rect = text6.get_rect()
  text6Rect.center = (300, 85)
  text7Rect = text7.get_rect()
  text7Rect.center = (300, 100)

  font = pygame.font.Font(None, 32)
  text5 = font.render('Press 3 to play', True, blue)
  text5Rect = text5.get_rect()
  text5Rect.center = (300, 250)

  while rulecode == True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_3:
          rulecode = False
          startcode = True
    pygame.display.update()
    display_surface.fill(white)
    display_surface.blit(text4, text4Rect)
    display_surface.blit(text5, text5Rect)
    display_surface.blit(text6, text6Rect)
    display_surface.blit(text7, text7Rect)

'''
'''
first, print the user input all nice and neatly at the top
then print the number of whites and blacks next to it

then repeat, and count game as fail if take 9 tries
'''
import random
print("This is Mastermind. You are trying to guess a 4-digit code using digits 1-8. 'White' represents that one of the inputted digits is in the code you are trying to guess, but in the wrong place. 'Black' represents that one of the inputted digits is in the code you are trying to guess, and in the right place.")
startcode = True
rulecode = False
startscreen = True
win = False
a = 4
tries = 0

while startcode == True:

  gamecode = []
  while len(gamecode) != 4:
    digit = random.randint(1,8)
    if not str(digit) in gamecode:
      gamecode.append(str(digit))

  def check(place, x, y, z):
    global white
    global black
    if usercode[place] == gamecode[x] or usercode[place] == gamecode[y] or usercode[place] == gamecode[z]:
      white += 1
    if usercode[place] == gamecode[place]:
      black += 1  

  while win == False:
    print()
    usercode = input("Enter a non-repeating 4-digit code using digits 1-8: ")
    usercode.split()
    usercode = list(usercode)
  
    if usercode[0] != usercode[1] != usercode[2] != usercode[3] and len(usercode) == 4 and str(0) not in usercode and str(9) not in usercode:
    
      tries += 1
      white = 0
      black = 0
      check(0, 1, 2, 3)
      check(1, 0, 2, 3)
      check(2, 0, 1, 3)
      check(3, 0, 1, 2)

      print(str(white) + " whites")
      print(str(black) + " blacks")
      if black >= 4:
        print()
        print("You won in " + str(tries) + " tries!")
        win = True
    else:
      print("Error. Code has incorrect length, repeating digits, and/or digits 0 or 9.")