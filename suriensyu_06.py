# %%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

sns.set()
sns.set_style('whitegrid')
sns.set_palette('gray')

a = 6371.2*10e+3

g01 = np.array([-30594,-30554,-30500,-30421,-30334,-30220,-30100,-29992,-29873,-29775,-29682,-29615])
g11 = np.array([-2285,-2250,-2215,-2169,-2119,-2068,-2013,-1956,-1905,-1848,-1789,-1728])
h11 = np.array([5810,5815,5820,5791,5776,5737,5675,5604,5500,5406,5318,5186])
year = np.arange(1945,2001,5)

M = a**3*(g01**2+g11**2+h11**2)**0.5


sita0 = (g11**2+h11**2)**0.5 / g01
ramda0 = h11/ g11

print(M[0])

fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax2 = fig2.add_subplot(1, 1, 1)
ax3 = fig3.add_subplot(1, 1, 1)
ax1.plot(year, M)
ax2.plot(year, sita0)
ax3.plot(year, ramda0)
ax1.set_xlabel('year')
ax2.set_xlabel('year')
ax1.set_ylabel('M(10e27)')
ax2.set_ylabel('tan')
ax3.set_ylabel('tan')
ax1.set_title("Time variation of dipole moment")
ax2.set_title("Time variation of axis direction")
ax3.set_title("Time variation of axis direction")

fig1.savefig("01.png")
fig2.savefig("02.png")
fig3.savefig("03.png")
# ax.set_ylim(0, 2)
plt.show()