import string

string1 = "Hello, my name is Joe. I love long walks in the park and staring at stars at night."
count_upper = 0
count_lower = 0
white_space = 0

for char in string1:
    if char in string1:
        if char.isupper():
            count_upper = count_upper + 1 
        if char.islower():
            count_lower = count_lower + 1 
        if char.isspace():
            white_space = white_space + 1

print('Number of upper case: ', count_upper, '\nNumber of lower case: ', count_lower, 
    '\nNumber of whitespace: ', white_space)
