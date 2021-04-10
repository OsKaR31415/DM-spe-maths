import matplotlib.pyplot as plt
import numpy as np


def Euler(x0, xf, y0, n):
    """
    Solution approchée de l'équa diff y'=y avec y(x_0)=y_0
    x0 sera une des bornes de l'intervalle
    xf sera l'autre borne de l'intervalle
    n est le nombre de points créés - 1
    La fonction renvoie les listes des abscisses et des ordonnées des points créés
    """
    x = x0
    y = y0
    h = (xf - x0) / n
    abscisses = [x0]
    ordonnees = [y0]
    for i in range(n):
        x = x + h
        y = y * (1 + h)
        abscisses.append(x)
        ordonnees.append(y)
    return abscisses, ordonnees


def Euler_bis(x0, xf, a, b, y0, n):
    """
    Solution approchée de l'équa diff y'=ay+b avec y(x_0)=y_0
    x0 sera une des bornes de l'intervalle
    xf sera l'autre borne de l'intervalle
    n est le nombre de points créés - 1
    La fonction renvoie les listes des abscisses et des ordonnées des points créés
    """
    x = x0
    y = y0
    h = (xf - x0) / n
    abscisses = [x0]
    ordonnees = [y0]
    for i in range(n):
        x = x + h
        y = y * (1 + a * h) + h * b
        abscisses.append(x)
        ordonnees.append(y)
    return abscisses, ordonnees


# Approximation
x, y = Euler_bis(2, 5, -0.5, 3, 1, 30)
x, y = Euler(0, 5, 1, 30)
abscisses = np.array(x)
ordonnees = np.array(y)
# tracé du nuage des points dont les coordonnées sont les éléments couleur "red" et marqueur "square"
approximation = plt.scatter(abscisses, ordonnees, c="r", label="approchée")
# des listes x et y pris les uns après les autres

# La solution exacte
y = np.exp(abscisses)
exacte = plt.plot(x, y, "b.", label="exacte")  # points bleus non reliés

plt.legend()
plt.show()
