def treasure_island_start():
    print("Welcome to Treasure Island.\n"
          "Your mission is to find the treasure")
    first_choice = input("You have come to a fork in the road. Do you go left or right? ")
    if first_choice == "left":
        second_choice = input("You've come to a lake, do you wait for a swim or wait?")
        if second_choice == "wait":
            third_choice = input("You hop on the boat and arrive at a house with three doors\n"
                                 "a red, blue, and yellow door. Which do you choose to enter?")
            if third_choice == "yellow":
                print("You found the treasure!!!!")
            else:
                print("Game Over")
        else:
            print("Game over")
    else:
        print("Game over")


treasure_island_start()
