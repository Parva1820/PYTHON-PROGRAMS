while(True):
    direction = input("Select a Direction: ")
    match direction:
        case "U":
            print("your bike has made an U turn")
        case "R":
            print("your bike has made an RIGHT turn")
        case "L":
            print("your bike has made an LEFT turn")
        case "P":
            print("your bike has made a parking ")
        case "F":
            print("your bike has made a FORWARD direction")
        case "B":
            print("your bike has made a BACKWARD direction")
        case _:
            print("invalid selection")
            print("your bike is standing still not moving ")