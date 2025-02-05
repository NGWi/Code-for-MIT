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

    print(f'Sample Mean of Data1: {mean1} [{unit1}]')
    print(f'Sample Standard Deviation of Data1: {std_dev1} [{unit1}]')
    print(f'Sample Mean of Data2: {mean2} [{unit2}]')
    print(f'Sample Standard Deviation of Data2: {std_dev2} [{unit2}]')
    print(f'Sample Covariance: {covariance} [{unit_product_string}]')
    print(f'Maximum Covariance when perfectly correlated: {max_cov} [{unit_product_string}]')
    print(f'Minimum Covariance when perfectly anti-correlated: {min_cov} [{unit_product_string}]')

# Test case:
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


if __name__ == '__main__':
    main((test_data_Xs, units_X, test_data_Ys, units_Y))

