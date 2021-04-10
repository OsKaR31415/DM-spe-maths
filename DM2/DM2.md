

# Exercice 1 :

$f$ est la fonction définie sur $\mathbb{R}$ par : $f(x) = xe^{\frac{-x^2}{2}}$.
On note $\mathscr{C}$ la courbe représentative de la fonction $f$ dans un repère orthonormé du plan.

## 1. Étude de la fonction

### a) étudier la parité de la fonction $f$

On sait, par définition qu'une fonction $f$ est paire si et seulement si pour tout $x$ dans $\mathbb{R}$, $f(-x) = f(x)$, et qu'une fonction est impaire si et seulement si pour tout $x$ dans $\mathbb{R}$, $f(-x) = -f(x)$.
    
Or, on sait que $f(-x) = -xe^{\frac{-x^2}{2}} = -f(x)$, on peut donc dire que la fonction $f$ est impaire.
    

### b) Établir le tableau de variations de $f$ sur l'intervalle $[0; +\infty[$.

On calcule d'abord $f'$ :
    
On pose $u(x) = x$, $u'(x) = 1$; $v(x) = \dfrac{-x^2}{2}$, $v'(x) = -x$
    

$$
    \begin{array}{rl}
        f'(x) &= u'(x)\left(e^v\right)(x) + u(x)\left(e^v\right)'(x)\\
              &= 1\left(e^{\frac{-x^2}{2}}\right) + x\left(-xe^{\frac{-x^2}{2}}\right)\\
              &= e^{\frac{-x^2}{2}} - x^2e^{\frac{-x^2}{2}}\\
              &= e^{\frac{-x^2}{2}}\left(1-x^2\right)\\
    \end{array}
$$

On cherche à déterminer le signe de $1-x^2$ sur $\mathbb{R}^+$, or $1-x^2>0 ⟺ x^2 < 1 ⟺ x < 1$
|              $x$              |    $0$     |    $1$     | $+\infty$  |
|:-----------------------------:|:----------:|:----------:|:----------:|
| signe de $e^{\frac{-x^2}{2}}$ |    $+$     |    $+$     |    $+$     |
|       signe de $1-x^2$        |    $-$     |    $+$     |    $-$     |
|       signe de $f'(x)$        |    $-$     |    $+$     |    $-$     |
|       variations de $f$       | $\searrow$ | $\nearrow$ | $\searrow$ |

### c) Déterminer une équation de la tangente $T_0$ à la courbe $\mathscr{C}$ au point d'abscisse $0$.

Une équation de la tangente est :

$$
    \begin{array}{rll}
        y &=& f'(a)(x-a) + f(a)\\
          &=& \left(e^{\frac{-a^2}{2}}\left(1-a^2\right)\right)(x - a) + ae^{\frac{-x^2}{2}}\Big{|}_{a=0}\\
          &=& \left(e^{\frac{-(0)^2}{2}}\left(1-(0)^2\right)\right)(x - 0) + (0)e^{\frac{-x^2}{2}}\\
          &=& e^{0}(x - 0)\\
        y &=& x
    \end{array}
$$

### d) Étudier la convexité de $f$ et déterminer les éventuels points d'inflextion

Pour étudier la convexité de $f$, on cherche le signe de $f''(x)$.

On pose :

$$
    \begin{array}{c}
        u(x) = e^{\frac{-x^2}{2}}\\
        u'(x) = -xe^{\frac{-x^2}{2}}\\
        \\
        v(x) = 1-x^2\\
        v'(x) = -2x\\
    \end{array}
$$

On sait que :

$$
f'(x) = u(x)v(x)
$$

On en déduit que :

$$
\begin{array}{rll}
        f''(x) &= u'(x)v(x) + u(x)v'(x)\\
               &= -xe^{\frac{-x^2}{2}}\left(1-x^2\right) - 2xe^{\frac{-x^2}{2}}\\
               &= e^{\frac{-x^2}{2}}\left(-x\left(1-x^2\right) - 2x\right)\\
               &= e^{\frac{-x^2}{2}}\left(x^3 - 3x \right)\\
               &= e^{\frac{-x^2}{2}}\left(x\left(x^2 - 3\right)\right)\\
               &= xe^{\frac{-x^2}{2}}\left(x^2 - 3\right)
    \end{array}
$$

On sait que la fonction exponentielle est positive $\mathbb{R}$. On peut donc dire que $e^{\frac{-x^2}{2}} > 0$.
On cherche le signe de $(x^2 - 3)$ : $x^2 - 3 > 0 ⟺ x^2 > 3 ⟺ -\sqrt{3} > x > \sqrt{3}$ 
On à donc :

|              $x$               | $-\infty$ | $-\sqrt{3}$ | $-1$ | $0$  | $\sqrt{3}$ |
| :----------------------------: | :-------: | :---------: | :--: | :--: | :--------: |
| signe de $xe^{\frac{-x^2}{2}}$ |    $-$    |     $-$     | $-$  | $0$  |    $+$     |
|        signe de $x^2-3$        |    $+$    |     $0$     | $-$  | $-$  |    $-$     |
|       signe de $f''(x)$        |    $-$    |     $0$     | $+$  | $0$  |    $-$     |

On voit donc que $f$ est concave sur $]-\infty; -\sqrt{3}]$, puis convexe sur $[-\sqrt{3}; 0]$, concave sur $[0; \sqrt{3}]$ et enfin convexe sur $[\sqrt{3}; +\infty]$.

