import random
#create try again variable for whle loop
try_again = 'yes'
#set up variables for possible moves
moves = {1:'Rock',2:'Paper',3:'Scissors'}
#set up user choice input and pc pick
user_choice = int(input('Please choose:\n1) rock\n2) paper\nor\n3) scissors\n'))
pc_choice = random.randint(1,3)
#set up win count variables
user_wins = 0
pc_wins = 0
ties = 0

#loop for actual game
while try_again.lower() == 'yes' or try_again.lower() =='y':
    #output choices to screen
    print('You chose ' + moves.get(int(user_choice)))
    print('The computer chose ' + moves.get(int(pc_choice)))
    if user_choice == pc_choice:
        ties +=1
        input('Tied. Please choose again:\n1) rock\n2) paper\nor\n3) scissors\n')
        pc_choice = random.randint(1,3)
    elif (user_choice == 1 and pc_choice == 3) or (user_choice == 2 and pc_choice == 1) or (user_choice == 3 and pc_choice == 2):
        print('You win')
        user_wins +=1
        try_again = input('Do you want to play again? ')
        if try_again =='yes' or try_again == 'y':
            user_choice = int(input('Please choose:\n1) rock\n2) paper\nor\n3) scissors\n'))
            pc_choice = random.randint(1,3)

    else:
        print('You lose') 
        pc_wins +=1
        try_again = input('Do you want to play again? ')
        if try_again =='yes' or try_again == 'y':
                user_choice = int(input('Please choose:\n1) rock\n2) paper\nor\n3) scissors\n'))
                pc_choice = random.randint(1,3)
#output results
print('Game Results\n')
print('You won %d games' % (user_wins))
print('The computer won %d games' % (pc_wins))
print('There were %d ties' %(ties))

