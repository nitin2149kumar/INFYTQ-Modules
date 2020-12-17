#DSA-ass-23

import random
other=['J','K','Q','A']
deck=['C','D','H','S']
def generate_cards_per_type(card_type):
    #Remove pass and write your logic here
    l=[card_type+str(i) for i in [j for j in range(2,11)]+other]
    return l

def generate_card_deck():
    #Remove pass and write your logic here
    l=[]
    for i in deck:
        l.extend(generate_cards_per_type(i))
    return l

def shuffle_card_deck(cards_list):
    #Remove pass and write your logic here
    new_cards_list=cards_list.copy()
    while(new_cards_list):
       r1 = random.choice(new_cards_list)
       new_cards_list.remove(r1)
       r2 = random.choice(new_cards_list)
       new_cards_list.remove(r2)
       i1=cards_list.index(r1)
       i2=cards_list.index(r2)
       cards_list[i1]=r2
       cards_list[i2]=r1
    return cards_list

def cardSort(val):
    i=deck.index(val[0])*20
    if val[1:] in other:
        j=other.index(val[1:])+11
    else:
        j=int(val[1:])
    return (i+j)
    
def sort_cards_of_each_player(card_list):
    #Remove pass and write your logic here
    card_list.sort(key=cardSort, reverse=True)
    return card_list

def allocate_cards_to_players(cards_list):
    #Remove pass and write your logic here
    dictionary={
        'player1': [],
        'player2': [],
        'player3': [],
        'player4': []
    }
    for index,value in enumerate(cards_list):
        dictionary['player'+str((index%4)+1)].append(value)
    return dictionary

def prepare_cards():
    #Remove pass and write your logic here
    cards_list = generate_card_deck()
    new_cards_list = shuffle_card_deck(cards_list)
    dictionary= allocate_cards_to_players(new_cards_list)
    for i in range(1,5):
        dictionary['player'+str(i)]=sort_cards_of_each_player(dictionary['player'+str(i)])
    for i in range(1,5):
        if "SA" in dictionary['player'+str(i)]:
            return 'player'+str(i)

first_player=prepare_cards()
print("The first player is:",first_player)
