print('Welcome to play Blackjack')

import random
import time
SPADES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
HEARTS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
DIAMONDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CLUBS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Cards = {'♠️': SPADES, '♥️': HEARTS, '♦️': DIAMONDS, '♣️': CLUBS} 

# confirm the numbers of player
def numbers_of_player():
    check_point = 0
    while check_point == 0:
        numbers_of_player=input('How many players will join the game? ')
        try:
            int(numbers_of_player)
            if int(numbers_of_player) > 7:
                print('Number of players must be less than 7.')
                continue
        except:
            print('Please enter a number.')
            continue
        check_players=input('Check the numbers of players. Players: {}\n(y/n). '.format(int(numbers_of_player)))
        if check_players == 'Y' or check_players == 'y':
            check_point += 1
            return int(numbers_of_player)
        elif check_players == 'N' or check_players == 'n':
            continue
        else:
            check_point += 2
            while check_point == 2:
                check_players = input('Please enter " Y " or " N ". ')
                if check_players == 'Y' or check_players == 'y':
                    check_point -= 1
                    return int(numbers_of_player)
                elif check_players == 'N' or check_players == 'n':
                    check_point -= 2
                else:    
                    continue

Numbers_of_player = numbers_of_player()

# (list) nick name 
def name_of_players():
    names_of_player = ['dealer']
    print('Please enter your nickname')
    for i in range(Numbers_of_player): 
        names_of_player.append(input('player {}: '.format(i+1)))
    return names_of_player

Name_of_players = name_of_players()

# (list) players
list_Name_of_players = []
for i in range(Numbers_of_player + 1): # including dealer
    list_Name_of_players.append('player{}'.format(i))

# deal the card
def deal():
    check_point = 0
    dealed_card = []
    while check_point == 0:
        try:
            points = random.randint(0, 12)
            suit = random.choice(list(Cards.keys()))
            dealed_point = Cards[suit].pop(points)
            dealed_card.append([suit, dealed_point])
            check_point += 1
        except:
            continue
    return dealed_card

# all_status 
def all_status():
    for i in range(Numbers_of_player + 1): # including dealer
        print(Name_of_players[i],':',list_Name_of_players[i])

# calculate_points
def calculate_points(i):
    if list_Name_of_players[i][-1] == 'PASS':
        list_Name_of_players[i].pop()
    sum = 0
    for card in list_Name_of_players[i]:
        try:
            sum += int(card[1])
        except:
            if card[1] == 'A':
                sum += 11
            elif card[1] == 'J' or card[1] == 'Q' or card[1] == 'K':
                sum += 10
    if sum > 21:
        sum = 0
        for card in list_Name_of_players[i]:
            try:
                sum += int(card[1])
            except:
                if card[1] == 'A':
                    sum += 1
                elif card[1] == 'J' or card[1] == 'Q' or card[1] == 'K':
                    sum += 10
    return sum

# first round
def first_round():
    for i in range(len(list_Name_of_players)):
        list_Name_of_players[i] = []
        for card in deal():
            list_Name_of_players[i].append(card)
        for card in deal():
            list_Name_of_players[i].append(card)
    for i in range(1, 101):
        print('\r' + 'dealing the card {} % '.format(i) + '.' * (i // 4) ,end = '')
        time.sleep(0.025)
    print('\n')
    all_status()
    time.sleep(0.5)
    return list_Name_of_players 

# subsequential round
def other_round():
    check_point = 0
    while check_point < len(list_Name_of_players):
        for i in range(len(list_Name_of_players)):
            if i == 0:
                sum = 0
                if 'PASS' == list_Name_of_players[i][-1]:
                    continue
                else:
                    sum = calculate_points(i)
                    if sum <= 17 and len(list_Name_of_players[0]) < 5:
                            for card in deal():
                                list_Name_of_players[0].append(card)
                    else:
                        list_Name_of_players[0].append('PASS')
                        check_point += 1
            else:
                if 'PASS' == list_Name_of_players[i][-1]:
                    continue
                else:
                    check_point1 = 0
                    while check_point1 == 0:
                        if len(list_Name_of_players[i]) == 5:
                            list_Name_of_players[i].append('PASS')
                            check_point += 1
                            check_point1 += 1
                            continue
                        print('\n')
                        print(Name_of_players[i],'your current cards:',list_Name_of_players[i])
                        answer = input('Would you want to get a deal?\n(y/n)')                     
                        if answer == 'Y' or answer == 'y':
                            check_point1 += 1
                            for card in deal():
                                list_Name_of_players[i].append(card)
                            for x in range(1, 101):
                                print('\r' + 'dealing the card {} % '.format(x) + '.' * (x // 4) ,end = '')
                                time.sleep(0.0125)
                            print('')
                            print(Name_of_players[i],':',list_Name_of_players[i])
                        elif answer == 'n' or answer == 'N':
                            list_Name_of_players[i].append('PASS')
                            check_point += 1
                            check_point1 += 1
                        else:
                            print('{} please answer "Y" or "N".'.format(Name_of_players[i]))
                            continue
    print('\nTHIS ROUND:')
    all_status()

# show the winner
def the_winner():
    list_points = []
    print('\n')
    for a in range(1, 101):
        print('\r' + 'calculating the points {} % '.format(a) + '.' * (a // 4) ,end = '')
        time.sleep(0.025)
    print('\n')
    for i in range(len(list_Name_of_players)):
        list_Name_of_players[i].append('TOTAL POINTS: {}'.format(calculate_points(i)))
        list_points.append(calculate_points(i))
        print(Name_of_players[i],':',list_Name_of_players[i])
    winners = ['None']
    points_winner = 1
    five_cards_points_winner = 1
    five_cards_check = 0
    for i in range(len(list_Name_of_players)):
        if list_points[i] <= 21 and (len(list_Name_of_players[i])-1) == 5:
            five_cards_check += 1
            if list_points[i] > five_cards_points_winner:
                winners[0] = Name_of_players[i]
                five_cards_points_winner = list_points[i]
            elif list_points[i] == five_cards_points_winner:
                winners.append(Name_of_players[i])
            else:
                continue
        elif five_cards_check == 0 and list_points[i] <= 21:
            if list_points[i] > points_winner:
                winners[0] = Name_of_players[i]
                points_winner = list_points[i]
            elif list_points[i] == points_winner:
                winners.append(Name_of_players[i])
        else:
            continue
    print('========')
    if winners[0] == 'None':
        return print('There is no winner in this round.')
    elif len(winners) == 1:
        return print('The winner is {}.'.format(winners[0]))
    elif len(winners) == 2:
        return print('The winners are {} and {}.'.format(winners[0], winners[1]))
    elif len(winners) == 3:
        return print('The winners are {}, {} and {}.'.format(winners[0], winners[1], winners[2]))

# Game start
game_check_point = 0
while game_check_point == 0:
    first_round()
    other_round()
    the_winner()
    print('========\n')
    round_check = 0
    while round_check == 0:
        continue_check = input('Continue?\n(y/n)')
        if continue_check == 'y' or continue_check == 'Y':
            round_check += 1
            print('\n')
            continue
        elif continue_check == 'n' or continue_check == 'N':
            round_check += 1
            game_check_point += 1
        else:
            print('Please enter "Y" or "N".')
