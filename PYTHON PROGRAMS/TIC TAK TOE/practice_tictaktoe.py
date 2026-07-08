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
def userinput(box,current):
    while True:
        num = input(" ENTER NUMBER (1-9): ")
        num = int(num)
        for i in range(3):
            for j in range(3):
                if box[i][j] == num:
                    box[i][j] = current
                    return

""" parva = int(input("PARVA:-ENTER THE NUMBER BETWEEN 1 TO 9: "))
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
              return """

def win_check(box, var):
    # Row check
    for i in range(3):
        if box[i][0] == var and box[i][1] == var and box[i][2] == var:
            return True

    # Column check
    for j in range(3):
        if box[0][j] == var and box[1][j] == var and box[2][j] == var:
            return True

    # cross check
    if box[0][0] == var and box[1][1] == var and box[2][2] == var:
        return True
    if box[0][2] == var and box[1][1] == var and box[2][0] == var:
        return True

    return False
def draw(box):
    for i in range(3):
        for j in range(3):
            if (box[i][j] != "X" and box[i][j] != "O"):
                return False
    return True



box = table()
current = "X"
board(box)
while True:
 userinput(box,current)
 board(box)
 if draw(box):
     print("IT IS A DRAW!!!")
     break

 if win_check(box, current):
     board(box)
     print(f"{current}  WON THE GAME!")
     break
 if current == "X":
     current = "O"
 else:
     current = "X"


