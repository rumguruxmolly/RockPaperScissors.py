from random import *
rock = 1
paper = 2
scissors = 3
def saisie():
    print("play against a computer or with a friend in real life ?")
    x=input('your choice: ')
    while x.upper()!="COMPUTER" and x.upper()!="FRIEND":
        print("Can't choose that!")
        x=input('your choice: ')
    return x
x = saisie()
def saisie1():
    n = input("How many rounds would you like ?: ")
    while not n.isnumeric():
        n = input('choose another value! ')
    return n
n = int(saisie1())

def game(n,x):
    if x.upper()=="COMPUTER":
        player1= 0
        computer= 0
        for i in range(n):
            choix1 = input("player 1: ")
            while choix1.upper()!="ROCK" and choix1.upper()!='PAPER' and choix1.upper()!='SCISSORS':
                choix1= input("ERREUR! check your answer: ")
            nig = str(randint(1,3))
            if nig=="1":
                choix2="rock"
                print("computer: ", choix2)
            elif nig=="2":
                choix2="paper"
                print("computer: ", choix2)
            elif nig=="3":
                choix2="scissors"
                print("computer: ", choix2)
            while choix2.upper()==choix1.upper():
                print("TIE")
                choix1= input("player 1: ")
                while choix1.upper()!="ROCK" and choix1.upper()!='PAPER' and choix1.upper()!='SCISSORS':
                    choix1= input("ERREUR! check your answer: ")
                nig = str(randint(1,3))
                if nig=="1":
                    choix2=="rock"
                    print("computer: ", choix2)
                elif nig=="2":
                    choix2="paper"
                    print("computer: ", choix2)
                elif nig=="3":
                    choix2="scissors"
                    print("computer: ", choix2)
            if choix1.upper()=="ROCK" and choix2.upper()=="PAPER":
                computer+=1
                print("POINT TO COMPUTER")
            elif choix1.upper()=="PAPER" and choix2.upper()=="SCISSORS":
                computer+=1
                print("POINT TO COMPUTER")
            elif choix1.upper()=="SCISSORS" and choix2.upper()=="ROCK":
                computer+1
                print("POINT TO COMPUTER")
            elif choix2.upper()=="ROCK" and choix1.upper()=="PAPER":
                player1+=1
                print("POINT TO PLAYER1")
            elif choix2.upper()=="PAPER" and choix1.upper()=="SCISSORS":
                player1+=1
                print("POINT TO PLAYER1")
            elif choix2.upper()=="SCISSORS" and choix1.upper()=="ROCK":
                player1+1
                print("POINT TO PLAYER1")
            
        if player1>computer:
            print("Player1 has won!!")
        else:
            print('the computer has won!!')
    else:
        player1= 0
        player2= 0
        for i in range(n):
            choix1 = input("player 1: ")
            while choix1.upper()!="ROCK" and choix1.upper()!='PAPER' and choix1.upper()!='SCISSORS':
                choix1= input("ERREUR! check your answer: ")
            choix2 = input("player 2: ")
            while choix2.upper()!="ROCK" and choix2.upper()!='PAPER' and choix2.upper()!='SCISSORS':
                choix2= input("ERREUR! check your answer: ")
            while choix2.upper()==choix1.upper():
                print("TIE")
                choix1= input("player 1: ")
                while choix1.upper()!="ROCK" and choix1.upper()!='PAPER' and choix1.upper()!='SCISSORS':
                    choix1= input("ERREUR! check your answer: ")
                choix2 = input("player 2: ")
                while choix2.upper()!="ROCK" and choix2.upper()!='PAPER' and choix2.upper()!='SCISSORS':
                    choix2= input("ERREUR! check your answer: ")
            if choix1.upper()=="ROCK" and choix2.upper()=="PAPER":
                player2+=1
                print("POINT TO PLAYER2")
            elif choix1.upper()=="PAPER" and choix2.upper()=="SCISSORS":
                player2+=1
                print("POINT TO PLAYER2")
            elif choix1.upper()=="SCISSORS" and choix2.upper()=="ROCK":
                player2+1
                print("POINT TO PLAYER2")
            elif choix2.upper()=="ROCK" and choix1.upper()=="PAPER":
                player1+=1
                print("POINT TO PLAYER1")
            elif choix2.upper()=="PAPER" and choix1.upper()=="SCISSORS":
                player1+=1
                print("POINT TO PLAYER1")
            elif choix2.upper()=="SCISSORS" and choix1.upper()=="ROCK":
                player1+1
                print("POINT TO PLAYER1")
            
        if player1>player2:
            print("Player1 has won!!")
        else:
            print('player2 has won!!')
game(n,x)