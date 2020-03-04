#Coin Toss Main

from coin import Coin

def main():
    # Create an object from the Coin class.
    coin1 = Coin()
    coin2 = Coin()

    answer = input("Would you like to continue? (y/n): ").lower()
    while answer == "y":
        coin1.toss()
        coin2.toss()

        if coin1.get_sideup() == coin2.get_sideup():
            coin2.set_amount(1)
            coin1.set_amount(-1)
            print("Player 2 Wins!")
        else:
            coin2.set_amount(-1)
            coin1.set_amount(1)
            print("Player 1 Wins!")
     
        # Object calling the function of class.
        print("Player 1 tossed a",coin1.get_sideup(),"and Player 2 tossed a", coin2.get_sideup())
        answer = input("\n\nWould you like to continue? ").lower()

    #print amounts
    print("\n\nPlayer1:", coin1.get_amount(),"cents", " |  Player2:", coin2.get_amount(), "cents")

main()
