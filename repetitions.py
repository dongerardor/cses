""" 
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
Input
The only input line contains a string of n characters.
Output
Print one integer: the length of the longest repetition.
Constraints

1 \le n \le 10^6

Example
Input:
ATTCGGGA

Output:
3

import importlib
modulo = importlib.import_module("_03_repetitions")

modulo.funcion() # llamar una func del modulo

modulo = importlib.reload(modulo)
"""

""" sequence = 'ATTCGGGA' """
""" sequence = 'AAAAABBBDDDDBBBBBBBBBBBEEEEEE' """

sequence = input()
longer_list = []
temp_list = []

for i, ch in enumerate(sequence):
    prev_ch = sequence[i - 1] if i > 0 else ''

    if prev_ch != ch:
        if len(temp_list) > len(longer_list):
            longer_list = temp_list.copy()
        temp_list.clear()
        
    temp_list.append(ch)

else:
    if len(temp_list) > len(longer_list):
        longer_list = temp_list.copy()  

print(len(longer_list))
