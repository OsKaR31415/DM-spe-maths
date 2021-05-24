---
title: Devoir Maison de mathématiques n°7
author: Oscar Plaisant
date: Pour le vendredi 9 avril
header-includes: |
    \usepackage[top=2cm, bottom=2.5cm, left=2cm, right=2cm]{geometry}
    \usepackage{amsmath, amssymb}
    \usepackage{mathrsfs}
    \newcommand\Lim{\displaystyle\lim}
    \usepackage{tikz, tkz-tab}
    \newcommand\vect\overrightarrow
---

# Exercice 1:

## Partie A


$u(x) = a + \dfrac{b}{x} + \dfrac{c}{x^2}$

 1. $u(1) = 0$ et $u(4) = 0$

 2. On sait que $\mathscr{D}$ est une asymptote de $\mathscr{C}_u$. Or, puisque $\mathscr{D}$ à pour équation $y = 1$, on peut dire que :

$$\lim_{x \rightarrow +\infty} u(x) = 1$$


On sait également que :

$$
\begin{array}{rcl}
\Lim_{x \rightarrow +\infty} u(x) &=& \Lim_{x \rightarrow +\infty} \left( a + \dfrac{b}{x} + \dfrac{c}{x^2} \right) \\
&=& \Lim_{x \rightarrow +\infty} (a) + \Lim_{x \rightarrow +\infty} \left(\dfrac{b}{x}\right) + \Lim_{x \rightarrow +\infty} \left(\dfrac{c}{x^2}\right)\\
&=& \Lim_{x \rightarrow +\infty} ( a ) + 0 + 0\\
\Lim_{x \rightarrow +\infty} u(x) &=& a\\
\end{array}
$$


On peut donc dire que $a = 1$.

\newpage

 3. On cherche à résoudre le système suivant :

