cross_road = input("Your at cross road. Where do you like to go? Type \"left\" or \"right\": ")

match cross_road:
    case "left":
        lake = input("You Come to a lake. there is an island in the middle of the lake. type \"wait\" to wait for a boat. Type \"swim\" to swim across.: ")
        match lake:
            case "wait":
                house = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose: ")
                match house:
                    case "red":
                        print("Game Over")
                    case "yellow":
                        print("You located the treasure :-)")
                    case "blue":
                        print("Game Over")

                    case _:
                        print("Input Invalid")                        
            case "swim":
                print("Game Over")

            case _:
                print("Input Invalid")
    case "right":
        print("Game Over")
    case _:
        print("Input Invalid")
