---
title: Devoir Maison n°6
author: Oscar Plaisant
date:
header-includes: |
    \usepackage[top=2cm, bottom=2.5cm, left=2cm, right=2cm]{geometry}
---

# Exercice 81 p 235

## 1.

$(E_1) : y' = \dfrac{y}{4}$

### a.

$(E_1)$ est une équation du type $y' = ay$, avec $a$ un réel, donc les solutions de $(E_1)$ sont de la forme $f(x) = C e^{ax}$, avec $C$ une constante réelle, soit, dans le cas de $(E_1)$ :

$$f(x) = Ce^{\frac{x}{4}}$$, avec $C$ une constante réelle.

On cherche donc une valeur de $C$ pour laquelle $f(0) = 0,5$, soit :

$$
\begin{array}{rcl}
f(0)= 0,5 &\iff& Ce^{\frac{0}{4}} = 0,5\\
&\iff& C = \dfrac{0,5}{e^0}\\
&\iff& C = 0,4
\end{array}
$$

on a donc : $f(x) = \dfrac{1}{2}e^{\frac{x}{4}}$

### b.

La fonction $x\longmapsto \dfrac{x}{4}$ est strictement croissante sur $\mathbb{R}$, et la fonction exponentielle est également strictement croissante sur $\mathbb{R}$. La fonction $x\longmapsto e^{\frac{x}{4}}$ est donc aussi strictement croissante sur $\mathbb{R}$.


On sait que $\lim_{t\longmapsto +\infty}\left( \dfrac{t}{4} \right) = +\infty$. On sait aussi que $\lim_{t\longmapsto +\infty}\left( e^t \right) = +\infty$

Donc, on a : $\lim_{t\longmapsto +\infty}\left( e^{\frac{t}{4}} \right) = +\infty$

On en déduit que $\lim_{t\longmapsto +\infty}\left( \dfrac{1}{2} e^{\frac{t}{4}} \right) = +\infty$, soit que :

$$\lim_{t\longmapsto +\infty} \left( f(t) \right) = +\infty$$

### c.

On cherche la plus petite valeur de $t$ telle que $f(t) > 3$.

$$
\begin{array}{rcl}
f(t) > 3 &\iff& \dfrac{1}{2}e^{\frac{t}{4}} > 3\\
&\iff& e^{\frac{t}{4}} > 6, \text{ et, puisque } e^{\frac{t}{4}} \text{ et } 6 > 0 :\\
&\iff& \frac{t}{4} > \ln{6}\\
&\iff& t > 4\ln{6}\\
\end{array}
$$

la population dépasse donc les 300 individus après $4\ln{6}$ jours, soit environ 7 ans et 61 jours.

## 2.

$(E): y' = \dfrac{y}{4} - \dfrac{y^2}{12}$, $g$ est solution de $(E)$, et on a : $g(0) = 20$


### a.

$(E'): y' = -\dfrac{1}{4}y + \dfrac{1}{12}y^2$,

$\forall t\in \mathbb{R}^+, g(t) > 0$

$h$ est définie sur $\mathbb{R}^+$ par $h=\dfrac{1}{g}$

$g$ est solution de $(E)$ si et seulement si $g' = \dfrac{g}{4} - \dfrac{g^2}{12}$

Puisque $h = \dfrac{1}{g}$ et que $g$ est strictement positive sur $\mathbb{R}^+$, $h$ est dérivable sur $\mathbb{R}^+$, et on sait que $h' = +\dfrac{g'}{g^2}$.

Si $g$ est solution de $(E)$, alors on a $g' = \dfrac{1}{4}g - \dfrac{1}{12}g^2$. Puisque $h = \dfrac{1}{g}$ et que $g$ est strictement positive sur $\mathbb{R}^+$, on a (toujours sur $\mathbb{R}^+$) :

$\begin{array}{rcl}
h' &=& \dfrac{-g'}{g^2}\\[4ex]
&=& \dfrac{-\left( \dfrac{1}{4}g - \dfrac{1}{12}g^2 \right)}{g^2}\\[4ex]
&=& \dfrac{-\dfrac{1}{4}g + \dfrac{1}{12}g^2}{g^2}\\[4ex]
&=& \dfrac{-\dfrac{1}{4} + \dfrac{1}{12}g}{g}\\[4ex]
&=& -\dfrac{1}{4}\cdot\dfrac{1}{g} + \dfrac{1}{12}\\[4ex]
&=& -\dfrac{1}{4}\cdot h + \dfrac{1}{12}\\[4ex]
\end{array}$

