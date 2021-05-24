import random as rd


def simu_X():
    return rd.randint(-2, 2) + rd.randint(0, 2)

"""
Arbre de probabilité correspondant :
        /  0 --> -2
    -2 |-- 1 --> -1
  /     \  2 --> 0
 /
/       /  0 --> -1
|   -1 |-- 1 --> 0
| /     \  2 --> 1
|/
||       /  0 --> 0
----- 0 |-- 1 --> 1
||       \  2 --> 2
| \
|  \     /  0 --> 1
 \  \ 1 |-- 1 --> 2
  \      \  2 --> 3
   \
    \     /  0 --> 2
     \ 2 |-- 1 --> 3
          \  2 --> 4

On en déduit la table de probabilités de la loi X :

| issue | probabilité |
|-------|-------------|
| -2    | 1/15        |
| -1    | 2/15        |
| 0     | 3/15        |
| 1     | 3/15        |
| 2     | 3/15        |
| 3     | 2/15        |
| 4     | 1/15        |


"""


