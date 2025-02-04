import scipy.stats as stats


def calculate_probability_within_range(mean, variance, lower_bound, upper_bound):
    # Calculate the standard deviation
    std_dev = variance ** 0.5
    
    # Calculate z-scores for the bounds
    z_lower = (lower_bound - mean) / std_dev
    z_upper = (upper_bound - mean) / std_dev
    
    # Calculate the probabilities using the CDF of the standard normal distribution
    probability = stats.norm.cdf(z_upper) - stats.norm.cdf(z_lower)
    return probability

if __name__ == '__main__':
    mean = float(input('Enter the mean: '))
    variance = float(input('Enter the variance: '))
    lower_bound = float(input('Enter the lower bound: '))
    upper_bound = float(input('Enter the upper bound: '))
    
    probability = calculate_probability_within_range(mean, variance, lower_bound, upper_bound)
    print(f'The probability that x is within the range [{lower_bound}, {upper_bound}] is: {probability}')