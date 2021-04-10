import matplotlib.pyplot as plt


def U(n):
    if n <= 2:
        return 1
    return U(n - 2) + U(n - 1)

plt.bar([n - .05 for n in range(11)], [U(n) for n in range(11)], .1)
plt.plot([U(n) for n in range(11)], 'o')

plt.show()


