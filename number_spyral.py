"""
A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:

Your task is to find out the number in row y and column x.
Input
The first input line contains an integer t: the number of tests.
After this, there are t lines, each containing integers y and x.
Output
For each test, print the number in row y and column x.
Constraints

1 \le t \le 10^5
1 \le y,x \le 10^9

Example
Input:
3
2 3
1 1
4 2

Output:
8
1
15


//////////////////////////////
1. Encuentro la raiz del numero 
"""

tests = int(input())
coords = []

for i in range(tests):
    coords.append(input())

for coord in coords:
    y, x = map(int, coord.split())

    big = y if y > x else x
    small = x if x != big else y
    output = 0
    if y % 2 == 0:
        output = big ** 2 - small + 1
    else:
        output = ((big - 1) ** 2) + small
    
    print(output)


"""
3
2 3
1 1
4 2


Si el numero mayor es par, (N ** 2) - n + 1
Si el numero mayor es impar, ((N-1) ** 2) + n



formula
1) tomar el numero mayor de la dupla (NM)
El rango es ((NM - 1) ** 2) + 1 <= num <= NM ** 2
Ejemplo: 3 7 (es el 47)
Rango: 
(7 - 1) ** 2 + 1 = 37
7 ** 2 = 49
True: 37 <= 47 <= 49

Ejemplo: 4 8 (es el 53)
Rango: 50 <= 53 <= 64

Ejemplo: 7 4 (es el 40)
Rango: 37 <= 40 <= 49

Ejemplo: 2 4 (es el 11)
Rango: 10 <= 11 <= 16

Encontrar el offset.
7 4 (es el 40)
(7-1)**2 = 36
36 + x = 40

7 7 (es el 43)
(7-1)**2 = 36
36 + x = 43

7 2 (es el 39)

3 7 (es el 47)
Rango: 37 <= 47 <= 49

Hipotesis: para encontrar el offset:
si el y es impar, se suma el x a la base del rango.





//////

5 7 = 45


En todos los casos se calcula el cuadrado del numero mayor menos 1
5 7 = 6 ** 2 = 36 
base 36 entonces

y ES IMPAR
a la base se le suma el numero X. En este caso es 7
36 + 7 = 43

x es impar
se le resta y al cuadrado del numero mayor. En este caso, es 49 - 5. Y se le suma 1.
-----------------


8 5 = 60
6 6 = 31
8 4 = 61

5 3 = 19
7 4 = 40
3 7 = 39

Si el numero mayor es par, (N ** 2) - n + 1
Si el numero mayor es impar, ((N-1) ** 2) + n


"""


