import random as rd


def bern():
    if rd.randint(1, 1000) <= 270:
        return 1
    return 0


def bino():
    s = 0
    for exp in range(50):
        s += bern()
    return s


def echeant():
    liste = []
    for simu in range(600):
        liste.append(bino())
    return liste


def prop():
    return sum(map(
        lambda x: x <= 10,
        echeant())) / 600


print(prop())


