---
title: Devoir maison de mathématiques n°5
date: Pour le Dimanche 31 Janvier
author: Oscar Plaisant
documentclass: scrartcl
fontsize: 12pt
header-includes: |
    \usepackage[utf8]{inputenc}
    \usepackage[T1]{fontenc}
    \usepackage[french]{babel}
    \usepackage[left=1cm, right=1cm, top=5cm, bottom=2.5cm]{geometry}
    \usepackage{enumerate}
    \usepackage{amsmath, amsfonts, amssymb, amsthm, mathrsfs}
    \usepackage{fancyhdr}
---
\newgeometry{top=2cm, bottom=2.5cm, left=1cm, right=1cm}
\pagestyle{fancy}
\renewcommand{\headrulewidth}{.5px}
\renewcommand{\footrulewidth}{1pt}
\fancyfoot[L]{Oscar Plaisant}
\fancyfoot[C]{p.\thepage/\pageref{lastpage}}
\fancyfoot[R]{DM n$^\circ$ 5}



# Exercice 1 :

On sait que seuls 4 triangles sont à considérer: RME, RMT, TMC et EMC.

##### Les triangles RME et RMT

On cherche à montrer que 

Donc, parce que l'on sait que $(s) \perp [RE]$ et que $(d) \perp [RT]$, on peut conclure que RME et RME sont tous les deux des triangles rectangles.

##### Le triangle CME

Pour monter que le triangle CME est rectangle en E, on cherche à monter que $\vec{CE}\cdot\vec{CM} = 0$

On sait, d'après la relation de chasles, que $EM = ER + RM$.

On peut donc dire que :
$\begin{array}{rcl}
    \vec{EC}\cdot\vec{EM} &=& \vec{EC}\cdot\left(\vec{ER} + \vec{RM}\right)\\
                          &=& \vec{EC}\cdot\vec{ER} + \vec{EC}\cdot\vec{RM}\\
\end{array}$

Or, [EC] et [ER] sont des cotés adjacents de RECT qui est un rectangle. EC est donc orthogonal à ER, et $(d)$ est orthogonale au plan $\mathcal{P}$, donc toutes les droites sur $\mathcal{P}$ qui passent par R sont orthogonales à $(d)$, et le vecteur $\vec{ER}$ est orthogonal au vecteur $\vec{RM}$. Les produits scalaires $\vec{EC}\cdot\vec{ER}$ et $\vec{EC}\cdot\vec{RM}$ sont donc nuls.

On en déduit que :

$\begin{array}{rcl}
    \vec{EC}\cdot\vec{EM} &=& 0+0\\
                          &=& 0
\end{array}$

Puisque le produit scalaire de ces deux vecteurs est nul, on sait qu'ils sont orthogonaux, et donc que le triangle CME est rectangle en E.

##### Le triangle TMC


Pour monter que le triangle TMC est rectangle en T, on cherche à monter que $\vec{TC}\cdot\vec{TM} = 0$

On sait, d'après la relation de chasles, que $TM = TR + RM$.

On peut donc dire que :
$\begin{array}{rcl}
    \vec{TC}\cdot\vec{TM} &=& \vec{TC}\cdot\left(\vec{TR} + \vec{RM}\right)\\
                          &=& \vec{TC}\cdot\vec{TR} + \vec{TC}\cdot\vec{RM}\\
\end{array}$

Or, [TC] et [TR] sont des cotés adjacents de RECT qui est un rectangle. TC est donc orthogonal à TR, et $(d)$ est orthogonale au plan $\mathcal{P}$, donc toutes les droites sur $\mathcal{P}$ qui passent par R sont orthogonales à $(d)$, et le vecteur $\vec{TR}$ est orthogonal au vecteur $\vec{RM}$. Les produits scalaires $\vec{TC}\cdot\vec{TR}$ et $\vec{TC}\cdot\vec{RM}$ sont donc nuls.

On en déduit que :

$\begin{array}{rcl}
    \vec{TC}\cdot\vec{TM} &=& 0+0\\
                          &=& 0
\end{array}$

Puisque le produit scalaire de ces deux vecteurs est nul, on sait qu'ils sont orthogonaux, et donc que le triangle TMC est rectangle en T.




