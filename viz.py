import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('Result.csv')

N = np.arange(10**3, 10**4 + 1, 10**3)
mean_deg = np.arange(5, 25, 5)

# x = []
# energy = []
# time = []
# for n in N:
#     x.append(n)
#     values = df[df['n'] == n].iloc[:, -2:].to_numpy()
#     energy.append(
#         np.mean(values[:, 0])
#     )
#     time.append(
#         np.mean(values[:, 1])
#     )

# fig, ax = plt.subplots(nrows=1, ncols=1, dpi = 300)

# ax.plot(x, np.array(energy) / x, label = "Mean")
# ax.set_ylabel("Energy Density")
# ax.set_xlabel("Number of vertices")
# # ax.set_ylim([0, 1])
# ax.legend()
# plt.show()

# fig, ax = plt.subplots(nrows=1, ncols=1, dpi = 300)

# ax.plot(x, np.array(time), label = "Mean")
# ax.set_ylabel("Runtime")
# ax.set_xlabel("Number of vertices")
# # ax.set_ylim([0, 1])
# ax.legend()
# plt.show()

x = []
energy = []
time = []
for n in N:
    x.append(n)
    values = df[df['n'] == n].iloc[:, -2:].to_numpy()
    energy.append(values[0, 0])
    time.append(values[0, 1])

fig, ax = plt.subplots(nrows=1, ncols=1, dpi=300)

ax.plot(x, np.array(energy) / x, label="Mean degree = 5")
ax.set_ylabel("Energy Density")
ax.set_xlabel("Number of vertices")
# ax.set_ylim([0, 1])
ax.legend()
plt.savefig("EDbyN.png")

fig, ax = plt.subplots(nrows=1, ncols=1, dpi=300)

ax.plot(x, np.array(time), label="Mean degree = 5")
ax.set_ylabel("Runtime")
ax.set_xlabel("Number of vertices")
# ax.set_ylim([0, 1])
ax.legend()
plt.savefig("TimebyN.png")

c = []
energy = []
time = []
for m in mean_deg:
    c.append(m)
    values = df[df['c'] == m].iloc[:, -2:].to_numpy()
    energy.append(values[-1, 0])
    time.append(values[-1, 1])

fig, ax = plt.subplots(nrows=1, ncols=1, dpi=300)

ax.plot(c, np.array(energy) / 10000, label="No. of vertices : 10000")
ax.set_ylabel("Energy Density")
ax.set_xlabel("Mean degree of vertices")
ax.set_ylim([0.95, 1])
ax.legend()
plt.savefig("EnergybyM.png")

fig, ax = plt.subplots(nrows=1, ncols=1, dpi=300)

ax.plot(c, np.array(time), label="No. of vertices : 10000")
ax.set_ylabel("Runtime")
ax.set_xlabel("Mean degree of vertices")
# ax.set_ylim([0, 1])
ax.legend()
plt.savefig("TimebyM.png")

values = df.to_numpy()
x = np.arange(10**3, 10**4 + 1, 10**3)
y = np.arange(5, 25, 5)
z = values[:, 2].reshape(4, 10)
x.shape, y.shape, z.shape

fig, ax = plt.subplots(dpi=300)
X, Y = np.meshgrid(x, y)
cp = ax.contourf(X, Y, z)
ax.set_title("Cardinaality of FVS")
ax.set_ylabel("Mean Degree of vertices")
ax.set_xlabel("No. of vertices")
fig.colorbar(cp)
plt.savefig("Energy_contour.png")

values = df.to_numpy()
x = np.arange(10**3, 10**4 + 1, 10**3)
y = np.arange(5, 25, 5)
z = values[:, 3].reshape(4, 10)
x.shape, y.shape, z.shape

fig, ax = plt.subplots(dpi=300)
X, Y = np.meshgrid(x, y)
cp = ax.contourf(X, Y, z)
ax.set_title("Runtime")
ax.set_ylabel("Mean Degree of vertices")
ax.set_xlabel("No. of vertices")
fig.colorbar(cp)
plt.savefig("Time_contour.png")
