import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#df lists 
x = [1,2,3,4,76,83,22,90,97,99,39,37,21]
y = [3,5,7,10,34,89,83,91,94,83,24,33,12]

#from lists to array 
array_xy = np.array([x, y])

#poly1d_fn is now a function which takes in x and returns an estimate for y
coef = np.polyfit(x,y,1)
poly1d_fn = np.poly1d(coef) 

#'--k'=black dashed line, 'yo' = yellow circle marker
plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k') 

# plot regression
plt.xlim(0, 100)
plt.ylim(0, 100)

# the means (rows)
meanx = np.mean(array_xy[0])
meany = np.mean(array_xy[1])

#print(meanx)
#print(meany)

# the st values (check numpy.std)
stdx = np.std(array_xy[0])
stdy = np.std(array_xy[1])
 
#trova R1
R1 = np.corrcoef(array_xy)
R=R1[1,0]

# prediction made on linear regression by 

# set driver value
x_obs = 50

# standardize for both above or below
if x_obs >= meanx:
    standnorm = x_obs - meanx
if x_obs <= meanx:
    standnorm = meanx - x_obs

standnorm = standnorm / stdx

if x_obs >= meanx:
    pr_value = meany + R * standnorm * stdy
if x_obs <= meanx:
    pr_value = meany - R * standnorm * stdy

#np.poly_b_1d is now a Residual Plot for underline difference between observed and predicted
coef = np.polyfit_b(x,y,R)
poly2d_fn = np.poly_b_1d(coef) 


print(pr_value)
print(R)
