#CODE TO SHOW THE MOVEMENT OF THE LIFTWHEN IT IS CALLED
#GENERATING RANDOM NUMBER FOR THE CURRENT STATUS OF THE LIFT.
import random
current_status=random.randint(1,5)
print(current_status)

#MOVEMENT OF THE LIFT WHEN IT IS CALLED..
floor=int(input("ON WHICH FLOOR YOU ARE: "))
if floor==current_status:
    print("THE LIFT IS ALREADY PRESENT AT YOUR FLOOR. ")
    print("PLEASE ENTER IN THE LIFT")

elif floor < current_status:
    print("THE LIFT IS MOVING DOWN TOWARDS YOUR FLOOR. ")
    while(floor!=current_status):
        current_status-=1;
        print(current_status)
    print("PLEASE ENTER IN THE LIFT",floor)

else:
    print("THE LIFT IS MOVING up TOWARDS YOUR FLOOR. ")
    while (floor != current_status):
        current_status += 1;
        print(current_status)
    print("PLEASE ENTER IN THE LIFT",floor)

#on which floor / destination you want to go using lift
destination=int(input("ON WHICH DESTINATION YOU WANT TO GO: "))
if destination==floor:
    print("YOU ARE ALREADY PRESENT AT YOUR DESTINATION. ")
    print("PLEASE GET OUT")

elif destination < floor:
    print("THE LIFT IS MOVING DOWN TOWARDS YOUR DESTINATION. ")
    while(destination != floor):
        floor-=1;
        print(floor)

    print("you have reached to your destination",destination)

else:
    print("THE LIFT IS MOVING UP TOWARDS YOUR DESTINATION. ")
    while (destination != floor):
        floor += 1;
        print(floor)

    print("you have reached to your destination", destination)