Ce qui équivaut a dire que $h$ est solution de $(E')$.

On a donc bien une équivalance : $h$ est solution de ()


### b.

L'equation $(E')$ est de la forme $y' = ay + b$, on sait donc que ses solutions sont de la forme $x\longmapsto Ce^{ax} - \dfrac{b}{a}$ avec $C$ une constante réelle, soit, dans le cas de $h$, $x\longmapsto Ce^{-\frac{1}{4}x} - \dfrac{1}{12}\cdot\dfrac{4}{1}$
nd{array}
OAOAOAOAOAOBOBOBOBOBOBOAOBOBOAOAkjkjkjkjkjkjkjkjkjOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOBOAOAOAOAOAOAOAOAOAOAOAOAOAOAOAOAOAOAOBOBOBOBOBOAOAOAkjjjkjjji[[[]]]
On cherche donc la valeur de $C$ telle que $h = \left( x \longmapsto Ce^{-\dfrac{1}{4}x} - \dfrac{4}{12} \right)$. Or, on sait que $h = \dfrac{1}{g}$. On sait également que $g(0) = 20$, on a donc $h(0) = \dfrac{1}{20}$, et on cherche $C$ tel que $Ce^{-\dfrac{1}{4}\cdot 0} - \dfrac{4}{12} = \dfrac{1}{20}$ :

$\begin{array}{rcl}
Ce^{-\dfrac{1}{4}\cdot 0} - \dfrac{4}{12} = \dfrac{1}{20} &\iff& Ce^{0} = \dfrac{1}{20} + \dfrac{4}{12}\\[4ex]
&\iff& C = \dfrac{23}{60}\\
\end{array}$


--------------------------------------------------------------------------------


# Exercice 70 p 233

$(E): y' + y^2 = 4$, avec $y(0) = 0$

Avec la méthode d'Euler, pour $h$ proche de 0, on obtient l'approximation suivante :

$$y(x_n + h) \approx f(x_n) + hf'(x_n)$$

soit

$$y(x_n + h) \approx f(x_n) + h\left( 4 - (y(x_n))^2 \right)$$


Plutôt qu'un tableur, on peut utiliser un outil adapté aux mathématiques : un langage de programmation (ici, de paradigme descriptif, donc très proche de la notation mathématique) :

On commence par régler le "pas" du calcul : $h$, soit : 

```apl
      h ← 0.1
```

Ensuite, on définit une fonction qui, a partir de l'approximation de $y(x_n)$ renvoie l'approximation de $y(x_{n+1})$ en utilisant la méthode d'Euler. On appelle cette fonction `nextStep` :

```apl
      nextStep ← {⍵+h×(4-⍵*2)}
```

On définit également une fonction qui, a partir d'un nombre (son argument, `⍵`), renvoie les valeurs de l'approximation de 1 jusqu'a ce nombre :

```apl
      list ← {(nextStep⍣⍵)0}¨⍳
```

Finalement, on définit une dernière fonction qui affiche un graphique a partir d'une liste de nombres. On définit d'abord une variable

\tiny
```apl
      h ← 0.1
      nextStep ← {⍵+h×(4-⍵*2)}
      list ← {(nextStep⍣⍵)0}¨⍳
      graphStep ← 0.05
      plot ← ⍪{⍵≤0:'⋄' ⋄ '—',∇⍵-graphStep}¨

      ⍪list 20
0.4
0.784
1.1225344
1.396526052
1.601497551
1.74501811
1.84050929
1.901761845
1.940092034
1.963696324
1.978085999
1.986803577
1.992064732
1.995232542
1.997137252
1.998281532
1.998968624
1.999381068
1.999628602
1.999777148
      plot list 20
 —————————⋄
 ————————————————⋄
 ———————————————————————⋄
 ————————————————————————————⋄
 —————————————————————————————————⋄
 ———————————————————————————————————⋄
 —————————————————————————————————————⋄
 ———————————————————————————————————————⋄
 ———————————————————————————————————————⋄
 ————————————————————————————————————————⋄
 ————————————————————————————————————————⋄
 ————————————————————————————————————————⋄
 ————————————————————————————————————————⋄
 ————————————————————————————————————————⋄
 ————————————————————————————————————————⋄
 ————————————————————————————————————————⋄
 ————————————————————————————————————————⋄
 ————————————————————————————————————————⋄
 ————————————————————————————————————————⋄
 ————————————————————————————————————————⋄
 ————————————————————————————————————————⋄
```

