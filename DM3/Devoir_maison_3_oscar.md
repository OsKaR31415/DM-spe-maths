---
title: \huge Devoir Maison de mathématiques
author: Oscar Plaisant
documentclass: scrartcl
header-includes: |
    \usepackage[utf8]{inputenc}
    \usepackage[T1]{fontenc}
    \usepackage[french]{babel}
    
    \usepackage[left=1.2cm, right=1.2cm, top=2cm, bottom=2.5cm]{geometry}
    
    \usepackage{amsmath, amsfonts, amssymb}
    
    \usepackage{lastpage}
    
    \usepackage{xcolor}
    \usepackage{enumitem}
    \usepackage{fancyhdr}
    \usepackage{sectsty}
    \usepackage{graphicx}
    \usepackage{euler}
    
    
    \pagestyle{fancy}
    
    \renewcommand{\headrulewidth}{0pt}
    \fancyhead[L]{}
    \fancyhead[C]{}
    \fancyhead[R]{}
    
    \renewcommand{\footrulewidth}{1pt}
    \fancyfoot[L]{Antonin\;Peronnet,\;Benoit\;Leroux,\;Oscar\;Plaisant}
    \fancyfoot[C]{\thepage/\pageref{LastPage}}
    \fancyfoot[R]{\.\.\text{DM N}$^\circ3$}

    \renewcommand{\frac}[2]{\dfrac{#1}{#2}}

    \sectionfont{\Huge}
    \subsectionfont{\huge}
    \subsubsectionfont{\Large}
    \paragraphfont{\large}
---


# Exercice 1 :

$u_0 = 3$

$u_1 = 6$

$u_{n+2} = \frac{5}{4}u_{n+1} -\frac{1}{4}u_n$

## Partie A

### 1. Donner une formule qui, saisie dans la cellule B4, puis recopiée vers le bas, permet d’obtenir les valeurs de la suite $(u_n)$ dans la colonne B.

La formule est "=(5\*B3/4) + (B2/4)"

### 2. Recopier et compléter le tableau ci-dessus. On donnera des valeurs approchées à 10 - 3 près deun pour $n$ allant de 2 à 5.

\includegraphics[scale=0.5]{images/tableur.png}

### 3. Que peut-on conjecturer à propose de la convergence de la suite $(u_n)$ ?

On peut conjecturer que la suite diverge vers $+\infty$


## Partie B

### 1.
#### a) Démontrer que $(v_n)$ est une suite constante

$$
\begin{array}{rcl}
    v_n = u_{n+1} - \dfrac{1}{4}u_n & \iff & v_{n+1} = u_{n+2} + \frac{1}{4}u_{n+1}\\
        &\iff& v_{n+1} = \left(\dfrac{5}{4}u_{n+1} - \dfrac{1}{4}u_n\right) - \dfrac{1}{4}u_{n+1}\\
        &\iff& v_{n+1} = u_{n+1} - \dfrac{1}{4}u_{n+1}\\
        &\iff& v_{n+1} = v_n
\end{array}
$$
Donc, la suite $(v_n)$ est constante.
#### b) En déduire que, pour tout $n\in\mathbb{N}, u_{n+1} = \dfrac{1}{4}u_n + \dfrac{21}{4}$

On sait que 
$$
\begin{array}{rcl}
    u_{n+1} &=& v_n + \frac{1}{4}u_n\\
            &=& v_0 + \frac{1}{4}u_n\\
            &=& \frac{21}{4} + \frac{1}{4}u_n\\ 
\end{array}
$$

### 2.
#### a) En utilisant le résultat de la question **1.b)**, montrer par récurrence que $\forall n\in\mathbb{N}, u_n\leq u_{n+1}\leq 15$\\

On pose $P$, la proposition : $P_n \iff u_n\leq u_{n+1}\leq 15$


##### Initialisation

$P_0 \iff u_0 \leq u_1 \leq 15 \iff 3 \leq 6\leq 15$

Donc, $P_0$ est vraie.

##### Hérédité


On cherche à montrer que $\forall n\in\mathbb{N}, P_n\implies P_{n+1}$.

$$
\begin{array}{rcl}
    P_n &\iff& u_n \leq u_{n+1}\leq 15\\[2ex]
        &\iff& \frac{1}{4}u_n \leq \frac{1}{4}u_{n+1} \leq \frac{15}{4}\\[2ex]
        &\iff& \frac{1}{4}u_n + \dfrac{21}{4}u_n \leq \frac{1}{4}u_{n+1} + \frac{21}{4} \leq \frac{15}{4} + \frac{21}{4}\\[2ex]
        &\iff& u_{n+1} \leq u_{n+2} \leq 9\\[2ex]
        &\implies& u_{n+1} \leq u_{n+2} \leq 15
\end{array}
$$


On à donc bien $P_n \implies P_{n+1}$



##### Récurrence

puisque $P_0 \wedge \forall n\in\mathbb{N}, P_n\implies P_{n+1}$, on sait que $\forall n\in\mathbb{N}, P_n$
    b) En déduire que la suite $(u_n)$ est une suite convergente.

La suite $(u_n)$ est strictement croissante et majorée par 15, on peut donc dire qu'elle converge.

### 3.
#### a) Démontrer que $(w_n)$ est une suite géométrique dont on précisera le premier terme et la raison

On sait que :

$w_n = u_n - 7$


On peut donc en déduire que :

$w_0=u_0-7=3-7=-4$

Et que :

$$
\begin{array}{rcl}
    w_{n+1} &=& u_{n+1} - 7\\
            &=& \frac{u_n}{4} + \frac{21}{4} - \frac{28}{4}\\
            &=& \frac{u_n - 7}{4}\\
    w_{n+1} &=& \frac{1}{4}w_n
\end{array}
$$

On à donc :


$\left\{\begin{array}{rcl}w_0 &=& -4\\w_{n+1} &=& \frac{1}{4}w_n\end{array}\right.$

On peut donc dire que la suite $(w_n)$ est une suite de premier terme -4 et de raison $\frac{1}{4}$.

#### b) En déduire que $\forall n\in\mathbb{N}, u_n = 7 -\left(\frac{1}{4}\right)^{n-1}$

On sait que $(w_n)$ est la suite géométrique de raison $\frac{1}{4}$ et de premier terme -4. On peut donc dire que $w_n = -4\left(\frac{1}{4}\right)^{n} =-\left(\frac{1}{4}\right)^{n-1}$

On sait également que $w_n = u_n - 7$, soit que $u_n = 7 + w_n$.

On peut donc dire que $w_n = u_n - 7\iff w_n = 7 -\left(\frac{1}{4}\right)^{n-1}$


#### c) calculer la limite de la suite $(u_n)$

On sait que $u_n = 7 - \left(\frac{1}{4}\right)^{n-1}$. On cherche donc à calculer $\lim_{n\rightarrow +\infty}\left(7 - \left(\frac{1}{4}\right)^{n-1}\right)$ :

$$\newcommand{\disp}{\displaystyle}
\begin{array}{rcl}
    \disp\lim_{n\rightarrow +\infty}\left(u_n\right) &=& \disp\lim_{n\rightarrow +\infty}\left(7 - \left(\frac{1}{4}\right)^{n-1}\right)\\[2ex]
        &=& \disp\lim_{n\rightarrow +\infty}(7) - \lim_{n\rightarrow +\infty}\left(\left(\frac{1}{4}\right)^{n - 1}\right)\\[2ex]
        &&\text{Or, }\;\;\frac{1}{4}\in ]-1; 1[\;\;\text{ Donc :}\\[2ex]
        &=& 7 - 0\\
        &=& 7
\end{array}
$$







