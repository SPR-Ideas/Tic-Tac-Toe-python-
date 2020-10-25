#tic tac toe using python
#by PRADEEP RAGUL S
#NON-GRAPHICAL PROGRAM. 


board = ["-","-","-","-","-","-","-","-","-"]
import os
postions_avilable=[1,2,3,4,5,6,7,8,9]
game_counter=0
position=0

#function for showning the board

def show_board():
    clear()
    for i in range(5):
        print()
    print("                          ",end="")
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("                          ",end="")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("                          ",end="")
    print(board[6]+" | "+board[7]+" | "+board[8])
    for i in range(5):
        print()


def clear():
    if(os.name == "posix" ):
        os.system("clear")
    else:
        os.system("cls")
def check_pos(post):
    if(board[post-1] == "-"):
        return True
    else:
        return False

def get_pos():
    global postions_avilable
    try:
        post = int(input("Enter position : "))
    except ValueError :
        post=0

    while post not in postions_avilable:
        try:
            post = int(input("Enter position : "))
        except ValueError :
            post=0
    check_pos(post)
    postions_avilable.remove(post)
    return post

def swap_player(g):
    if(g%2==0):
        print("                          ",end="")
        print("player X turn ")
        for i in range(5):
            print()
        return "X"
    else:
        print("                          ",end="")
        print("player O turn ")
        for i in range(5):
            print()
        return "O"

def check_win():
    if(check_row()):
        return True
    elif (check_coloum()):
        return True
    elif(check_diagonal()):
        return True
    else:
        False


def check_row():
    global board
    if((board[0]==board[1]==board[2]=="X") or (board[0]==board[1]==board[2]=="O")):
        return True
    elif((board[3]==board[4]==board[5]=="X") or (board[3]==board[4]==board[5]=="O")):
        return True
    elif((board[6]==board[7]==board[8]=="X") or (board[6]==board[7]==board[8]=="O")):
        return True
    else:
        return False


def check_coloum():
    global board
    if ((board[0]==board[3]==board[6]=="X") or (board[0]==board[3]==board[6]=="O")):
        return True
    elif((board[1]==board[4]==board[7]=="X") or (board[1]==board[4]==board[7]=="O")):
        return True
    elif ((board[2]==board[5]==board[8]=="X") or (board[2]==board[5]==board[8]=="O")):
        return True
    else:
        return False


def check_diagonal():
    global board
    if ((board[0]==board[4]==board[8]=="X") or (board[0]==board[4]==board[8]=="O")):
        return True
    elif ((board[2]==board[4]==board[6]=="X") or (board[2]==board[4]==board[6]=="O")):
        return True
    else:
        return False


clear()
player1=input("Enter player X name : ")
player2= input("Enter player O name: ")


while (1):

    show_board()
    value=swap_player(game_counter)
    print("postions avilable ",postions_avilable)
    position=get_pos()
    board[position-1]=value
    game_counter+=1
    if(check_win()):
        show_board()
        if (value == "X"):
            print("                          ",end="")
            print("player "+player1+" wins")
            for i in range (5):
                print()
        else:
            print("                          ",end="")
            print("player "+player2+" wins")
            for i in range (5):
                print()
        break

    if (game_counter == 9 ):
        show_board()
        print("                          ",end="")
        print(" match draw ")
        for i in range (5):
            print()
        break
