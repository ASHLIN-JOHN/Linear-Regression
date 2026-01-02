#Linear Regression
#Table
x = [1,2,3,4,5]
y = [20,10,35,70,45]

"""
y = ax + b
Find a,b
a = E(x-x0)(y-y0)
    -------------
       E(x-x1)²
       
b = y0 - a.x0
"""
mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)

num = 0   # numerator
den = 0   # denominator

for xi, yi in zip(x, y):
    num += (xi - mean_x) * (yi - mean_y)
    den += (xi - mean_x) ** 2

a = num / den
b = mean_y - a * mean_x

print(f"y = {a}x + {b}")

# R-Squared Method to check the fitness of the linear regression

"""
        SSE
R²= 1 - ___
        SST
          
SSE = E(y-y_cap)²
SST = E(y-y0)²
"""

SSE = 0  # Sum of Squared Errors
SST = 0  # Total Sum of Squares

for xi, yi in zip(x, y):
    y_hat = a * xi + b
    SSE += (yi - y_hat) ** 2
    SST += (yi - mean_y) ** 2

R_squared = int((1 - (SSE / SST))*100)

print(f"{R_squared}% of fitness in the linear regression")

if R_squared >= 95:
    print("It is a Excellent Fit")
elif R_squared >= 90:
    print("It is a Strong Fit")
else:
    print("It is a Poor Fit")
