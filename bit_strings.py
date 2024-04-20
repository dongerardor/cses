""" 
str_binary = ""
for i in range(input):
    str_binary += "1"

print(str_binary)

print(int(str_binary, 2) + 1) 
"""

print((1 << int(input())) % 1000000007)