#%%
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://en.wikipedia.org/wiki/Armand_Duplantis"
headers = {"User-Agent": "Mozilla/5.0"}

# Get HTML with a browser-like header
html = requests.get(url, headers=headers).text

# Read only the table that contains that phrase (in caption/header)
tables = pd.read_html(html, match="World records and other milestones")

# There should be exactly one match
df = tables[0]

# Keep just Age and Height
df = df[["Age", "Height"]].copy()

# Convert to numeric and drop junk rows
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")
df = df.dropna(subset=["Age", "Height"]).sort_values("Age")

print(df)  # sanity check



h = np.array(df["Height"])
a = np.array(df["Age"])


matrix = np.zeros((len(a), 4))

age_matrix = np.column_stack((np.ones_like(a),a,a**2,a**3))

print(age_matrix)

X = age_matrix

XtX = X.T @ X
Xty = X.T @ h

B = np.linalg.inv(XtX) @ Xty
print("Betas:", B)

y = Xty = X @ B

b0, b1, b2, b3 = B[0], B[1], B[2], B[3]
def y_model(x):
    return b0 + b1*x + b2*x**2 + b3*x**3

x = np.linspace(6,25, 1000)
y = y_model(x)


y_hat = X @ B

# --- residuals & covariance of parameters ---
n, p = X.shape  # p = 4
resid = h - y_hat

sigma2 = np.sum(resid**2) / (n - p)        # residual variance
XtX_inv = np.linalg.inv(XtX)
cov_B = sigma2 * XtX_inv                   # 4x4 covariance matrix

# --- fine grid for smooth curve + confidence band ---
x_fine = np.linspace(a.min(), a.max(), 1000)
X_fine = np.column_stack((
    np.ones_like(x_fine),
    x_fine,
    x_fine**2,
    x_fine**3
))

y_fine = X_fine @ B

# Var(ŷ(x)) = x* Cov(B) x*^T
var_y = np.einsum("ij,jk,ik->i", X_fine, cov_B, X_fine)
std_y = np.sqrt(var_y)

z = 1.96  # 95% CI
upper = y_fine + z * std_y
lower = y_fine - z * std_y


plt.figure(figsize=(8, 5))
plt.plot(df["Age"], df["Height"], marker="x")
plt.plot(x_fine, y_fine, label="cubic fit")
plt.fill_between(x_fine, lower, upper, alpha=0.2, label="95% CI (mean)")
plt.plot(x, y)
plt.xlabel("Age (years)")
plt.ylabel("PB (m)")
plt.title("Armand Duplantis PB progression by age")
plt.grid(True)
plt.tight_layout()
plt.show()
