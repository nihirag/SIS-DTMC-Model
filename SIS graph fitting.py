import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
x, y = [], []
for line in open('pneumococcus.txt', 'r'):
  values = [float(s) for s in line.split()]
  x.append(values[0])
  y.append(values[1])
N=150000
I=5000
def test(x, a, b, c):
    terms=(b*N)-a-c
    return 1/((b/terms)*(1-np.exp(-terms*x))+(1/I)*np.exp(-terms*x))
param, param_cov = curve_fit(test, x, y)
print("funcion coefficients:")
print(param)
print("Covariance of coefficients:")
print(param_cov)
k=(param[1]*N)-param[0]-param[2]
ans = (1/((param[1]/k)*(1-np.exp(-k*x))+(1/I)*np.exp(-k*x)))
plt.plot(x, y, 'o', color ='red', label ="data")
plt.plot(x, ans, '--', color ='blue', label ="optimized data")
plt.legend()
plt.show()

