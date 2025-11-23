import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("X/O Game")
white = (225,225,225)
black = (0,0,0)
size = 200
board = [["","",""],
         ["","",""],
         ["","",""]]
player = "X"
font = pygame.font.Font(None,100,)
run = True

while run:
  screen.fill(white)
  pygame.draw.line(screen,black,(200,0),(200,600),5)
  pygame.draw.line(screen,black,(400,0),(400,600),5)
  pygame.draw.line(screen,black,(0,200),(600,200),5)
  pygame.draw.line(screen,black,(0,400),(600,400),5)
  for row in range(3):
    for col in range(3):
      if board[row][col] != "":
        # render X or O in black
        text = font.render(board[row][col], True, black)
        # blit expects a single position tuple (x, y)
        screen.blit(text, (col * size + 70, row * size + 50))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x , mouse_y = pygame.mouse.get_pos()
      # convert pixel coordinates to board indices
      row = mouse_y // size
      col = mouse_x // size
      # ensure indices are inside the 3x3 board
      if 0 <= row < 3 and 0 <= col < 3:
        if board[row][col] == "":
          board[row][col] = player
          # switch player
          if player == "X":
            player = "O"
          else:
            player = "X"
        if player == "X":
          player = "O"
        else :
          player = "X"
  pygame.display.update()
pygame.quit()  

