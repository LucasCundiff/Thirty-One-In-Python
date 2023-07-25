import random
import standard_cards as cards
import name_generator as ng


class Player:
    hand = []
    player_name = ""
    is_npc = False
    has_knocked = False

    def __init__(self, name, npc):
        self.player_name = name
        self.is_npc = npc
        self.hand = []
        self.has_knocked = False

    def __str__(self):
        return self.player_name

    def has_31(self):
        return determine_score(self.hand) == 31


HAND_SIZE = 3
CURRENT_PLAYER_INDEX = 0
PLAY_DECK = cards.get_deck_copy()
DISCARD_PILE = []
PLAYERS = []

opponent_knock_chance = {
    25: 40,
    26: 50,
    27: 60,
    28: 70,
    29: 80,
    30: 90
}


def main():
    game_intro()
    player_intro()
    setup_game_start()
    run_game()


def game_intro():
    print("Welcome to 31 in python!")
    user_setup()
    create_opponents(determine_opponent_count())


def user_setup():
    while True:
        new_player_name = input("Please enter your name: ")
        if len(new_player_name) == 0:
            print("Please enter at least one character for your name")
        else:
            player = Player(new_player_name, False)
            PLAYERS.append(player)
            break


def determine_opponent_count():
    while True:
        opponent_count = input("How many opponents would you like? (1-3): ")
        try:
            oc_int = int(opponent_count)
        except ValueError:
            print("please enter an integer between 1 and 3")
        else:
            if 0 < oc_int < 4:
                break
            else:
                print("please enter an integer between 1 and 3")
    return oc_int


def create_opponents(opponent_count):
    x = 0
    while x < opponent_count:
        new_opponent_name = ng.get_name()
        new_opponent = Player(new_opponent_name, True)
        PLAYERS.append(new_opponent)
        x += 1


def player_intro():
    print("---------------------------------------")
    print(f"Ok {PLAYERS[0]}, you'll be playing against")
    for x in PLAYERS:
        if x.is_npc:
            print(x)
    print("---------------------------------------")


def setup_game_start():
    random.shuffle(PLAY_DECK)
    for x in PLAYERS:
        deal_starting_hand(x.hand)

    DISCARD_PILE.append(draw_card())


def deal_starting_hand(hand):
    if len(hand) > 0:
        hand = []
    while len(hand) < HAND_SIZE:
        hand.append(draw_card())


def run_game():
    global CURRENT_PLAYER_INDEX
    CURRENT_PLAYER_INDEX = random.choice(range(4))
    print(f"{PLAYERS[CURRENT_PLAYER_INDEX]} is going first!")
    while True:
        if PLAYERS[CURRENT_PLAYER_INDEX].has_knocked:
            break
        else:
            print(f"Top of discard is a {top_discard()}")

        if PLAYERS[CURRENT_PLAYER_INDEX].is_npc:
            opponent_turn()
        else:
            user_turn()

        if PLAYERS[CURRENT_PLAYER_INDEX].has_31():
            print(f"{PLAYERS[CURRENT_PLAYER_INDEX]} has 31! Round over")
            break

        if CURRENT_PLAYER_INDEX >= len(PLAYERS) - 1:
            CURRENT_PLAYER_INDEX = 0
        else:
            CURRENT_PLAYER_INDEX += 1

    game_over()


def opponent_turn():
    print("---------------------------------------")
    low_card = get_lowest_card(PLAYERS[CURRENT_PLAYER_INDEX].hand, top_discard())
    if low_card == top_discard():
        if not opponent_knock_check():
            opponent_draw_from_deck()
    else:
        opponent_pickup_discard(low_card)


def opponent_knock_check():
    current_score = determine_score(PLAYERS[CURRENT_PLAYER_INDEX].hand)
    if current_score in opponent_knock_chance and not any_player_knocked():
        knock_roll = random.choice(range(100))
        if knock_roll < opponent_knock_chance[current_score]:
            knock()
            print("---------------------------------------")
            return True
        else:
            return False


def opponent_draw_from_deck():
    drawn_card = draw_card()
    low_card = get_lowest_card(PLAYERS[CURRENT_PLAYER_INDEX].hand, drawn_card)
    if low_card == drawn_card:
        DISCARD_PILE.append(drawn_card)
        print(f"{PLAYERS[CURRENT_PLAYER_INDEX].player_name} has drawn and discarded {low_card}")
        print("---------------------------------------")

    else:
        PLAYERS[CURRENT_PLAYER_INDEX].hand.append(drawn_card)
        PLAYERS[CURRENT_PLAYER_INDEX].hand.remove(low_card)
        DISCARD_PILE.append(low_card)
        print(f"{PLAYERS[CURRENT_PLAYER_INDEX].player_name} has discarded {low_card} and drawn from the deck")
        print("---------------------------------------")


