import random

money = 100

#Write your game of chance functions here

def coinFlip(choice, bet):

    print("You are about to play heads or tails and bet £{} that it is {}".format(bet, choice))
    # coin toss
    num = random.randint(1, 2)
    if (num == 1):
        coin = "Heads"
    else:
        coin = "Tails"

    # compare choice to coin
    if (choice == coin):
        print("It's {}...You win!".format(coin))
        return bet * 2 
    else:
        print("It's {}...You lose!".format(coin))
        return bet * -1


def choHan(choice, bet):
    print("You are about to play choHan and bet £{} that it is {}".format(bet, choice))

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    sumOfDice = die1 + die2

    # sum is even or odd 
    if (sumOfDice % 2 == 0):
        result = "Even"
    else: 
        result = "Odd"
    
    if (choice == result):
        print("The sum of the dice is {}...You win!".format(result))
        return bet * 2 
    else:
        print("The sum of the dice is {}...You lose!".format(result))
        return bet * -1


def higherCard(bet):
    print("You are about to play higher card and bet £{} that your card is higher".format(bet))

    # number relates to card
    # assuming ace high, highest number is 12 (ace), lowest number is 0 (two)
    cardsInDeck = []

    # build deck
    for suit in range(4):
        for card in range(13):
            cardsInDeck.append(card)

    # player 1 picks out a card randomly
    player1Card = random.choice(cardsInDeck)
    print("You pick {}".format(player1Card))

    # remove card from deck
    cardsInDeck.remove(player1Card)

    # player 2 picks out a card randomly
    player2Card = random.choice(cardsInDeck)
    print("The other player picks {}".format(player2Card))

    if (player1Card == player2Card):
        print("It's a draw!")
        return bet
    elif (player1Card > player2Card):
        print("Your card is higher...You win!")
        return bet * 2
    else:
        print("Your card is lower...You lose!")
        return bet * -1


def roulette(choice, bet):
    print("You are about to play roulette and bet £{} that it is {}".format(bet, choice))

    # 37 = 0, 38 = 00
    num = random.randint(1, 38)
    
    if (num % 2 == 0 & num <= 36):
        value = "Even"
    elif (num % 2 == 1 & num <= 36):
        value = "Odd"
    elif (num == 37):
        value = "0"
    else: # num == 38
        value = "00"


    if (choice == "Even" or choice == "Odd"):

        if (choice == value and num <= 36):
            print("Number {} is {}...You win!".format(num, value))
            return bet * 2
        else:
            print("Number {} is {}...You lose!".format(num, value))
            return bet * -1

    elif (choice ==  "0" or choice == "00"):

        if (choice == value):
            print("You chose {} and you landed on {}.. you win!".format(choice, value))
            return bet * 36
        else:
            print("You chose {} and you landed on {}.. you lose!".format(choice, value))
            return bet * -1
    
    elif (choice >= 1 and choice <= 36):

        if (choice == num):
            print("The ball lands on your chosen number {}...You win!".format(choice))
            return bet * 36
        else: 
            print("The ball lands on {} but your chosen number is {}...You lose!".format(num, choice))
            return bet * -1



#Call your game of chance functions here

print("You have £{}".format(money))
print("\n")

money += coinFlip("Heads", 20)
print("You now have £{}".format(money))
print("\n")

money += choHan("Even", 20)
print("You now have £{}".format(money))
print("\n")

money += higherCard(20)
print("You now have £{}".format(money))
print("\n")

money += roulette("0",20)
print("You now have £{}".format(money))