\newpage
# Exercice 2 :

## Partie A : Principe

 1. Une équation de la tangente à $\mathcal{C}_f$ en $M_0$ est : $y=f'(x_0)(x - x_0) + f(x_0)$

 2. On cherche le point qui est l'intersection entre l'axe des abcisses et la droite d'équation :
  $$y = f'(x_0)(x-x_0) + f(x_0)$$

    On cherche donc à résoudre l'équation suivante pour $x_1$:

    $\begin{array}{rcl}
      f'(x_0)(x_1-x_0) + f(x_0) = 0 &\iff& f'(x_0)(x_1 - x_0) = - f(x_0)\\
                                    &\iff& x_1 - x_0 = - \dfrac{f(x_0)}{f'(x_0)}\\
                                    &\iff& x_1 = x_0 - \dfrac{f(x_0)}{f'(x_0)}\\
    \end{array}$

 3. On sait que $f$ est convexe. La courbe $\mathscr{C}_f$ est donc au dessus de ses tangentes. Puisque $x_0 \leq c$, et que le point $c$ a une abcisse égale à $f(c) = 0$, on sait donc que la tangente à $\mathscr{C}_f$ en $x_0$ est en dessous de la courbe au point d'abcisse $c$, et donc que, soit $\mathscr{T}_0$ la fonction dont la courbe représentative est la tangente à $\mathscr{C}_f$ en $x_0$, $\mathscr{T}_0(c)$ est inférieur à 0.

    $\begin{array}{rcl}\mathscr{T}_0(c) \leq 0 &\iff& f'(c)(c - x_0) + f(x_0) \leq 0\\ &\iff& f'(c)(c- x_0)  \leq -f(x_0)\\ &\iff& c - x_0 \leq -\dfrac{f(x)}{f'(x)}\\ &\iff& c \leq x_0 - \dfrac{f(x)}{f'(x)}\\\end{array}$



    Or, on sait (voir le 2.) que $x_0 - \dfrac{f(x)}{f(x)}{f'(x)} = x_1$, on obtient donc :

    $\begin{array}{rcl}\mathscr{T}_0(c) \leq 0 &\iff& c \leq x_0 - \dfrac{f(x)}{f'(x)}\\ &\iff& c \leq x_1\end{array}$.

 4. On procède de la même manière que pour le 2.

    A chaque étape, on cherche à  nésoudre l'équation $f'(x_n)(x_{n+1} - x_n) + f(x_n) = 0$ :

    $\begin{array}{rcl}
        f'(x_n)(x_{n+1} - x_n) + f(x_n) = 0 &\iff& f'(x_n)(x_{n+1} - x_n) = - f(x_n)\\
                                            &\iff& x_{n+1} - x_n = - \dfrac{f(x_n)}{f'(x_n)}\\
                                            &\iff& x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}\\
    \end{array}$

 5. On utilise une démonstration par récurrence.

    On cherche à montrer que : $\forall n\in \mathbb{N}, c \leq x_n$

    ##### Initialisation

    On sait par l'énoncé que $x_0 \geq c$, et on sait (voir le 3.) que $x_1 \geq c$ .



    ##### Récurrence

    Pour tout $n$ réel, on sait que, si $x_n \geq c$, alors la tangente à $\mathscr{C}_f$ en $x_0$ est en dessous de $\mathscr{C}_f$. Puisque le point d'abscisse $c$ à une ordonnée $f(c) = 0$, on peut dire que, soit $\mathscr{T}_n$ la tangente à $\mathscr{C}_f$ en $\mathscr{M}_n$ , on a $x_n \leq c \implies \mathscr{T}_n(c) \leq 0$.

    Or, on sait que :

    $\begin{array}{rcl}
        x_n \leq c &\implies& \mathscr{T}_n(c) \leq 0\\
        &\implies& f'(c)(c - x_n) + f(x_n) \leq 0\\
        &\implies& f'(c)(c - x_n) \leq -f(x_n)\\
        &\implies& c - x_n \leq - \dfrac{f(x_n)}{f'(x_n)}\\
        &\implies& c \leq x_n - \dfrac{f(x_n)}{f'(x_n)}\\
        &\implies& c \leq x_{n+1}
    \end{array}$


## Partie B : Application

 1. $f$ est une fonction polynôme du troisième degré, elle est donc dérivable sur $\mathbb{R}$, et sa dérivée est continue sur cet intervalle.

     $f'(x) = 3x^2 - 2x - 0.5$

     $f'$ est donc une fonction polynôme du second degré.

    $\begin{array}{rcl}
        \Delta' &=& (-2)^2 - 4\cdot 3\cdot -0.5\\
                &=& 4+6\\
                &=& 10\\
        \Delta' &>& 0\\
    \end{array}$

    Donc, $f'$ s'annule 2 fois sur $\mathbb{R}$

    $S = \left\{ \dfrac{-b-\sqrt{\Delta}}{2a}; \dfrac{-b+\sqrt{\Delta}}{2a}\right\} = \left\{ \dfrac{2-\sqrt{10}}{6}; \dfrac{2-\sqrt{10}}{6}\right\}$

    La fonction $f'$ a un coefficient devant $x$ positif, donc elle possède un minimum dans $\mathbb{R}$. Ce minimum est situé au point d'abcisse $-\dfrac{b}{2a} = \dfrac{-(-2)}{2\cdot 3} = \dfrac{2}{6} = \dfrac{1}{3}$

    Puisque $f'$ est une fonction polynôme du second degré, on peut dire qu'elle est croissante après son sommet (ici don minimum, en $\dfrac{1}{3}$). On peut donc dire que $f'$ est croissante sur I, car $c > \dfrac{1}{3}$ 

    On sait que $f'$ est croissante sur I et que $f'(1) = 3(1)^2 - 2(1) - 0,5 = 0,5 > 0$, on peut dire que pour tout $x$ dans I, $f'(x) > 0$.
    duit que $f$ est strictement croissante sur I.

    $f''(x) = 6x - 2$

    $f''$ est une fonction affine. Son coefficient dirrecteur est 6, elle est donc croissante.

    $\begin{array}{rcl}
    f''(x) > 0 & \iff & 6x - 2 > 0\\
           &\iff& 6x > 2\\
           &\iff& x > \dfrac{1}{3}
    \end{array}$

    Puisque, pour tout $x > \dfrac{1}{3}$, $f(x) > 0$, on peut dire que $f''$ est positive sur I, que $f'$ est croissante sur I et que $f$ est convexe sur I.

    2. $f$ est une fonction polynôme du troisième degré, donc dérivable, et on sait qu'elle est strictement croissante sur I. $f$ est donc continue et strictement monotone sur I. De plus, $f(1) = 1,2$ et $f(3) = 15,8$ (1 et 3 sont les bornes de l'intervalle I). D'après le corollaire du théorème des valeurs intermédiaires, on peut donc dire que l'équation $f(x) = 0$ admet une unique solution sur I.

    \newpage{}
    3. programme en langage python :
    ```python
    def f(x: int or float) -> int or float:
        return x**3 - x**2 - 0.5*x - 0.7

    def derivee(x: int or float) -> int or float:
        return 3*x**2 - 2*x - 0.5

    def newton(x: int or float, n: int) -> int or float:
        for i in range(n):
            x = x - (f(x) / derivee(x))
        return x
    ```


    4. Si on souhaite avoir l'affichage de ces valeurs, on peut soit taper ceci dans la console après que le script aie été lancé:


    ```python
    >>> for rang in range(10):
    ...     print(newton(3, rang))
    ```


    soit changer le script précédent pour celui-ci (ajout des 3 dernières lignes) :


    ```python
    def f(x: int or float) -> int or float:
        return x**3 - x**2 - 0.5*x - 0.7

    def derivee(x: int or float) -> int or float:
        return 3*x**2 - 2*x - 0.5

    def newton(x: int or float, n: int) -> int or float:
        for i in range(n):
            x = x - (f(x) / derivee(x))
        return x

    if __name__ == "__main__":
        for rang in range(10):
            print(newton(3, rang))
    ```




\label{lastpage}
