import scipy
alpha = float(input('Enter alpha: '))
lambda_ = float(input('Enter units in treatment group: '))
pi = float(input('Enter incidence rate in control group: '))

print(scipy.stats.binom.ppf(alpha, lambda_, pi))