#car game
car_condition="stop"

while True:
    command=input("command your car!! ")
    if command=="start":
        if car_condition=="car is moving":
            print("the car arleady started")
            continue
        print("the car has started")
        car_condition="car is moving"
        continue
    elif command=="stop":
        if car_condition=="car stopped":
            print("the car arleady stopped")
            continue
        print("you stopped your car")
        car_condition="car stopped"
        continue
    elif command=="help":
        print("""
            start:start the car
            stop:stop the car
            help:get help of game
            exit:exit the game""")
        continue
    elif command=="exit":
        break
    else:
        print("""your command is not valid
                type help to get help about the game""")
        continue
