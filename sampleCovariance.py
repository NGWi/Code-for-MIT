import numpy as np


def sample_mean(data):
    return sum(data) / len(data)


def sample_std_dev(data):
    mean = sample_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    return variance ** 0.5


def sample_covariance(data1, data2):
    mean1 = sample_mean(data1)
    mean2 = sample_mean(data2)
    covariance = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(len(data1))) / (len(data1) - 1)
    return covariance


def max_covariance(std_dev1, std_dev2):
    return std_dev1 * std_dev2


def min_covariance(std_dev1, std_dev2):
    return -std_dev1 * std_dev2


def calculate_beta_hat_1(covariance, variance_x):
    """
    Calculates the slope of a linear regression model.

    Returns:
        The slope of the linear regression model.
    """
    if variance_x == 0:
        return 0
    return covariance / variance_x


def calculate_beta_hat_0(mean_x, mean_y, beta_hat_1):
    """
    Calculates the intercept beta_hat_0.

    Args:
        mean_x: The mean of the X values.
        mean_y: The mean of the Y values.
        beta_hat_1: The slope of the linear regression model.

    Returns:
        The intercept beta_hat_0.
    """
    beta_hat_0 = mean_y - beta_hat_1 * mean_x
    return beta_hat_0


def direct_r_squared(data_x, data_y, beta_hat_1, beta_hat_0):
    """
    Tests the goodness of fit of a linear regression model.

    Returns:
        The R-squared value.
    """
    # Predicted values
    predicted_y = [beta_hat_0 + beta_hat_1 * x for x in data_x]
    
    # Calculate the mean of observed values
    mean_y = sample_mean(data_y)
    
    # Calculate SST
    sst = sum((y - mean_y) ** 2 for y in data_y)
    
    # Calculate SSR
    ssr = sum((data_y[i] - predicted_y[i]) ** 2 for i in range(len(data_y)))
    
    # Calculate R^2
    r_squared = 1 - (ssr / sst)
    return r_squared

    """
    def count_significant_digits(number):
        Returns the number of significant digits in a number
        return len(str(number).rstrip('0').replace('.', ''))
    """


def main(test_data=None):
    # Input data points
    if test_data:
        data1 = test_data[0]
        unit1 = test_data[1]
        data2 = test_data[2]
        unit2 = test_data[3]
    else:
        data1 = list(map(float, input('Enter the first set of points separated by spaces or commas: ').replace(',', ' ').split()))
        unit1 = input('Enter the units of measurement for the first dataset: ')
        data2 = list(map(float, input('Enter the second set of points separated by spaces or commas: ').replace(',', ' ').split()))
        unit2 = input('Enter the units of measurement for the second dataset: ')

    # Calculate and print results
    mean1 = sample_mean(data1)
    std_dev1 = sample_std_dev(data1)
    mean2 = sample_mean(data2)
    std_dev2 = sample_std_dev(data2)
    covariance = sample_covariance(data1, data2)
    max_cov = max_covariance(std_dev1, std_dev2)
    min_cov = min_covariance(std_dev1, std_dev2)
    unit_product_string = unit1 + " * " + unit2
    correlation = covariance / (max_cov if covariance > 0 else min_cov)
    beta_hat_1 = calculate_beta_hat_1(covariance, std_dev1 ** 2)
    beta_hat_0 = calculate_beta_hat_0(mean1, mean2, beta_hat_1)
    correlation_squared = correlation ** 2
    r_squared = direct_r_squared(data1, data2, beta_hat_1, beta_hat_0)
    """
    if r_squared is not None and correlation_squared is not None:
        sd_r = count_significant_digits(r_squared)
        sd_corr = count_significant_digits(correlation_squared)
        if sd_r > sd_corr:
            r_squared = round(r_squared, sd_corr)
        elif sd_corr > sd_r:
            correlation_squared = round(correlation_squared, sd_r)
    """

    print(f'Sample Mean of Data1: {mean1} [{unit1}]')
    print(f'Sample Standard Deviation of Data1: {std_dev1} [{unit1}]')
    print(f'Sample Mean of Data2: {mean2} [{unit2}]')
    print(f'Sample Standard Deviation of Data2: {std_dev2} [{unit2}]')
    print(f'Sample Covariance: {covariance} [{unit_product_string}]')
    print(f'Maximum Covariance when perfectly correlated: {max_cov} [{unit_product_string}]')
    print(f'Minimum Covariance when perfectly anti-correlated: {min_cov} [{unit_product_string}]')
    print(f'Correlation Coefficient: {correlation}')
    print(f'Beta Hat 1: {beta_hat_1} [{unit2}/{unit1}]')
    print(f'Beta Hat 0: {beta_hat_0} [{unit2}]')
    """
    if r_squared and r_squared == correlation_squared:
        print(f"The direct method is equivalent to correlation squared: {r_squared}")
    else:
        print(f"The direct method is not equivalent to correlation squared: {r_squared} vs. {correlation_squared}")
    """

# Test case 1:
import numpy as np
# Test data
test_data_Xs = np.array([0.0339, 0.0423, 0.213, 0.257, 0.273, 0.273, 0.450, 0.503, 0.503, \
0.637, 0.805, 0.904, 0.904, 0.910, 0.910, 1.02, 1.11, 1.11, 1.41, \
1.72, 2.03, 2.02, 2.02, 2.02])
units_X = "Mpc"

test_data_Ys = np.array([-19.3, 30.4, 38.7, 5.52, -33.1, -77.3, 398.0, 406.0, 436.0, 320.0, 373.0, \
93.9, 210.0, 423.0, 594.0, 829.0, 718.0, 561.0, 608.0, 1.04E3, 1.10E3, \
840.0, 801.0, 519.0])
units_Y = "km/s"

# Test case 2:
Xs_2 = np.array([ 0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5 ])

Ys_2 = np.array([ 0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248 ])

if __name__ == '__main__':
    main((test_data_Xs, units_X, test_data_Ys, units_Y))
    main((Xs_2, "AU", Ys_2, "Years"))

