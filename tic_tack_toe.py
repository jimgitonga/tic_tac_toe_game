board=[" " for i in range(16)]

def  print_board():
    row1="| {} |   | {} |   | {} |".format(board[0],board[1],board[2],board[3])
    row2="| {} |   | {} |   | {} |".format(board[4],board[5],board[6],board[7])
    row3="| {} |   | {} |   | {} |".format(board[8],board[9],board[10],board[11])
    row4="| {} |   | {} |   | {} |".format(board[12],board[13],board[14],board[15])

    print()
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print()

def player_move(icon):
    
    if icon=="X":
        number=1
    elif icon=="O":
        number=2
    print("its your turn player {}".format(number))
    choice=int(input('between (1-9) choose :').strip())
    if board[choice-1]==" ":
        board[choice-1]=icon
    else:
        print()
        print ('all spaces taken')
def is_victory(icon):
    if (board[0]==icon and board[1]==icon and board[2]==icon and board[3]==icon)  or \
       (board[0]==icon and board[4]==icon and board[8]==icon  and board[12]==icon)or  \
       (board[1]==icon and board[5]==icon and board[9]==icon and board[13]==icon)or   \
       (board[2]==icon and board[6]==icon and board[10]==icon and board[14]==icon)or    \
       (board[3]==icon and board[7]==icon and board[11]==icon and board[15]==icon)or     \
       (board[4]==icon and board[5]==icon and board[6]==icon and board[7]==icon)or      \
       (board[8]==icon and board[9]==icon and board[10]==icon and board[11]==icon)or       \
       (board[12]==icon and board[13]==icon and board[14]==icon and board[15]==icon) or \
       (board[0]==icon and board[5]==icon and board[10]==icon and board[15]==icon)  or \
       (board[3]==icon and board[6]==icon and board[9]==icon and board[12]==icon):
        
       
        return True
    else :
        return False
def is_draw():
    if " " not in board:
        return True
    else:
        return False
while True:
        
        print_board()
        player_move("X")
        print_board
        if is_victory("X"):
            print("player X won")
            break
        elif is_draw():
            print("is a draw!")
            break
        player_move("O")
        if is_victory("O"):
            print_board()
            print("player O wins")
            break
        elif is_draw():
            print("is a draw")
            break
    
