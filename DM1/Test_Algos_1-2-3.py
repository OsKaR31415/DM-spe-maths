def Algo1(n: int) -> iter:
    """Algo 1 traduit en fonction

    Args:
                    n (int): The number of numbers to compute.

    Yields:
                    iter: An iterable containing the fibonacci numbers.
    """
    u = 1
    v = 1

    yield u
    for j in range(2, n + 1):
        v = u + v
        u = v - u
        yield u


def Algo2(n: int) -> iter:
    """Algo 2 traduit en fonction

    Args:
                    n (int): The number of numbers to compute.

    Yields:
                    iter: An iterable containing the fibonacci numbers.
    """
    u = 1
    v = 1
    yield v
    for j in range(1, n + 1):
        w = u + v
        u = v
        v = w
        yield v


def Algo3(n: int) -> iter:
    """Algo 3 traduit en fonction

    Args:
        n (int): The number of numbers to compute.

    Yields:
        iter: An iterable containing the powers of 2.
        """
    u = 1
    v = 1
    yield v
    for j in range(2, n + 1):
        v = u + v
        u = v
        yield v

if __name__ == "__main__":
    # on trouve la valeur de n par tatonnements, en testant
    # les valeurs possibles.
    n = 7

    print("")
    # print(list(Algo1(n)))
    try:
        assert list(Algo1(n)) == [1, 1, 2, 3, 5, 8, 13]
        print("Algo 1 fonctionne")
    except AssertionError:
        print("Algo 1 ne fonctionne pas")

    print("")
    # print(list(Algo2(n)))
    try:
        assert list(Algo2(n)) == [1, 1, 2, 3, 5, 8, 13]
        print("Algo 2 fonctionne")
    except AssertionError:
        print("Algo 2 ne fonctionne pas")

    print("")
    # print(list(Algo3(n)))
    try:
        assert list(Algo3(n)) == [1, 1, 2, 3, 5, 8, 13]
        print("Algo 3 fonctionne")
    except AssertionError:
        print("Algo 3 ne fonctionne pas")
