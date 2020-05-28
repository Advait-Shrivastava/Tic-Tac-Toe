#board
#display board
# play game
#handle turn
#check Win
  #check Row
  #check Column
  #check diagonals
#check tie
#flip player

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]


game_is_still_going = True


#Who won or tie

winner = None


#Who's  turn is it

current_player = "X"


def display_board():
  print(board[0]+" | "+board[1]+" | "+ board[2])
  print(board[3]+" | "+board[4]+" | "+ board[5])
  print(board[6]+" | "+board[7]+" | "+ board[8])    


def play_game():
  
  #display_board()
  display_board()    



  #while the game is still going

  while game_is_still_going : 
    

    # handle a single turn of the arbitrary player
    handle_turn(current_player) 


    #check is the game has ended
    check_if_game_is_over()


    #Flip to the other player
    flip_player()

  #The game has ended

  if winner =="X" or winner == "O":

    print(winner + " won.")  

  elif winner == None :
    print("Tie")  


# handle a single turn of the arbitrary player
def handle_turn(player):  

  

  print()
  print(player+"'s turn : ")

  position = input("Choose a position from 1-9 : ")
  print()

  valid = False

  while not valid:

   while position not in ["1","2","3","4","5","6","7","8","9"]:
    print("Invalid Input!")
    position = input("Choose a position from 1-9 : ")
    print()

   position = int(position) - 1


   if board[position] =="-":
    valid = True

   else:  
    print("Position already entered!")

  board[position] = player

  display_board()

#check is the game has ended1\
def check_if_game_is_over():
  
  check_for_winner()
  check_if_tie()

def check_for_winner():

  #set of global variables

  global winner


  #check rows
  row_winner = check_rows()
  #check colomns
  column_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()


  if row_winner:
    #there was a win

    winner = row_winner

  elif column_winner:
    #ther was a win
    winner = column_winner

  elif diagonal_winner:
    #there was a win
    winner = diagonal_winner

  else:
    #there was a win   

    winner = None 

  return


def check_rows():

  global game_is_still_going

  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"


  if row_1 or row_2 or row_3:
    game_is_still_going = False


  #Return the winner(X or O)
  if row_1:
    return board[0]  

  elif row_2:
    return board[3]

  elif row_3:
    return board[6]    
  return




def check_columns():

  global game_is_still_going

  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-"


  if col_1 or col_2 or col_3:
    game_is_still_going = False


  #Return the winner(X or O)
  if col_1:
    return board[0]  

  elif col_2:
    return board[1]

  elif col_3:
    return board[2]    
  return




def check_diagonals():

  global game_is_still_going

  dia_1 = board[0] == board[4] == board[8] != "-"
  dia_2 = board[2] == board[7] == board[6] != "-"
  


  if dia_1 or dia_2:
    game_is_still_going = False


  #Return the winner(X or O)
  if dia_1:
    return board[0]  

  elif dia_2:
    return board[2]
   
  return  





def check_if_tie():

  global game_is_still_going

  if "-" not in board:
    game_is_still_going = False

  return


def flip_player():

  global current_player

  if current_player =="X":
    current_player = "O"

  elif current_player == "O":
    current_player = "X"  

  return 




play_game()  