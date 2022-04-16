def reduce(value):
    if value not in [11, 22, 33]:
        str_val = str(value)
        final_value = 0
        print(f'\n----- Final sum values = {str_val}')
        for digit in str_val:
            final_value += int(digit)
    return final_value

alpha = ['a', 'b', 'c','d',"e", 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vowels_alpha = ['a','e','i','o','u','y']

print('Insert your name:')
name = input()
value = 0
vowels = 0
for letter in name:
    letter = letter.lower()
    if letter != ' ':
        indv = (alpha.index(letter)+1)%9
        if not indv:
            indv = 9
        value += indv
        if letter in vowels_alpha:
            vowels += indv
            # print(f'---------------- {indv}')
        # print(f'LETTER {letter} -> {indv}')
print(f'Name [{name.upper()}] holds value = {reduce(value)}')
print(f'SOULS URGE NUMBER: {reduce(vowels)}')
