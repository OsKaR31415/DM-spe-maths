
def f(x: float or int) -> float or int:
    return x ** 3 - x ** 2 - 0.5 * x - 0.7

def derivee(x: float or int) -> float or int:
    return 3 * x ** 2 - 2 * x - 0.5

def newton(x: float or int, n: int) -> float or int:
    for i in range(n):
        x = x - (f(x) / derivee(x))
    return x

# if __name__ == "__name__":
for rang in range(10):
    print(newton(3, rang))
