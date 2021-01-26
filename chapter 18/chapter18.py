# -*- coding: utf-8 -*-

import random
import numpy as np

# # Figure 18-1 on page 396
def roll_die():
    return random.choice([1,2,3,4,5,6])

# #Used later in chapter
# def roll_die():
#     return random.choice([1,1,2,3,3,4,4,5,5,5,6,6])

def check_pascal(num_trials):
    """Assumes num_trials is an int > 0
       Prints an estimate of the probability of winning"""
    num_wins = 0
    for i in range(num_trials):
        for j in range(24):
            d1 = roll_die()
            d2 = roll_die()
            if d1 == 6 and d2 == 6:
                num_wins += 1
                break
    print('Probability of winning =', num_wins/num_trials)
    
# check_pascal(1000000)

# # Figure 18-2 on page 397
class Craps_game(object):
    def __init__(self):
        self.pass_wins, self.pass_losses = 0, 0
        self.dp_wins, self.dp_losses, self.dp_pushes = 0, 0, 0

    def play_hand(self):
        throw = roll_die() + roll_die()
        if throw == 7 or throw == 11:
            self.pass_wins += 1
            self.dp_losses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.pass_losses += 1
            if throw == 12:
                self.dp_pushes += 1
            else:
                self.dp_wins += 1
        else:
            point = throw
            while True:
                throw = roll_die() + roll_die()
                if throw == point:
                    self.pass_wins += 1
                    self.dp_losses += 1
                    break
                elif throw == 7:
                    self.pass_losses += 1
                    self.dp_wins += 1
                    break

    def pass_results(self):
        return (self.pass_wins, self.pass_losses)

    def dp_results(self):
        return (self.dp_wins, self.dp_losses, self.dp_pushes)
  
def craps_sim(hands_per_game, num_games):
    """Assumes hands_per_game and num_games are ints > 0
       Play num_games games of hands_per_game hands; print results"""
    games = []

    #Play num_games games
    for t in range(num_games):
        c = Craps_game()
        for i in range(hands_per_game):
            c.play_hand()
        games.append(c)
        
    #Produce statistics for each game
    p_ROI_per_game, dp_ROI_per_game = [], []
    for g in games:
        wins, losses = g.pass_results()
        p_ROI_per_game.append((wins - losses)/float(hands_per_game))
        wins, losses, pushes = g.dp_results()
        dp_ROI_per_game.append((wins - losses)/float(hands_per_game))
        
    #Produce and print summary statistics
    mean_ROI = str(round((100*sum(p_ROI_per_game)/num_games), 4)) + '%'
    sigma = str(round(100*np.std(p_ROI_per_game), 4)) + '%'
    print('Pass:', 'Mean ROI =', mean_ROI, 'Std. Dev. =', sigma)
    mean_ROI = str(round((100*sum(dp_ROI_per_game)/num_games), 4)) +'%'
    sigma = str(round(100*np.std(dp_ROI_per_game), 4)) + '%'
    print('Don\'t pass:','Mean ROI =', mean_ROI, 'Std Dev =', sigma)

# # Code from page 400
# craps_sim(20, 10)
        
# craps_sim(1000000, 10)

# # Code from page 401
# craps_sim(20, 1000000)

# # Class with version of play_hand from Figure 18-4 on page 403
class Craps_game(object):
    def __init__(self):
        self.pass_wins, self.pass_losses = 0, 0
        self.dp_wins, self.dp_losses, self.dp_pushes = 0, 0, 0
    def play_hand(self):
        #An alternative, faster, implementation of play_hand
        points_dict = {4:1/3, 5:2/5, 6:5/11, 8:5/11, 9:2/5, 10:1/3}
        throw = roll_die() + roll_die()
        if throw == 7 or throw == 11:
            self.pass_wins += 1
            self.dp_losses += 1
        elif throw == 2 or throw == 3 or throw == 12:
            self.pass_losses += 1
            if throw == 12:
                self.dp_pushes += 1
            else:
                self.dp_wins += 1
        else:
            if random.random() <= points_dict[throw]: # point before 7
                self.pass_wins += 1
                self.dp_losses += 1
            else:                                    # 7 before point
                self.pass_losses += 1
                self.dp_wins += 1

    def pass_results(self):
        return (self.pass_wins, self.pass_losses)

    def dp_results(self):
        return (self.dp_wins, self.dp_losses, self.dp_pushes)

# # Figure 18-6 from page 407
def throw_needles(num_needles):
    in_circle = 0
    for Needles in range(1, num_needles + 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1:
            in_circle += 1
    #Counting needles in one quadrant only, so multiply by 4
    return 4*(in_circle/num_needles)

def get_est(num_needles, num_trials):
    estimates = []
    for t in range(num_trials):
        pi_guess = throw_needles(num_needles)
        estimates.append(pi_guess)
    std_dev = np.std(estimates)
    cur_est = sum(estimates)/len(estimates)
    print('Est. =', str(round(cur_est, 5)) + ',',
          'Std. dev. =', str(round(std_dev, 5)) + ',',
          'Needles =', num_needles)
    return (cur_est, std_dev)

def est_pi(precision, num_trials):
    num_needles = 1000
    std_dev = precision
    while std_dev > precision/1.96:
        cur_est, std_dev = get_est(num_needles, num_trials)
        num_needles *= 2
    return cur_est

# # Code from page 407
random.seed(0)
est_pi(0.01, 100)