__e) Tracer $T_0$ et $\mathscr{C}$ dans un repère orthonormé du plan, en choisissant une unité graphique adaptée.__

![Graphique](Graphique.pdf)


# Exercice 2: 

$$
    (u_n): \left\{
        \begin{array}{l}
            u_0 = 1\\
            u_{n+1} = f(u_n)
        \end{array}
    \right.
$$

__a) Montrer que, pour tout entier naturel $n$, $0 \leq u_n \leq 1$.__

On utilise une démonstration par réccurence, avec la proposition $P_n: 0 \leq u_n \leq 1$



### Initialisation

$P_0 \iff 0\leq u_0\leq 1 \iff 0\leq 1\leq 1$, donc $P_0$ est vraie.

### Hérédité

On cherche à démontrer que $P_n \implies P_{n+1}$. On suppose donc que $P_n$ est vraie.

$$
\begin{array}{rrl}P_{n+1} &\iff& 0\leq f(u_n)\leq 1\\ &\iff& 0\leq u_ne^{\frac{-u_n^2}{2}}\leq 1\\\end{array}
$$

Or, on sait que $0\leq u_n\leq 1$, on peut en déduire que $0\leq u_n^2\leq 1$, que $0\leq \dfrac{-u_n^2}{2}$, que $e^0\geq e^{\frac{-u_n^2}{2}}\geq e^{-1}$, et donc que $1\geq e^\frac{-u_n^2}{2}\geq e^{-1}$ car la fonction carré est croissante sur $\mathbb{R}^+$, car la fonction $x\mapsto \dfrac{-x}{2}$ est décroissante sur $\mathbb{R}$, et car la fonction exponentielle croissante sur $\mathbb{R}$.

On peut donc en déduire que $0\leq u_n \leq 1$, puisque la fonction exponentielle est positive sur $\mathbb{R}$, et donc que $e^{-1}\geq 1$.

__b) Déduire de la convexité de la fonction $f$ le sens de variation de la suite $(u_n)$__

Pour étudier les variation de $(u_n)$, on commence par chercher si $f(x) > x$, ce qui revient à chercher le signe de $f(x)-x$, soit le signe de $xe^{\frac{-x^2}{2}}-x = x(e^{\frac{-x^2}{2}} - 1)$. On sait que la fonction exponentielle est croissante sur $\mathbb{R}$, et inférieure à $1$ sur $\mathbb{R}^-$. On en déduit donc que $e^{\frac{-x^2}{2}} - 1$ est négatif sur $\mathbb{R}^-$, nul en $x=0$ et positif sur $\mathbb{R}^+$ , soit du signe de $x$. En multipliant par $x$, on ne change donc pas le signe. $xe^{\frac{-x^2}{2}}-x$ est donc du signe de x. Sur $\mathbb{R}^+$ (le domaine qui nous intéresse pour $(u_n)$), $f(x)\geq x$, et on peut donc dire que $(u_n)$ est croissante, puisque chacun de ses termes est supérieur ou égal au précédent. On peut même dire que $(u_n)$ est strictement croissante sur $\mathbb{R}^*_+$, puisque, sur cet intervalle, $f(x) > x$.

__c) On admet que la suite $(u_n)$ est convergente et que sa limite est $L = 0$. Écrire un algorithme en langage naturel de sorte qu'il détermine le plus petit rang $n_0$ à partir duquel, pour tout $n\leq 0$, $|u_0|\leq 10^{-1}$__

Puisque l'on est en langage naturel, on pourrait dire :

```
retourner le plus petit k pour k entier naturel tel que pour tout n supérieur ou égal à k, |u(n)| est inférieur à 0.1.
```

avec ```u(n)``` définit comme :

```
0 si n est nul, le produit de u(n-1) et de l'exponentielle de la moitié de l'opposé de u(n-1) sinon.
```

soit :

```
retourner le plus petit k pour k entier naturel tel que pour tout n supérieur ou égal à k, la valeur absolue de la fonction qui renvoie 0 si son entrée est nulle et elle même avec pour entrée son entrée moins 1 — appelée en n est inférieur à 0.1.
```

Cependant, cette réponse ne correspond pas à certaines définitions du langage naturel. On pourra donc plutôt dire :

```
On définit f, une fonction d'argument x, qui retourne:
  x⋅exp(-(x⋅x)÷2)

On définit U, une fonction d'argument n, qui retourne :
  si n est nul : 0
  sinon : la f(U(n-1))

k ← 0
Tant que |U(n)| >= .1:
  k ← k + 1

retourner k
```

__d) Coder cet algorithme en langage _Python_. Donner le programme, le saisir, l’exécuter. Indiquer la valeur de $n_0$ obtenue.__

```python
from math import exp
def f(x: float) -> float:
    return x * exp((- x ** 2)/2)

def U(n: int) -> float:
    return 1 if not n else f(U(n - 1))

if __name__ == "__main__":
    k = 0
    while abs(U(k)) >= .1:
        k += 1
    print(k)
```

_Python_ 3.8 permet un petit changement assez joli dans la boucle while :

```python
from math import exp
def f(x: float) -> float:
    return x * exp((- x ** 2)/2)

def U(n: int) -> float:
    return 1 if not n else f(U(n - 1))

if __name__ == "__main__":
    k = 0
    while abs(U(k := k + 1)) >= .1: pass
    print(k)
```

L'éxécution du programme affiche :

```shell python
97
```

Ce qui signifie que $n_0$ vaut 97.
