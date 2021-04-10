import matplotlib.pyplot as plt


def U(n):
    return -160 * (1 / 2)**n + 360


def V(n):
    return U(n) - 360

plt.plot([U(n) for n in range(10)])
print([U(n) for n in range(10)])
# plt.bar([V(n) for n in range(50)])

plt.show()


-160 * (1 / 2)**6 + 360
