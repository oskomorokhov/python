import random

class Card:

    suits = {'H':'♥','D':'♦','C':'♣','P':'♠'}
    ranks = {i:str(i) if i<11 else ['Q','K','A','J'][i%4] for i in range(2,15)}
    
    def __init__(self,rank=int,suit=str):
        self.rank = rank # 2-10,11-14(J,Q,K,A)
        self.suit = self.suits[suit] # H,D,C,P = ♥♦♣♠
    
    def __str__(self):
        s = '┌─────────┐\n'
        s+=f'| {self.ranks[self.rank]:<2}      |\n'
        s+='|         |\n'
        s+=f'|    {self.suit}    |\n'
        s+='|         |\n'
        s+=f'|      {self.ranks[self.rank]:>2} |\n'
        s+='└─────────┘'
        return s

class Deck:

    games = {'durak':{'min':6,'hand':6,'size':36},'poker':{'min':2,'hand':2,'size':52}} # durak=36,standard=52

    def __init__(self,game=str):
        if game not in self.games:
            raise ValueError('Unsupported game')
        self.game = self.games[game]
        self.deck = []
        for rank in range(self.game['min'],15):
            for suit in Card.suits.keys():
                self.deck.append(Card(rank,suit))
    
        random.shuffle(self.deck)

    def pop(self):
        return self.deck.pop()
    
    def __len__(self):
        return len(self.deck)
    
    def __str__(self):
        s ='┌───────────────┐\n'
        s+=f'| {"?":<2}            |\n'
        s+=f'|       {"?"}       |\n'
        s+=f'| {len(self):<2}         {"?":>2} |\n'
        s+='└───────────────┘'
        return s
    
    def print(self,trump=None):
        s ='┌───────────────┐\n'
        s+=f'| {"?":<2}            |\n'
        s+=f'|       {"?"}       |\n'
        s+=f'| {len(self):<2}         {"?":>2} |\n'
        s+='└──┌─────────┐──┘\n'
        s+=f'   |    {trump.suit}    |\n'
        s+='   |         |\n'
        s+=f'   |      {trump.ranks[trump.rank]:>2} |\n'
        s+='   └─────────┘'
        if len(self) > 0:
            print(s)
        elif not trump:
            print("Empty deck")
        else:
            print(trump)


class Hand:

    def __init__(self,deck,ai=False):
        self.hand = [deck.pop() for i in range(deck.game['hand'])]
        self.ai = ai

    def append(self,card):
        self.hand.append(card)
    
    def remove(self,card):
        self.hand.remove(card)
    
    def __getitem__(self,i):
        return self.hand[i]
    
    def turn(self,deck,trump,i=None):
        if len(deck) == 0 and trump == None:
            print("AI WON" if self.ai else "YOU WON")
        if self.ai:
            card = min(self.hand,key=lambda x: x.rank * 100 if x.suit==trump.suit else x.rank)
        else:
            card = self[i]
        self.remove(card)
        return card

    def __str__(self):

        hand_len = len(self.hand)
        ranks = tuple(card.ranks[card.rank] if not self.ai else '?' for card in self.hand)
        suits = tuple(card.suit if not self.ai else '?' for card in self.hand)

        s = '┌─────────┐ ' * hand_len + '\n'
        s+=('| {:<2}      | ' * hand_len).format(*ranks) + '\n'
        s+='|         | ' * hand_len + '\n'
        s+=('|    {}    | ' * hand_len).format(*suits) + '\n'
        s+='|         | ' * hand_len + '\n'
        s+=('|      {:>2} | ' *hand_len).format(*ranks) + '\n'
        s+='└─────────┘ ' * hand_len
        return s
    
    def __len__(self):
        return len(self.hand)


def show_rooster(player_hand,ai_hand,trump,deck,attack=None,defence=None):
    delimeter = max(len(ai_hand),len(player_hand))
    print(ai_hand)
    print('────────────' * delimeter)
    deck.print(trump)
    print(attack)
    print(defence)
    print('────────────' * delimeter)
    print(player_hand)


def main():
    # play game
    deck = Deck('durak')
    player_hand = Hand(deck)
    ai_hand = Hand(deck,ai=True)
    trump = deck.pop()
    done = []
    field = []
    show_rooster(player_hand,ai_hand,trump,deck)
    while len(deck)>0 and (len(player_hand)==0 or len(ai_hand) == 0):
        # start with player turn
        i = int(input(f"Select a card (1-{len(player_hand)}): "))-1
        if len(player_hand)-1 < i < 0:
            continue
        attack = player_hand.attack(deck,trump,i)
        show_rooster(player_hand,ai_hand,trump,deck,attack)
        sleep(1)
        #ai_hand.turn('defend',trump)

    
    

if __name__ == "__main__":
    main()


