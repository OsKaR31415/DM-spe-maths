import random as rd

def simu_X():
    if rd.randint(1, 1000) <= 421:
        return 1
    return 0

def simu_S():
    s = 0
    for esp in range(210):
        s += simu_X()
    return s

def m(n):
    acc = [simu_S() for sim in range(n)]
    return sum(acc) / n


"""
 1. X est une loi correspondant à une épreuve de Bernoulli.
On sait que P(X=1) = 0.421, et donc que P(X=0) = 0.579

 2. Puisque S compte le nomre de 1 dans une répétition d'épreuves correspondant à la loi X, on sait que S est une loi binômiale.
 On sait que S est une loi binômiale de paramètres (210, 0.421)

 3. Cette valeur signifie que la moyenne sur 10000 expériences suivant la loi S est de 88.043
 On peut utiliser cette valeur pour estimer E(S), puisque lorsque n tend vers $+\infty$, la moyenne sur n expériences suivant S tend vers E(X) (loi des grands nombes).

"""


