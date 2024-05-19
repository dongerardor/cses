""" 

Given a string, your task is to reorder its letters 
in such a way that it becomes a palindrome 
(i.e., it reads the same forwards and backwards).

Input
The only input line has a string of length n 
consisting of characters A–Z.

Output
Print a palindrome consisting of the characters 
of the original string. You may print any valid solution. 
If there are no solutions, print "NO SOLUTION".

Constraints
1 <= n <= 10^6

Example
Input: AAAACACBA
Output: AACABACAA


    
    # si ha sido encontrada una segunda ocurrencia
    # de una letra anteriormente presente
    # incorporamos ese par a nuestro palindromo
    # una letra en la primera mitad de la palabra
    # y otra en la segunda, espejando la primera

"""

# input = 'AAAACACBAFFFF'
input = input()
palindrome = "NO SOLUTION"
half_word_list = []
temp = {}

def get_loose_letters(temp):
    loose_letters = []
    for letter, val in temp.items():
        if val == True:
            loose_letters.append(letter)
    return loose_letters

""" 
    En qué circunstancias hay la cantidad de letras correcta?
    
    Si luego de la distribucion, encontramos que:
    -"temp" tiene 0 letras excedentes 
    -input tiene una cantidad par de letras
    
    o
    
    -"temp" tiene 1 letra excedente
    -input tiene una cantidad impar de letras
"""
def check_too_many_letters(input, temp):
    loose_letters = get_loose_letters(temp)
    loose_letters_count = len(loose_letters)
    is_input_odd = len(input) % 2 == 1

    if is_input_odd and loose_letters_count == 1:
        return False
    
    if loose_letters_count == 0:
        return False
    
    return True


for letter in input:
    if not letter in temp:
        temp[letter] = False

    if temp[letter]:
        half_word_list.append(letter)
    
    temp[letter] = not temp[letter]


loose_letters = get_loose_letters(temp)
is_input_odd = len(input) % 2 == 1
pivot_char = loose_letters[0] if len(loose_letters) == 1 and is_input_odd else ""
too_many_letters = check_too_many_letters(input, temp)

if not too_many_letters:
    palindrome = "".join(half_word_list) + pivot_char + "".join(half_word_list[::-1])
 
print(palindrome)
