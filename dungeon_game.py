import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_map(w, h):
    # CELLS  = []
    CELLS = list((x, y) for x in range(w) for y in range(h))
    return CELLS
    # for x in range(w):
    #     for y in range(h):
    #         CELLS.append((x,y))
    # return CELLS


def get_locations(CELLS):
    return random.sample(CELLS, 3)


def get_moves(player, w, h):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    x, y = player
    if y == 0:
        moves.remove('LEFT')
    if y == h-1:
        moves.remove('RIGHT')
    if x == 0:
        moves.remove('UP')
    if x == w-1:
        moves.remove('DOWN')
    return moves


def move_player(player, move):
    x, y = player
    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'DOWN':
        x += 1
    elif move == 'UP':
        x -= 1
    return x, y

def draw_map(player, CELLS, w, h):
    print(' _' * h)
    tile = '|{}'

    for cell in CELLS:
        x, y = cell
        if y < h-1:
            line_end = ''
            if cell == player:
                output = tile.format('X')
            else:
                output = tile.format('_')
        else:
            line_end = '\n'
            if cell == player:
                output = tile.format('X|')
            else:
                output = tile.format('_|')
        print(output, end=line_end)


def game_loop():
    w = random.randint(5, 10)
    h = random.randint(5, 10)
    CELLS = generate_map(w, h)
    player, monster, door = get_locations(CELLS)
    playing = True

    while playing:
        clear()
        draw_map(player, CELLS, w, h)
        valid_moves = get_moves(player, w, h)

        print(f'You are currently in room {player}')
        print(f'You can move {", ".join(valid_moves)}')
        print('Enter QUIT to quit')

        move = input('> ').upper()

        if move == 'QUIT':
            break
        elif move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print('\n** Monster got you! Better luck next time **\n')
                playing = False
            if player == door:
                print('\n** You escaped! Congratulations!**\n')
                playing = False
        else:
            input('\n**You can not go through walls! **\n')
    else:
        if input('Play again? [Y/n] ').lower() != 'n':
            game_loop()


print('Welcome to the Dungeon')
input('Press return to start')
clear()
game_loop()
