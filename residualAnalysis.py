import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import sampleCovariance


def plot_residuals(data_x, data_y, beta_hat_1, beta_hat_0):
    # Predicted values
    predicted_y = [beta_hat_0 + beta_hat_1 * x for x in data_x]
    
    # Calculate residuals
    residuals = [data_y[i] - predicted_y[i] for i in range(len(data_y))]
    
    # Residual plot
    plt.scatter(predicted_y, residuals)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')
    plt.show()

    # Normality test
    stat, p_value = stats.shapiro(residuals)
    print(f'Shapiro-Wilk Test: Statistics={stat}, p-value={p_value}')
    if p_value > 0.05:
        print('Residuals are normally distributed (fail to reject H0)')
    else:
        print('Residuals are not normally distributed (reject H0)')


def main(data_x, data_y, beta_hat_1, beta_hat_0):
    plot_residuals(data_x, data_y, beta_hat_1, beta_hat_0)


# Test Data:
Xs_2 = np.array([ 0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5 ])
units_X_2 = "AU"
Ys_2 = np.array([ 0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248 ])
units_Y_2 = "Years"


if __name__ == '__main__':
    # Example data for testing
    test_data_Xs = np.array([0.0339, 0.0423, 0.213, 0.257, 0.273])
    test_data_Ys = np.array([-19.3, 30.4, 38.7, 5.52, -33.1])
    beta_hat_1 = sampleCovariance.calculate_beta_hat_1(sampleCovariance.sample_covariance(test_data_Xs, test_data_Ys), sampleCovariance.sample_std_dev(test_data_Xs) ** 2)
    beta_hat_0 = sampleCovariance.calculate_beta_hat_0(test_data_Xs, test_data_Ys, beta_hat_1)
    main(test_data_Xs, test_data_Ys, beta_hat_1, beta_hat_0)