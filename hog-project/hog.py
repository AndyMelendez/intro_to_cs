# Project: The Game of Hog
# Authors: Jordan Shefrin & Krishna Parashar
# Class: CS61A
# Date: 09-12-12

# Preprogram Functions

from dice import four_sided_dice, six_sided_dice, make_test_dice
from ucb import main, trace, log_current_line, interact

goal = 100                 # The goal of Hog is to score 100 points.
commentary = False  # Whether to display commentary for every roll.

# Turn Taking Functions

def roll_dice(num_rolls, dice = six_sided_dice, who = 'Boss Hogg'):
    """Calculate WHO's turn score after rolling DICE for NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A function of no args and returns an integer outcome.
    who:        Name of the current player, for commentary.
    """

    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    k, score_total = 1, 0
    rolled_a_one = False
    while k <= num_rolls:
        outcome = dice()
        if commentary:
            announce(outcome, who)
        if outcome == 1:
            rolled_a_one = True
        else:
            score_total, k = score_total + outcome, k + 1
    if rolled_a_one == True:
        return 1 
    return score_total

def take_turn(num_rolls, opponent_score, dice=six_sided_dice, who='Boss Hogg'):
    """Simulate a turn in which WHO chooses to roll NUM_ROLLS, perhaps 0.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args and returns an integer outcome.
    who:             Name of the current player, for commentary.
    """

    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    
    if commentary:
        print(who, 'is going to roll', num_rolls, 'dice')
    if num_rolls == 0:
        return opponent_score//10 + 1    
    else:
        return roll_dice(num_rolls, dice, who)

def take_turn_test():
    # Test the roll_dice and take_turn functions using test dice.
    
    print('Testing roll_dice function with deterministic test dice...')
    
    dice = make_test_dice(4, 6, 1)
    assert roll_dice(2, dice) == 10, 'First two rolls total 10'
    dice = make_test_dice(4, 6, 1)
    assert roll_dice(3, dice) == 1, 'Third roll is a 1'
    dice = make_test_dice(1, 2, 3)
    assert roll_dice(3, dice) == 1, 'First roll is a 1'
    print('Testing Turn Taking Functions..')
    dice = make_test_dice(4, 6, 1)
    assert take_turn(2, 0, dice) == 10, 'First two rolls total 10'
    dice = make_test_dice(4, 6, 1)
    assert take_turn(3, 20, dice) == 1, 'Third roll is a 1'
    assert take_turn(0, 34) == 4, 'Opponent score 10s digit is 3'
    assert take_turn(0, 71) == 8, 'Opponent score 10s digit is 7'
    assert take_turn(0,  7) == 1, 'Opponont score 10s digit is 0'
    print('Tests for roll_dice and take_turn passed.')


# Commentator Functions

def announce(outcome, who):
    # Print a description of WHO rolling OUTCOME.
    
    print(who, 'rolled a', outcome)
    print(draw_number(outcome))

def draw_number(n, dot='*'):
    """Return a text representation of rolling the number N.
    If a number has multiple possible representations (such as 2 and 3), any
    valid representation is acceptable.
    """
    
    if n == 1:
        return draw_dice(True, False, False, False,dot)
    elif n == 2:
        return draw_dice(False, False, True, False,dot)
    elif n == 3:
        return draw_dice(True, True, False, False,dot)
    elif n == 4:
        return draw_dice(False, True, True, False,dot)
    elif n == 5:
        return draw_dice(True, True, True, False, dot)
    elif n == 6:
        return draw_dice( False, True, True, True, dot)
    else:
       return draw_dice(False, False, False, False, dot) #For case in which invalid dice is passed

def draw_dice(c, f, b, s, dot):
    """Return an ASCII art representation of a die roll\

    c, f, b, s -- booleans; whether to place dots in corresponding positions.
    dot        -- A length-one string to use for a dot.
    """
    assert len(dot) == 1, 'Dot must be a single symbol'
    border = ' -------'
    def draw(b):
        return dot if b else ' '
    c, f, b, s = map(draw, [c, f, b, s])
    top = ' '.join(['|', b, ' ', f, '|'])
    middle = ' '.join(['|', s, c, s, '|'])
    bottom = ' '.join(['|', f, ' ', b, '|'])
    return '\n'.join([border, top, middle, bottom, border])


# Game Simulator Functions

def num_allowed_dice(score, opponent_score):
    #Return the maximum number of dice allowed this turn.
    # The maximum number of dice allowed is 10 unless the sum of SCORE and OPPONENT_SCORE has a 7 as its ones digit.

    if (score + opponent_score) % 10 == 7:
        return 1
    else:
        return 10

def select_dice(score, opponent_score):
    # Select 6-sided dice unless the sum of scores is a multiple of 7.

    if (score + opponent_score) % 7 == 0:
        return four_sided_dice
    else:
        return six_sided_dice

def other(who):
    # Return the other player, for players numbered 0 or 1.
    return (who + 1) % 2

def name(who):
    # Return the name of player WHO, for player numbered 0 or 1.
    
    if who == 0:
        return 'Player 0'
    elif who == 1:
        return 'Player 1'
    else:
        return 'An Unknown Player'

def play(strategy0, strategy1):
    """Simulate a game and return 0 if the first player wins and 1 otherwise.

    A strategy function takes two scores for the current and opposing players.
    It returns the number of dice that the current player will roll this turn.

    If a strategy returns more than the maximum allowed dice for a turn, then
    the maximum allowed is rolled instead.

    strategy0:  The strategy function for player 0, who plays first.
    strategy1:  The strategy function for player 1, who plays second.
    """
    
    score, opp_score = 0, 0
    strategy, opp_strategy = strategy0, strategy1

    while score < goal and opp_score < goal:
        score =  score +  take_turn(min(num_allowed_dice(score, opp_score), strategy(score, opp_score)), opp_score, select_dice(score, opp_score), name(who))
        score, opp_score = opp_score, score
        who = other(who)
        strategy, opp_strategy = opp_strategy, strategy

    if score >= goal:
        return 0
    else:
        return 1


