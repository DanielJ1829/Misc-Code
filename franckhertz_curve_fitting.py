import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks


# choose file and settings
filename = r"C:\Users\danie\Desktop\Projects\roadovscode\DataMercury20msu1is2.50u3is1.50.csv"
n_peaks = 5


#gaussian model
def gaussian(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))

def model(x, c, m, *params):
    y = c + m*x
    for i in range(0, len(params), 3):
        A = params[i]
        mu = params[i+1]
        sigma = params[i+2]
        y += gaussian(x, A, mu, sigma)
    return y

from scipy.ndimage import median_filter
import numpy as np

def remove_outliers(y, window=5, threshold=3):
    y_med = median_filter(y, size=window)
    residuals = y - y_med
    sigma = np.std(residuals)

    mask = np.abs(residuals) < threshold * sigma

    y_clean = y.copy()
    y_clean[~mask] = y_med[~mask]

    return y_clean, mask


#load data:
data = np.loadtxt(filename, delimiter=",")
x = data[:, 0]
y = data[:, 1]

#smooth the data for finding peaks:

y_clean, mask = remove_outliers(y, window=5, threshold=3)
#y_smooth = savgol_filter(y_clean, 11, 3)
# find peaks automatically
peaks, properties = find_peaks(y_clean, prominence=0.03*(max(y)-min(y)), distance=len(x)//15)

#keep the strongest n_peaks
prominences = properties["prominences"]
order = np.argsort(prominences)[::-1]
peaks = peaks[order[:n_peaks]]
peaks = peaks[np.argsort(x[peaks])]


#initial guesses:
c_guess = min(y)
m_guess = 0

p0 = [c_guess, m_guess]
lower = [min(y) - 1, -1]
upper = [max(y) + 1, 1]

sigma_guess = 0.1

for p in peaks:
    A_guess = y[p] - c_guess
    mu_guess = x[p]
    p0 += [A_guess, mu_guess, sigma_guess]
    lower += [0, min(x), 0.05]
    upper += [2*(max(y)-min(y)), max(x), 3]

#fit:
popt, pcov = curve_fit(model, x, y_clean, p0=p0, bounds=(lower, upper), maxfev=20000) #popt = [c, m, A1, mu1, sigma1, A2, mu2, sigma2, ...], pcov = covariance matrix

y_fit = model(x, *popt)

# plot result:
plt.figure(figsize=(8,5))
plt.plot(x, y, ".", label="data")
plt.plot(x, y_fit, "-", label="fit")

baseline = popt[0] + popt[1]*x
plt.plot(x, baseline, "--", label="baseline")

for i in range(2, len(popt), 3):
    A = popt[i]
    mu = popt[i+1]
    sigma = popt[i+2]
    plt.plot(x, baseline + gaussian(x, A, mu, sigma), "--")

plt.xlabel("Voltage / V")
plt.ylabel("Current")
plt.legend()
plt.grid()
plt.show()


#print fitted parameters
print("Baseline:")
print("c =", popt[0])
print("m =", popt[1])

for i in range(n_peaks):
    A = popt[2 + 3*i]
    mu = popt[2 + 3*i + 1]
    sigma = popt[2 + 3*i + 2]
    print(f"Peak {i+1}: A = {A:.3f}, mu = {mu:.3f}, sigma = {sigma:.3f}")

mus = [popt[2 + 3*i + 1] for i in range(n_peaks)]
mus = np.sort(mus)
if len(mus) > 1:
    spacing = np.diff(mus)
    print("Mean peak spacing =", np.mean(spacing))