$$
\begin{array}{rcl}
\left\{ \begin{array}{l}
a = 1\\
u(1) = 0\\
u(4) = 0\\
\end{array} \right.
&\iff&
\left\{ \begin{array}{l}
a = 1\\ [2ex]
a + \dfrac{b}{1} + \dfrac{c}{1^2} = 0\\ [2ex]
a + \dfrac{b}{4} + \dfrac{c}{4^2} = 0
\end{array} \right.\\ [8ex]
&\iff& \left\{ \begin{array}{l}
a = 1\\ [2ex]
1 + b + c = 0\\ [2ex]
1 + \dfrac{1}{4}b + \dfrac{1}{16}c = 0
\end{array} \right.\\ [8ex]
&\iff& \left\{ \begin{array}{l}
a = 1\\ [2ex]
b + c = -1\\ [2ex]
b + \dfrac{1}{4}c = -4
\end{array} \right.\\ [8ex]
&\iff& \left\{ \begin{array}{l}
a = 1\\ [2ex]
b = - c - 1\\ [2ex]
b + \dfrac{1}{4}c = -4
\end{array} \right.\\ [8ex]
&\iff& \left\{ \begin{array}{l}
a = 1\\ [2ex]
b = - c - 1\\ [2ex]
- c - 1 + \dfrac{1}{4}c = -4
\end{array} \right.\\ [8ex]
&\iff& \left\{ \begin{array}{l}
a = 1\\ [2ex]
b = - c - 1\\ [2ex]
\dfrac{3}{4}c = 3
\end{array} \right.\\ [8ex]
&\iff& \left\{ \begin{array}{l}
a = 1\\ [2ex]
b = - c - 1\\ [2ex]
c = 4
\end{array} \right.\\ [8ex]
&\iff& \left\{ \begin{array}{l}
a = 1\\ [2ex]
b = -5\\ [2ex]
c = 4
\end{array} \right.\\ [8ex]
\end{array}
$$

On à donc : $u(x) = 1 - \dfrac{5}{x} + \dfrac{4}{x^2}$

$u(x) = \dfrac{x^2 - 5x - 4}{x^2}$
 4. On a :

$$
\begin{array}{rcl}
u(x) &=& 1 - \dfrac{5}{x} + \dfrac{4}{x^2}\\ [2ex]
&=& \dfrac{x^2}{x^2} - \dfrac{5x}{x^2} + \dfrac{4}{x^2}\\ [2ex]
&=& \dfrac{x^2 - 5x - 4}{x^2}
\end{array}
$$

## Partie B

 1. On commence par chercher l'ensemble de définition de $f$.

$\ln$ est définie sur $\mathbb{R}^+_*$
$x\mapsto x^2$ est définie sur $\mathbb{R}$
On peut donc dire que $x\mapsto x^2 - 5x\ln(x) - 4$ est définie sur $\mathbb{R}^+_*$
La fonction inverse est définie sur $\mathbb{R}_*$.
On peut donc dire que $x\mapsto \dfrac{1}{x}\left( x^2 - 5x\ln(x) - 4 \right)$ est définie sur $\mathbb{R}^+_*$

On peut donc dire que $\Lim_{x \rightarrow 0} (f(x)) = \Lim_{x \rightarrow 0^+}(f(x))$

$\Lim_{x \rightarrow 0^+} = \Lim_{x \rightarrow 0^+} (\dfrac{x^2 - 5x\ln(x) - 4}{x^2})$

On sait que :

 - $\Lim_{x \rightarrow 0^+} ( x^2 ) = 0^+$
 - $\Lim_{x \rightarrow^+} ( x\ln(x) ) = 0$

On en déduit que $\Lim_{x \rightarrow 0^+} ( x^2 - 5x\ln(x) - 4) = 4$

Puisque la fonction carré tend vers $0^+$ en 0, par quotient, on obtient $\Lim_{x \rightarrow 0^+} \left( \dfrac{x^2 - 5x\ln(x) - 4}{x^2} \right) = -\infty$

Soit :

$$\Lim_{x \rightarrow 0^+} (f(x)) = -\infty$$

 2. On cherche à déterminer $\Lim_{x \rightarrow +\infty} ( f(x) )$.

$\Lim_{x \rightarrow +\infty} ( f(x) ) = \Lim_{x \rightarrow +\infty} \left(  x - 5\ln(x) + \dfrac{4}{x} \right)$

On sait que $\Lim_{x \rightarrow +\infty} \left(  \dfrac{4}{x} \right) = 0$.

On chercher à calculer $\Lim_{x \rightarrow +\infty} ( x - 5\ln(x) )$

On pose $X = \ln(x)$. On a donc :
$\Lim_{x \rightarrow +\infty} ( x - 5\ln(x) ) = \Lim_{X \rightarrow +\infty} \left(  e^X - 5X \right)$

Et, par croissance comparée, on sait que $\Lim_{X \rightarrow +\infty} \left(  e^X - 5X \right) = +\infty$

Puisque $\Lim_{X \rightarrow +\infty} (5X) = \Lim_{x \rightarrow +\infty} (5\ln(x)) = +\infty$, on peut conclure que :

$\Lim_{x \rightarrow +\infty} ( x - 5\ln(x) ) = +\infty$

Par somme, on obtient :

$\Lim_{x \rightarrow +\infty} (f(x)) = \Lim_{x \rightarrow +\infty} ( x - 5\ln(x) ) + \Lim_{x \rightarrow +\infty} \left(  \dfrac{4}{x} \right) = +\infty$


 3. Pour $x$ strictement positif, la fonction $\ln$ est définie. $f$ est donc également définie.

$f'(x) = 1 - 5 \left( \dfrac{1}{x} \right) + 4 \left( - \dfrac{1}{x^2} \right) = 1 - \dfrac{5}{x} + \dfrac{4}{x^2} = u(x)$

On sait que $u(x) = \dfrac{x^2 - 5x + 4}{x^2}$

###### Racines de $u$
$\Delta = (-5)^2 - 4 \times 1 \times 4 = 9$

$\Delta > 0$, $u$ possède donc 2 racines qu'on appellera $x_1$ et $x_2$ :

$x_1 = \dfrac{5 - \sqrt{9}}{2} = 1$
\hspace{2em}
$x_2 = \dfrac{5 + \sqrt{9}}{2} = 4$

\begin{tikzpicture}
   \tkzTabInit{$x$ / 1 , signe de $x^2$ / 1, signe de $x^2 - 5x + 4$ / 1, signe de $u(x)$ / 1,  variations de $f$ / 2}{$0$, $1$, $4$, $+\infty$}

   \tkzTabLine{z, +, +, +, +, +, +}
   \tkzTabLine{+, +, z, -, z, +, +}
   \tkzTabLine{z, +, z, -, z, +, +}
   \tkzTabVar{ -/, +/, -/, +/ $+\infty$}

\end{tikzpicture}




## Partie C


 1. On sait que cette courbe est la courbe représentative de $u$. On sait également que une primitive se $u$ sur $\mathbb{R}^+_*$ est $f$.

On à donc :

$$\mathcal{A} = \int_4^1 u(x) \text{d}x = \left[ f(x) \right]_4^1 = f(1) - f(4) = \left( 1 - 5\ln(1) - \dfrac{4}{1} \right)  \left( 4 - 4\ln(4) - \dfrac{4}{4} \right) = 5\ln(4) - 6$$

 2. On cherche une valeur de $\lambda$ telle que $\int_4^\lambda u(x) \text{d}x = \mathcal{A}$

$\displaystyle\int_4^\lambda u(x) \text{d}x = \left[ f(x) \right]_1^\lambda = f(\lambda) - f(4) = f(\lambda)  + 3 + 5\ln(4)$

On a donc :

$\displaystyle\int_4^\lambda u(x) \text{d}x = \mathcal{A} \iff f(\lambda) - 3 + 5\ln(4) = \mathcal{A} \iff f(\lambda) = -3$

Puisque $f$ est continue et strictement monotone sur $[4; +\infty]$, et que $\Lim_{x \rightarrow +\infty} f(x) = +\infty$, on peut dire, d'après le corollaire du théorème des valeurs intermédiaires, qu'il existe une unique solution dans $[4; +\infty]$ à $f(\lambda) = -3$.

Il existe donc bien une valeur de $\lambda$ pour laquelle $\mathcal{A}_\lambda = \mathcal{A}$

# Exercice 2


 1. Puisque [UV) et [EF] sont parallèles, et que [KM] appartient à (UVK) et à (SEF), d'après le théorème du toit, on peut affirmer que (KM) est parallèle à (UV) et à (EF)

 2. On sait que (UK) et (NP) sont tous les deux sur le plan (UVK). On sait également que [UK] est sur (SOA) et que [NP] est sur (CGB). Puisque ces deux plans sont parallèles et que [UK] et [NP] sont sur un plan qui leur est sécant, on peut dire que [UK] et [NP] sont parallèles.

 3. a) K est sur [ES]. On commence donc par chercher l'équation paramétrique de (ES).

On cherche à déterminer le vecteur directeur de (ES) :

$\vect{ES}\left( \begin{array}{c}x_S - x_E\\ y_S - y_E\\ z_S - z_E\end{array} \right) = \vect{ES} \left( \begin{array}{c} -4\\ 0\\ 1\end{array} \right)$


(ES) est donc la droite de vecteur directeur $\vect{ES}$ et qui passer par le point S.

$(ES) : \left\{ \begin{array}{lll} x &=& -4t + a\\ y &=& b, \text{ avec } (a, b, c) \in \mathbb{R}\\ z &=& t + c\end{array} \right.$

et avec $(a, b, c)$ tels qu'il existe une valeur de $t$ telle que $(x; y; z) = (0; 0; 3,5)$, soit $(a; b; c) = (0; 0; 3,5)$


$(ES) : \left\{ \begin{array}{lll} x &=& -4t\\ y &=& 0\\ z &=& t + 3,5 \end{array} \right.$

Puisque K est sur (ES), $K(1,2; 0; 3,2) \iff \exists t \in \mathbb{R}, \left\{ \begin{array}{lll}-4t &=& 1,2\\ 0 &=& 0\\ 3,2 &=& t + 3,5 \end{array} \right.$, ce qui est vérifié pour $t = -0,3$. K est donc bien sur (ES).