# Basic Strategy Functions

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two game scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice to roll.

    If a strategy returns more than the maximum allowed dice for a turn, then
    the maximum allowed is rolled instead.
    """
    
    def strategy(score, opponent_score):
        return n
    return strategy


# Experiment Functions (Phase 2)

def make_average(fn, num_samples = 30000):
    # Return a function that returns the average_value of FN when called.
    
    def average(*args):
        counter, total = 0, 0
        while counter < num_samples:
            counter, total = counter + 1, total + fn(*args)
        return total / num_samples
    return average

def compare_strategies(strategy, baseline=always_roll(5)):
    # Return the average win rate (out of 1) of STRATEGY against BASELINE.
    
    as_first = 1 - make_average(play)(strategy, baseline)
    as_second = make_average(play)(baseline, strategy)
    return (as_first + as_second) / 2  # average the two results

def eval_strategy_range(make_strategy, lower_bound, upper_bound):
    """Return the best integer argument value for MAKE_STRATEGY to use against
    the always-roll-5 baseline, between LOWER_BOUND and UPPER_BOUND (inclusive).

    make_strategy -- A one-argument function that returns a strategy.
    lower_bound -- lower bound of the evaluation range.
    upper_bound -- upper bound of the evaluation range.
    """
    
    best_value, best_win_rate = 0, 0
    value = lower_bound
    
    while value <= upper_bound:
        strategy = make_strategy(value)
        win_rate = compare_strategies(strategy)
        print('Win rate against the baseline using', value, 'value:', win_rate)
        if win_rate > best_win_rate:
            best_win_rate, best_value = win_rate, value
        value += 1
    return best_value

def run_experiments():
    # Run a series of strategy experiments and report results.

    if True: # Change to True when ready to test make_comeback_strategy
        result = eval_strategy_range(make_comeback_strategy, 5, 6)
        print('Best comeback strategy:', result)
    if True: # Change to True when ready to test make_mean_strategy
        result = eval_strategy_range(make_mean_strategy, 1, 2)
        print('Best mean strategy:', result)



# Developed Strategy Functions

def make_comeback_strategy(margin, num_rolls = 5):
    #Return a strategy that rolls one extra time when losing by MARGIN.
    def comeback(score, opponent_score):
        if opponent_score - score >= margin:
           return num_rolls + 1
        return num_rolls
    return comeback

def make_mean_strategy(min_points, num_rolls = 5):
    # Return a strategy that attempts to give the opponent problems.
    
    def mean(score, opponent_score):
        score_temp = 0
        if (opponent_score//10 + 1) >= min_points:
            score_temp = score + opponent_score//10 + 1
            if (score_temp + opponent_score) % 10 == 7 or (score_temp + opponent_score) % 7 == 0:
                return 0
        return num_rolls
    return mean


def final_strategy(score, opponent_score, num_rolls=5):
    # Take Advantage of Free Bacon and Probability (With a mix of Trial and Error) to Win!
    # Order of "IF" statements are important.
        
    free_bacon = ((opponent_score // 10) + 1)
    if score + (free_bacon) >= goal:
        return 0 # Intial Free Bacon Strategy
    elif (free_bacon >= 5) and ((score + opponent_score) % 10 == 7): # Another Free Bacon Strategy 
        return 0
    elif score >= goal - 3:
        return 1
    elif score >= goal - 6:
        return 2
    elif score >= goal - 9:
        return 3
    elif (free_bacon) + 1 >= 4 and ((free_bacon) + score + opponent_score) % 10 == 7 or (free_bacon + score + opponent_score) % 7 == 0:
        return 0 # More Free Bacon Strategy   
    elif score > opponent_score + 40:
        return 4 
    elif score < opponent_score - 20:
        return 6
    else:
        return 5 # Default Number of Rolls


def final_strategy_test():
    # Compares final strategy to the baseline strategy.

    print('Testing Final Strategy...')
    win_rate = compare_strategies(final_strategy)
    print('Win Rate:', win_rate, '\n')
    if win_rate >= 0.6:
        print('Congrats! You won', win_rate*100, '% of the time!' )



# Interaction Functions (You don't need to read this section of the program)

def interactive_strategy(score, opponent_score):
    """Prints total game scores and returns an interactive tactic.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    print('Current score:', score, 'to', opponent_score)
    while True:
        response = input('How many dice will you roll? ')
        try:
            result = int(response)
        except ValueError:
            print('Please enter a positive number')
            continue
        if result < 0:
            print('Please enter a non-negative number')
        else:
            return result

def play_interactively():
    # Play one interactive game.
    
    global commentary
    commentary = True
    print("Shall we play a game?")
    winner = play(interactive_strategy, always_roll(5))
    if winner == 0:
        print("You win!")
    else:
        print("The computer won.")

def play_basic():
    # Play one game in which two basic strategies compete.
    
    global commentary
    commentary = True
    winner = play(always_roll(5), always_roll(6))
    if winner == 0:
        print("Player 0, who always wants to roll 5, won.")
    else:
        print("Player 1, who always wants to roll 6, won.")

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--take_turn_test', '-t', action='store_true')
    parser.add_argument('--play_interactively', '-p', action='store_true')
    parser.add_argument('--play_basic', '-b', action='store_true')
    parser.add_argument('--run_experiments', '-r', action='store_true')
    parser.add_argument('--final_strategy_test', '-f', action='store_true')
    args = parser.parse_args()
    for name, execute in args.__dict__.items():
        if execute:
            globals()[name]()
