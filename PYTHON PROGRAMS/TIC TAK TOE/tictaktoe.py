def table():
    num = 1
    box = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(num)
            num += 1
        box.append(row)
    return box


def board(box):
    for i in range(3):
        for j in range(3):
            print(" ",box[i][j]," ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("-----+-----+-----")
def userinput(box):
    parva = int(input("PARVA:-ENTER THE NUMBER BETWEEN 1 TO 9: "))
    for i in range(3):
        for j in range(3):
           if box[i][j] == parva:
               box[i][j] = "X"
               return
def switch_player(box):
    player = int(input("PLAYER:-ENTER THE NUMBER BETWEEN 1 TO 9: "))
    for i in range(3):
        for j in range(3):
           if box[i][j] == player:
               box[i][j] = "O"
               return
def check_parva(box,parva):
    for i in range(3):
         if (box[i][0] == parva and
             box[i][1] == parva and
             box[i][2] == parva) or \
            (box[0][i] == parva and
             box[1][i] == parva and
             box[2][i] == parva):
             return True
    if (box[0][0] == parva and
        box[1][1] == parva and
        box[2][2] == parva) or \
       (box[0][2] == parva and
        box[1][1] == parva and
        box[2][0] == parva):
        return True
    return False
def check_player(box,player):
    for i in range(3):

         if (box[i][0] == player and
             box[i][1] == player and
             box[i][2] == player) or \
            (box[0][i] == player and
             box[1][i] == player and
             box[2][i] == player):
             return True
    if (box[0][0] == player and
        box[1][1] == player and
        box[2][2] == player) or \
       (box[0][2] == player and
        box[1][1] == player and
        box[2][0] == player):
        return True
    return False
def draw(box,parva,player):
    for i in range(3):
        for j in range(3):
            if (box[i][j] != parva and box[i][j] != player):
                return False
    return True



box = table()
board(box)
while True:
 userinput(box)
 if draw(box,parva='X',player='O'):
     print("IT IS A DRAW!!!")
     break
 check_parva(box,parva='X')
 if check_parva(box,parva='X'):
     print("PARVA WIN!")
     break
 board(box)
 switch_player(box)
 check_player(box,player='O')
 if check_player(box,player='O'):
     print("PLAYER WIN!")
     break
 board(box)


