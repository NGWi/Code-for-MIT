import scipy
p = float(input('Enter probability: '))
n = int(input('Enter number of trials: '))
k = int(input('Enter number of occurences: '))

ways_of_choosing_k = scipy.special.comb(n, k)
prob_that_take_1 = p ** k
prob_that_others_take_0 = (1 - p) ** (n - k)
pmf = ways_of_choosing_k * prob_that_take_1 * prob_that_others_take_0
print(pmf)