def opponent_pickup_discard(low_card):
    new_card = DISCARD_PILE.pop()
    PLAYERS[CURRENT_PLAYER_INDEX].hand.append(new_card)
    PLAYERS[CURRENT_PLAYER_INDEX].hand.remove(low_card)
    DISCARD_PILE.append(low_card)
    print(f"{PLAYERS[CURRENT_PLAYER_INDEX].player_name} has discarded {low_card} and picked up {new_card}")
    print("---------------------------------------")


def user_turn():
    print("---------------------------------------")
    print("Your hand:")
    print(*PLAYERS[CURRENT_PLAYER_INDEX].hand, sep="\n")
    print(f"It's your turn what would you like to do?\n1.Pickup {top_discard()}\n2.Draw a card\n3.Knock")
    while True:
        action_choice = input("Please use number index: ")
        if action_choice == "1":
            pickup_card = DISCARD_PILE.pop()
            PLAYERS[CURRENT_PLAYER_INDEX].hand.append(pickup_card)
            break
        elif action_choice == "2":
            PLAYERS[CURRENT_PLAYER_INDEX].hand.append(draw_card())
            break
        elif action_choice == "3":
            if not any_player_knocked():
                knock()
                break
            else:
                print("A player has already knocked, please select another option")

    while len(PLAYERS[CURRENT_PLAYER_INDEX].hand) > HAND_SIZE:
        print("---------------------------------------")
        for x in PLAYERS[CURRENT_PLAYER_INDEX].hand:
            print(f"{PLAYERS[CURRENT_PLAYER_INDEX].hand.index(x)}. {x}")
        card_choice = input("Which card would you like to discard, use number index: ")
        try:
            discard_card = PLAYERS[CURRENT_PLAYER_INDEX].hand[int(card_choice)]
        except TypeError:
            print("Wrong type, please enter a number within range")
        except IndexError:
            print("Out of index, please enter a number within range")
        except ValueError:
            print("Wrong value, please enter a number within range")
        else:
            PLAYERS[CURRENT_PLAYER_INDEX].hand.remove(discard_card)
            DISCARD_PILE.append(discard_card)
            break
    print("---------------------------------------")


def draw_card():
    global PLAY_DECK
    global DISCARD_PILE
    try:
        return PLAY_DECK.pop()
    except IndexError:
        top_card = top_discard()
        PLAY_DECK = DISCARD_PILE.copy()
        PLAY_DECK.remove(top_card)
        random.shuffle(PLAY_DECK)
        DISCARD_PILE = [top_card]
        return PLAY_DECK.pop()


def top_discard():
    return DISCARD_PILE[-1]


def knock():
    PLAYERS[CURRENT_PLAYER_INDEX].has_knocked = True
    print(f"{PLAYERS[CURRENT_PLAYER_INDEX]} has knocked!")


def any_player_knocked():
    return any(player.has_knocked for player in PLAYERS)


def game_over():
    print("Game has ended!")
    current_high_score = 0
    winners = []
    for player in PLAYERS:
        score = determine_score(player.hand)
        if score > current_high_score:
            current_high_score = score
            winners = [player]
        elif score == current_high_score:
            winners.append(player)
    print(*winners, sep=", ", end=" ")
    print(f"has won the game with a score of {current_high_score}!")
    for x in PLAYERS:
        print(f"{x} had a score of {determine_score(x.hand)}")
        print("Their hand contained: ", end="")
        print(*x.hand, sep=", ")
    print("---------------------------------------")
    print("Do you wish to play again?")
    play_again = input("Yes/No: ")
    if play_again.lower() == "yes":
        game_restart()
    else:
        print("Thanks for playing!")


def game_restart():
    global PLAY_DECK
    PLAY_DECK = cards.get_deck_copy()
    DISCARD_PILE.clear()
    PLAYERS.clear()
    main()


def determine_score(hand):
    total_values = [0, 0, 0, 0, 0]
    for x in hand:
        if x.card_type == "hearts":
            total_values[0] += x.card_value
        if x.card_type == "diamonds":
            total_values[1] += x.card_value
        if x.card_type == "spades":
            total_values[2] += x.card_value
        if x.card_type == "clubs":
            total_values[3] += x.card_value

    if all(card.card_name == hand[0].card_name for card in hand):
        total_values[4] = 30

    return max(total_values)


def get_lowest_card(hand, new_card):
    temp_hand = hand.copy()
    temp_hand.append(new_card)
    highest_score = 0
    lowest_card = new_card
    for x in temp_hand:
        test_hand = [y for y in temp_hand if y != x]
        score = determine_score(test_hand)
        if score > highest_score:
            highest_score = score
            lowest_card = x
        elif score == highest_score and lowest_card.card_value > x.card_value:
            lowest_card = x

    return lowest_card


main()
