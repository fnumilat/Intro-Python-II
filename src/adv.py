from room import Room
from player import Player
from os import system

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player_one = Player("Fnu", room["outside"])

def print_instructions():
    print("|Enter 'n' to move North  |")
    print("|Enter 's' to move South  |")
    print("|Enter 'e' to move East   |")
    print("|Enter 'w' to move West   |")
    print("|Enter 'q' to quit        |")


while True: 
    print(f'Player: {player_one.name}')
    print(f'Location: {player_one.current_room.name}')
    print(f'Location Description: {player_one.current_room.description}')
    print_instructions()

    next_move = input("What is your next move?")
    if next_move == "n":
        if player_one.current_room.n_to == None:
            print("Not a valid direction. Try a valid direction!")
        else:
            player_one.current_room = player_one.current_room.n_to
            print("You moved to North!")
    elif next_move == "s":
        if player_one.current_room.s_to == None:
            print("Not a valid direction. Try a valid direction!")
        else:
            player_one.current_room = player_one.current_room.s_to
            print("You moved to South!")
    elif next_move == "e":
        if player_one.current_room.e_to == None:
            print("Not a valid direction. Try a valid direction!")
        else:
            player_one.current_room = player_one.current_room.e_to
            print("You moved to East!")
    elif next_move == "w":
        if player_one.current_room.w_to == None:
            print("Not a valid direction. Try a valid direction!")
        else:
            player_one.current_room = player_one.current_room.w_to
            print("You moved to West!")
    elif next_move == "q":
        print("Exited the Game!!")
        system("clear")

        break
    else:
        print("Not a valid direction. Try a valid direction!")
