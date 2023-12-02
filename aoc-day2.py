import sys
import re


# each line is a list of semicolon delimited game trails with format:
#   Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# return a list of dicts with format:
#   [
#    {
#      game: 1,
#      trials: [
#         {'red': 4, 'green': 0, 'blue': 3 },
#         {'red': 1, 'green': 2, 'blue': 0 },
#         {'red': 0, 'green': 2, 'blue': 0 },
#      ]
#   },
#   ...
#   ]
def parse_inputs(file):
    print(f'loading {file}')
    res = []
    with open(file, 'r') as f:
        lines = f.readlines()
        print(f'loaded {len(lines)} lines')
        for line in lines:
            trimmed = line.strip()
            if trimmed:
                parts = trimmed.split(':')
                game = re.search(r'Game\s(\d+)', parts[0].strip()).group(1)
                trials_str = parts[1].split(';')
                trials = []
                for trial_str in trials_str:
                    trial = {
                        'red': 0,
                        'green': 0,
                        'blue': 0
                    }
                    for number, color in re.findall(r'(\d+)\s(\w+)', trial_str.strip()):
                        trial[color] = int(number)
                    trials.append(trial)
                res.append({
                    'game': int(game),
                    'trials': trials
                })
    return res


def is_possible_game(game, limits):
    for trial in game['trials']:
        for color, number in trial.items():
            if number > limits[color]:
                return False
    return True


def power(game):
    from functools import reduce
    maxs = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for trial in game['trials']:
        for color, number in trial.items():
            if number > maxs[color]:
                maxs[color] = number
    min_ball_counts = [x[1] for x in maxs.items()]
    return reduce(lambda x, y: x * y, min_ball_counts)


def main():
    limits = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    # load file and parse lines
    games = parse_inputs(sys.argv[1])
    # part 1
    possible_games = filter(lambda game: is_possible_game(game, limits), games)
    game_nums = [game['game'] for game in possible_games]
    print('possible games, game # sum', sum(game_nums))
    # part 2
    game_powers = [power(game) for game in games]
    print('powers, sum', sum(game_powers))


if __name__ == '__main__':
    main()
