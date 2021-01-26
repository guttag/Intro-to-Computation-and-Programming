# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

#set line width
plt.rcParams['lines.linewidth'] = 4
#set font size for titles 
plt.rcParams['axes.titlesize'] = 18
#set font size for labels on axes
plt.rcParams['axes.labelsize'] = 18
#set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
plt.rcParams['lines.markersize'] = 10
#set number of times marker is shown when displaying legend
plt.rcParams['legend.numpoints'] = 1
#Set size of type in legend
plt.rcParams['legend.fontsize'] = 14

# # Figure 17-1 from page 344
def roll_die():
    """Returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def roll_n(n):
    result = ''
    for i in range(n):
        result = result + str(roll_die())
    print(result)

# roll_n(10)

# # Figure 17-2 from page 347
def flip(num_flips):
    """Assumes num_flips a positive int"""
    heads = 0
    for i in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads/num_flips

def flip_sim(num_flips_per_trial, num_trials):
    """Assumes num_flips_per_trial and num_trials positive ints"""
    frac_heads = []
    for i in range(num_trials):
        frac_heads.append(flip(num_flips_per_trial))
    mean = sum(frac_heads)/len(frac_heads)
    return mean

# # Cdoe from page 347
# random.seed(0)
# print('Mean =', flip_sim(10, 1))
# print('Mean =', flip_sim(10, 1))
# print('Mean =', flip_sim(10, 100))
# print('Mean =', flip_sim(10, 100))

# # Figure 17-3 from page 350
def regress_to_mean(num_flips, num_trials):
    #Get fraction of heads for each trial of num_flips
    frac_heads = []
    for t in range(num_trials):
        frac_heads.append(flip(num_flips))
    #Find trials with extreme results and for each the next trial
    extremes, next_trials = [], []
    for i in range(len(frac_heads) - 1):
        if frac_heads[i] < 0.33 or frac_heads[i] > 0.66:
            extremes.append(frac_heads[i])
            next_trials.append(frac_heads[i+1])
    #Plot results
    plt.plot(range(len(extremes)), extremes, 'ko',
               label = 'Extreme')
    plt.plot(range(len(next_trials)), next_trials, 'k^',
               label = 'Next Trial')
    plt.axhline(0.5)
    plt.ylim(0, 1)
    plt.xlim(-1, len(extremes) + 1)
    plt.xlabel('Extreme Example and Next Trial')
    plt.ylabel('Fraction Heads')
    plt.title('Regression to the Mean')
    plt.legend(loc = 'best')

# random.seed(0)
# regress_to_mean(15, 50)

# # Figure 17-5 from page 352
def flip_plot(min_exp, max_exp):
    """Assumes min_exp and max_exp positive ints; min_exp < max_exp
       Plots results of 2**min_exp to 2**max_exp coin flips"""
    ratios, diffs, x_axis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2**exp)
    for num_flips in x_axis:
        num_heads = 0
        for n in range(num_flips):
            if random.choice(('H', 'T')) == 'H':
                num_heads += 1
        num_tails = num_flips - num_heads
        try:
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads - num_tails))
        except ZeroDivisionError:
            continue
    plt.title('Difference Between Heads and Tails')
    plt.xlabel('Number of Flips')
    plt.ylabel('Abs(#Heads - #Tails)')
    plt.xticks(rotation = 'vertical')
    plt.plot(x_axis, diffs, 'k')
    plt.figure()
    plt.title('Heads/Tails Ratios')
    plt.xlabel('Number of Flips')
    plt.ylabel('#Heads/#Tails')
    plt.xticks(rotation = 'vertical')
    plt.plot(x_axis, ratios, 'k')

# random.seed(0)
# flip_plot(4, 20)

# # Figure 17-8 from page 356
def variance(X):
    """Assumes that X is a list of numbers.
       Returns the variance of X"""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)
    
def std_dev(X):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    return variance(X)**0.5

# # Figure 17-6 from page 357
def make_plot(x_vals, y_vals, title, x_label, y_label, style,
             log_x = False, log_y = False):
    plt.figure()
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x_vals, y_vals, style)
    if log_x:
        plt.semilogx()
    if log_y:
        plt.semilogy()

# # Figure 17-10 from page 358
def run_trial(num_flips):
    num_heads = 0
    for n in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            num_heads += 1
    num_tails = num_flips - num_heads
    return (num_heads, num_tails)

def flip_plot1(min_exp, max_exp, num_trials):
    """Assumes min_exp, max_exp, num_trials ints >0; min_exp < max_exp
       Plots summaries of results of num_trials trials of
       2**min_exp to 2**max_exp coin flips"""
    ratios_means, diffs_means, ratios_SDs, diffs_SDs = [], [], [], []
    x_axis = []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2**exp)
    for num_flips in x_axis:
        ratios, diffs = [], []
        for t in range(num_trials):
            num_heads, num_tails = run_trial(num_flips)
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads - num_tails))
        ratios_means.append(sum(ratios)/num_trials)
        diffs_means.append(sum(diffs)/num_trials)
        ratios_SDs.append(std_dev(ratios))
        diffs_SDs.append(std_dev(diffs))
    title = f'Mean Heads/Tails Ratios ({num_trials} Trials)'
    make_plot(x_axis, ratios_means, title, 'Number of Flips',
             'Mean Heads/Tails', 'ko', log_x = True)
    title = f'SD Heads/Tails Ratios ({num_trials} Trials)'
    make_plot(x_axis, ratios_SDs, title, 'Number of Flips',
            'Standard Deviation', 'ko', log_x = True, log_y = True)

# random.seed(0)
# flip_plot1(4, 20, 20)

# # flip_plot1 with addtion of code from Figure 17-12 on page 360
def flip_plot1(min_exp, max_exp, num_trials):
    """Assumes min_exp, max_exp, num_trials ints >0; min_exp < max_exp
       Plots summaries of results of num_trials trials of
       2**min_exp to 2**max_exp coin flips"""
    ratios_means, diffs_means, ratios_SDs, diffs_SDs = [], [], [], []
    x_axis = []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2**exp)
    for num_flips in x_axis:
        ratios, diffs = [], []
        for t in range(num_trials):
            num_heads, num_tails = run_trial(num_flips)
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads - num_tails))
        ratios_means.append(sum(ratios)/num_trials)
        diffs_means.append(sum(diffs)/num_trials)
        ratios_SDs.append(std_dev(ratios))
        diffs_SDs.append(std_dev(diffs))
    title = f'Mean Heads/Tails Ratios ({num_trials} Trials)'
    make_plot(x_axis, ratios_means, title, 'Number of Flips',
             'Mean Heads/Tails', 'ko', log_x = True)
    title = f'SD Heads/Tails Ratios ({num_trials} Trials)'
    make_plot(x_axis, ratios_SDs, title, 'Number of Flips',
            'Standard Deviation', 'ko', log_x = True, log_y = True)
    ###Added later in chapter
    title = f'Mean abs(#Heads - #Tails) ({num_trials} Trials)'
    make_plot(x_axis, diffs_means, title,
          'Number of Flips', 'Mean abs(#Heads - #Tails)', 'ko',
          log_x = True, log_y = True)
    title = f'SD abs(#Heads - #Tails) ({num_trials} Trials)'
    make_plot(x_axis, diffs_SDs, title,
          'Number of Flips', 'Standard Deviation', 'ko',
          log_x = True, log_y = True)

# # Figure 17-14 from page 361
def CV(X):
    mean = sum(X)/len(X)
    try:
        return std_dev(X)/mean
    except ZeroDivisionError:
        return float('nan')

# # Figure 17-15 from page 362
def flip_plot2(min_exp, max_exp, num_trials):
    """Assumes min_exp and max_exp positive ints; min_exp < max_exp
         num_trials a positive integer
       Plots summaries of results of num_trials trials of
         2**min_exp to 2**max_exp coin flips"""
    ratios_means, diffs_means, ratios_SDs, diffs_SDs = [], [], [], []
    ratios_CVs, diffs_CVs, x_axis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2**exp)
    for num_flips in x_axis:
        ratios, diffs = [], []
        for t in range(num_trials):
            num_heads, num_tails = run_trial(num_flips)
            ratios.append(num_heads/float(num_tails))
            diffs.append(abs(num_heads - num_tails))
        ratios_means.append(sum(ratios)/num_trials)
        diffs_means.append(sum(diffs)/num_trials)
        ratios_SDs.append(std_dev(ratios))
        diffs_SDs.append(std_dev(diffs))
        ratios_CVs.append(CV(ratios))
        diffs_CVs.append(CV(diffs))
    num_trials_str = ' (' + str(num_trials) + ' Trials)'
    title = 'Mean Heads/Tails Ratios' + num_trials_str
    make_plot(x_axis, ratios_means, title, 'Number of flips',
             'Mean Heads/Tails', 'ko', log_x = True)
    title = 'SD Heads/Tails Ratios' + num_trials_str
    make_plot(x_axis, ratios_SDs, title, 'Number of flips',
             'Standard Deviation', 'ko', log_x = True, log_y = True)
    title = 'Mean abs(#Heads - #Tails)' + num_trials_str
    make_plot(x_axis, diffs_means, title,'Number of Flips',
             'Mean abs(#Heads - #Tails)', 'ko',
             log_x = True, log_y = True)
    title = 'SD abs(#Heads - #Tails)' + num_trials_str
    make_plot(x_axis, diffs_SDs, title, 'Number of Flips',
             'Standard Deviation', 'ko', log_x = True, log_y = True)
    title = 'Coeff. of Var. abs(#Heads - #Tails)' + num_trials_str
    make_plot(x_axis, diffs_CVs, title, 'Number of Flips',
             'Coeff. of Var.', 'ko', log_x = True)
    title = 'Coeff. of Var. Heads/Tails Ratio' + num_trials_str
    make_plot(x_axis, ratios_CVs, title, 'Number of Flips',
             'Coeff. of Var.', 'ko', log_x = True, log_y = True)

# flip_plot2(4, 20, 20)

# # Code from Figure 17-19 on page 366
# random.seed(0)
# vals = []
# for i in range(1000):
#     num1 = random.choice(range(0, 101))
#     num2 = random.choice(range(0, 101))
#     vals.append(num1 + num2)
# plt.hist(vals, bins = 10, ec = 'k')
# plt.xlabel('Sum')
# plt.ylabel('Number of Occurrences')

# # Code from Figure 17-20 on page 368
def flip(num_flips):
    """Assumes num_flips a positive int"""
    heads = 0
    for i in range(num_flips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads/float(num_flips)

def flip_sim(num_flips_per_trial, num_trials):
    frac_heads = []
    for i in range(num_trials):
        frac_heads.append(flip(num_flips_per_trial))
    mean = sum(frac_heads)/len(frac_heads)
    sd = std_dev(frac_heads)
    return (frac_heads, mean, sd)

def label_plot(num_flips, num_trials, mean, sd):
    plt.title(str(num_trials) + ' trials of '
                + str(num_flips) + ' flips each')
    plt.xlabel('Fraction of Heads')
    plt.ylabel('Number of Trials')
    plt.annotate('Mean = ' + str(round(mean, 4))
                   + '\nSD = ' + str(round(sd, 4)), size='x-large',
                   xycoords = 'axes fraction', xy = (0.67, 0.5))

def make_plots(num_flips1, num_flips2, num_trials):
    val1, mean1, sd1 = flip_sim(num_flips1, num_trials)
    plt.hist(val1, bins = 20)
    x_min,x_max = plt.xlim()
    label_plot(num_flips1, num_trials, mean1, sd1)
    plt.figure()
    val2, mean2, sd2 = flip_sim(num_flips2, num_trials)
    plt.hist(val2, bins = 20, ec = 'k')
    plt.xlim(x_min, x_max)
    label_plot(num_flips2, num_trials, mean2, sd2)

# random.seed(0)
# make_plots(100, 1000, 100000)

# # Code to produce plot in Figure 17-25 on page 374
# plt.plot([0,5], [0,5])
# plt.xlim(0,5)
# plt.ylim(0,5)
# plt.title('abs(x)')

#Figure 15.23
# print(scipy.integrate.quad(abs, 0, 5)[0])
# print(scipy.integrate.quad(abs, 0, 5)[1])

# # Figure 17-26 on page 375
def gaussian(x, mu, sigma):
    """assumes x, mu, sigma numbers
       returns the value of P(x) for a Gaussian
          with mean mu and sd sigma"""
    factor1 = (1.0/(sigma*((2*np.pi)**0.5)))
    factor2 = np.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2
   
def check_empirical(mu_max, sigma_max, num_trials):
    """assumes mu_max, sigma_max, num_trials positive ints
       prints fraction of values of a Gaussians (with randomly
       chosen mu and sigman) falling within 1, 2, 3 standard
       deviations"""
    for t in range(num_trials):
        mu = random.randint(-mu_max, mu_max + 1)
        sigma = random.randint(1, sigma_max)
        print('For mu =', mu, 'and sigma =', sigma)
        for num_std in (1, 2, 3):
            area = scipy.integrate.quad(gaussian, mu-num_std*sigma,
                                        mu+num_std*sigma,
                                        (mu, sigma))[0]
            print('  Fraction within', num_std, 'std =',
                  round(area, 4))

# random.seed(0)
# check_empirical(10, 10, 3)

# # Code on bottom of p[age 374]
# for x in range(-2, 3):
#     print(gaussian(x, 0, 1))

# # Code on top of page 375
# print(scipy.integrate.quad(gaussian, -1, 1, (0, 1))[0])

# # Figure 17-27 on page 377
def show_error_bars(min_exp, max_exp, num_trials):
    """Assumes min_exp and max_exp positive ints; min_exp < max_exp
         num_trials a positive integer
       Plots mean fraction of heads with error bars"""
    means, sds, x_vals = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_vals.append(2**exp)
        frac_heads, mean, sd = flip_sim(2**exp, num_trials)
        means.append(mean)
        sds.append(sd)
    plt.errorbar(x_vals, means, yerr=1.96*np.array(sds))
    plt.semilogx()
    plt.title('Mean Fraction of Heads ('
                + str(num_trials) + ' trials)')
    plt.xlabel('Number of flips per trial')
    plt.ylabel('Fraction of heads & 95% confidence')

# show_error_bars(3, 10, 100)

# # Figure 17-29 on page 382
def clear(n, p, steps):
    """Assumes n & steps positive ints, p a float
         n: the initial number of molecules
         p: the probability of a molecule being cleared
         steps: the length of the simulation"""
    num_remaining = [n]
    for t in range(steps):
        num_remaining.append(n*((1-p)**t))
    plt.plot(num_remaining)
    plt.xlabel('Time')
    plt.ylabel('Molecules Remaining')
    plt.title('Clearance of Drug')

# clear(1000, 0.01, 1000)

# # Code suggested at top of page 383
# plt.semilogy()

# # Figure 17-32 on page 384
def successful_starts(success_prob, num_trials):
    """Assumes success_prob is a float representing probability of a
         single attempt being successful. num_trials a positive int
       Returns a list of the number of attempts needed before a
         success for each trial."""
    tries_before_success = []
    for t in range(num_trials):
        consec_failures = 0
        while random.random() > success_prob:
            consec_failures += 1
        tries_before_success.append(consec_failures)
    return tries_before_success

# prob_of_success = 0.5
# num_trials = 5000
# distribution = successful_starts(prob_of_success, num_trials)
# plt.hist(distribution, bins = 14)
# plt.xlabel('Tries Before Success')
# plt.ylabel('Number of Occurrences Out of ' + str(num_trials))
# plt.title('Probability of Starting Each Try = '
#             + str(prob_of_success))

# # Code on page 387
def collision_prob(n, k):
    prob = 1.0
    for i in range(1, k):
        prob = prob * ((n - i)/n)
    return 1 - prob

# print(collision_prob(1000, 50))
# print(collision_prob(1000, 200))

# # Figure 17-34 on page 388
def sim_insertions(num_indices, num_insertions):
    """Assumes num_indices and num_insertions are positive ints.
       Returns 1 if there is a collision; 0 otherwise"""
    choices = range(num_indices) #list of possible indices
    used = []
    for i in range(num_insertions):
        hash_val = random.choice(choices)
        if hash_val in used: #there is a collision
            return 1
        else:
            used.append(hash_val)
    return 0

def find_prob(num_indices, num_insertions, num_trials):
    collisions = 0
    for t in range(num_trials):
        collisions += sim_insertions(num_indices, num_insertions)
    return collisions/num_trials

# # Code on page 388
# print('Actual probability of a collision =', collision_prob(1000, 50))
# print('Est. probability of a collision =', find_prob(1000, 50, 10000))
# print('Actual probability of a collision =', collision_prob(1000, 200))
# print('Est. probability of a collision =', find_prob(1000, 200, 10000))

# # Figure 17-35 on page 390
def play_series(num_games, team_prob):
    numWon = 0
    for game in range(num_games):
        if random.random() <= team_prob:
            numWon += 1
    return (numWon > num_games//2)
    
def fraction_won(team_prob, num_series, series_len):
    won = 0
    for series in range(num_series):
        if play_series(series_len, team_prob):
            won += 1
    return won/float(num_series)

def sim_series(num_series):
    prob = 0.5
    fracsWon, probs = [], []
    while prob <= 1.0:
        fracsWon.append(fraction_won(prob, num_series, 7))
        probs.append(prob)
        prob += 0.01
    plt.axhline(0.95) #Draw line at 95%
    plt.plot(probs, fracsWon, 'k', linewidth = 5)
    plt.xlabel('Probability of Winning a Game')
    plt.ylabel('Probability of Winning a Series') 
    plt.title(str(num_series) + ' Seven-Game Series')

# sim_series(400)
