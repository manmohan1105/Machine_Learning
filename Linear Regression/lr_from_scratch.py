from statistics import mean
import numpy as np
from matplotlib import style
import matplotlib.pyplot as plt

style.use('fivethirtyeight')

xs = np.asarray([1,2,3,4,5,6], dtype=np.float64)
ys = np.asarray([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope_and_intercept(xs, ys):
	m = ((mean(xs) * mean(ys)) - mean(xs*ys))/((mean(xs)*mean(xs)) - mean(xs*xs))  # PEMDAS
	
	b = mean(ys) - (m * mean(xs))
	return m, b


def squared_error(ys_orig, ys_line):
	return sum((ys_orig - ys_line) ** 2)


def coeff_of_determination(ys_orig, ys_line):
	y_mean_line = [mean(ys_orig) for y in ys_orig]
	squared_error_regr = squared_error(ys_orig, ys_line)
	squared_error_mean_line = squared_error(ys_orig, y_mean_line)
	return (1 - (squared_error_regr/squared_error_mean_line))


m,b = best_fit_slope_and_intercept(xs, ys)
regression_line = [(m*x) + b for x in xs]
r_squared = coeff_of_determination(ys, regression_line)
plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()
