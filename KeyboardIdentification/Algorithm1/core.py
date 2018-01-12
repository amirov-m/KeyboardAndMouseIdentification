# >>> from scipy.stats import ks_2samp
# >>> import numpy as np
# >>> 
# >>> np.random.seed(12345678)
# >>> x = np.random.normal(0, 1, 1000)
# >>> y = np.random.normal(0, 1, 1000)
# >>> z = np.random.normal(1.1, 0.9, 1000)
# >>> 
# >>> ks_2samp(x, y)
# Ks_2sampResult(statistic=0.022999999999999909, pvalue=0.95189016804849647)
# >>> ks_2samp(x, z)
# Ks_2sampResult(statistic=0.41800000000000004, pvalue=3.7081494119242173e-77)


import numpy as np
import math

from scipy.stats import ks_2samp


MINIMUM_DATA_POINTS = 5
MINIMUM_SAMPLING_CORRELATION = 0.001


def kolmogorov_smirnov_test(first_sequence, second_sequence):
	return ks_2samp(first_sequence, second_sequence).pvalue


def users_likelihood(first_user, second_user):
	product = 1
	reasonable_letter_pairs = 0

	for i in range(26):
		for j in range(26):
			if min(len(first_user[i][j]), len(second_user[i][j])) >= MINIMUM_DATA_POINTS:
				reasonable_letter_pairs += 1
				product *= kolmogorov_smirnov_test(first_user[i][j], second_user[i][j])

	if reasonable_letter_pairs == 0:
		return float("-inf")

	score = math.log(product) / reasonable_letter_pairs

	return score


if __name__ == "__main__":
	main()