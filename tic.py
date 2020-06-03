import pygame
import random
import os
import time
pygame.font.init()

MARGIN = 10
CUBE_SIZE = 170
MARGIN_SIZE = 2
WIDTH,HEIGHT = CUBE_SIZE*3+MARGIN_SIZE*2,CUBE_SIZE*3+MARGIN_SIZE*2
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe @Advait")
WIN.fill((255,255,255))

# Loading Images
TICK = pygame.image.load(os.path.join("assets","tick.png"))
CROSS = pygame.image.load(os.path.join("assets","cross.png"))

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")),(WIDTH,HEIGHT))

ICON = pygame.image.load(os.path.join("assets","icon.png"))
pygame.display.set_icon(ICON)


statement_font = pygame.font.SysFont("comicsans",40)
title_font = pygame.font.SysFont("comicsans",60)
result_font = pygame.font.SysFont("comicsans",100)


class FILL:
  def __init__(self,img,x,y):
    self.img = img
    self.x = x
    self.y = y

  def draw(self,window):
    window.blit(self.img,(self.x,self.y))





def check_if_game_is_over(winner,grid):
  
  winner,grid = check_for_winner(winner,grid)
  return winner,grid

def check_for_winner(winner,grid):

  winner,grid = check_rows(winner,grid)     #check rows 
  winner,grid = check_columns(winner,grid)    #check colomns 
  winner,grid = check_diagonals(winner,grid)    #check diagonals

  return  winner,grid


def check_rows(winner,grid):

    row_1 = grid[0][0] == grid[0][1] == grid[0][2] != "-"
    row_2 = grid[1][0] == grid[1][1] == grid[1][2] != "-"
    row_3 = grid[2][0] == grid[2][1] == grid[2][2] != "-"


  #Return the winner(X or O)
    if row_1:
      winner = grid[0][0]
      return winner,grid

    elif row_2:
      winner = grid[1][0]
      return winner,grid

    elif row_3:
      winner = grid[2][0]
      return winner,grid
    return winner,grid


def check_columns(winner,grid):

    col_1 = grid[0][0] == grid[1][0] == grid[2][0] != "-"
    col_2 = grid[0][1] == grid[1][1] == grid[2][1] != "-"
    col_3 = grid[0][2] == grid[1][2] == grid[2][2] != "-"


  #Return the winner(X or O)
    if col_1:
      winner = grid[0][0]
      return winner,grid

    elif col_2:
      winner = grid[0][1]
      return winner,grid

    elif col_3:
      winner = grid[0][2]
      return winner,grid  
    return winner,grid


def check_diagonals(winner,grid):

    dia_1 = grid[0][0] == grid[1][1] == grid[2][2] != "-"
    dia_2 = grid[0][2] == grid[1][1] == grid[2][0] != "-"
    
  #Return the winner(X or O)
    if dia_1:
      winner = grid[0][0]
      return winner,grid 

    elif dia_2:
      winner = grid[0][2]
      return winner,grid
   
    return winner,grid   


def flip_player(current_player,current_player_image):

  if current_player =="X":
    current_player = "O"
    current_player_image = TICK

  elif current_player == "O":
    current_player = "X"
    current_player_image = CROSS  
  return current_player,current_player_image    




def main():
  grid = []
  for row in range(3):
    grid.append([])
    for column in range(3):
        grid[row].append("-")  # Append a cell

  run = True
  game_is_still_going = True
  tie = False 
  winner = None     #Who won or tie
  current_player = "X"
  current_player_image = CROSS

  fill_boxes = []
  lost_count = 0
  tie_count = 0
  count = 0
  clock = pygame.time.Clock()


  def redraw_window():
    WIN.fill((255,255,255))
    for i in range(3):
      for j in range(3):
         pygame.draw.rect(WIN,(0,0,0),(j*CUBE_SIZE+j*MARGIN_SIZE,i*CUBE_SIZE+i*MARGIN_SIZE,CUBE_SIZE,CUBE_SIZE))


    for box in fill_boxes:
      box.draw(WIN)     

    if winner != None:
      lost_lable = result_font.render(f"{winner} Won",1,(255,255,255))
      pygame.draw.rect(WIN,(0,0,0),(WIDTH//2 - lost_lable.get_width()//2,HEIGHT//2,lost_lable.get_width() + 20,lost_lable.get_height()+10))   
      WIN.blit(lost_lable,(WIDTH//2 - lost_lable.get_width()//2 + 7,HEIGHT//2 + 10) )


    if count == 9 and winner == None:
      lost_lable = result_font.render("TIE",1,(255,255,255))
      pygame.draw.rect(WIN,(0,0,0),(WIDTH//2 - lost_lable.get_width()//2,HEIGHT//2,lost_lable.get_width() + 20,lost_lable.get_height()+10))
      WIN.blit(lost_lable,(WIDTH//2 - lost_lable.get_width()//2 + 7,HEIGHT//2 + 10) )    

    pygame.display.update()


  while run:
      redraw_window()
      clock.tick(60) 


      if(winner != None):
            game_is_still_going = False
            lost_count +=1

      if game_is_still_going == False:
          if lost_count > 60*3:
              run = False
          else:
              continue


      if count == 9:
        tie = True
        tie_count+=1

      if tie == True:
          if tie_count > 60*3:
              run = False
          else:
              continue        

  
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False

          elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            column = pos[0] // (CUBE_SIZE + MARGIN_SIZE//2)     # x coordinate og grid
            row = pos[1] // (CUBE_SIZE + MARGIN_SIZE//2)        # y coordinate of grid

            if grid[row][column] == "-" :
              count+=1
              grid[row][column] = current_player
              box = FILL(current_player_image,current_player_image.get_width()//2 + CUBE_SIZE*column ,current_player_image.get_width()//2 + CUBE_SIZE*row)
              fill_boxes.append(box)

              winner,grid = check_if_game_is_over(winner,grid)
              current_player,current_player_image = flip_player(current_player,current_player_image)
              print(current_player,"'s turn")
  
      

  if winner =="X" or winner == "O":
      print(winner + " won.")  

  elif winner == None :
      print("Tie")


def main_menu():

    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_lable = title_font.render("Click here to begin..",1,(255,255,255))
        my_name = statement_font.render("- Advait Shrivastava",1,(255,255,255))
        WIN.blit(title_lable,(WIDTH//2 - title_lable.get_width()//2,HEIGHT//3))
        WIN.blit(my_name,(WIDTH - my_name.get_width() - 20,HEIGHT - HEIGHT//3))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run == False
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()    
        