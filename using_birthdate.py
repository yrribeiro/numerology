def reduce(value): # @todo IMPORT IT FROM USING_NAME
    if value not in [11, 22, 33]:
        str_val = str(value)
        final_value = 0
        # print(f'\n----- Final sum values = {str_val}')
        for digit in str_val:
            final_value += int(digit)
    else:
        final_value = value
    return final_value

def calculate_single_values(birthdate):
    value = 0
    for digit in birthdate:
        digit = int(digit)
        value += digit

    return value

def calculate_pinnacles(birthdate, life_path):
    day = birthdate[0:2]
    month = birthdate[2:4]
    year = birthdate[4:]

    first_pinn = reduce(calculate_single_values(day) + calculate_single_values(month))
    second_pinn = reduce(calculate_single_values(day) + calculate_single_values(year))
    third_pinn = reduce(first_pinn + second_pinn)
    fourth_pinn = reduce(calculate_single_values(month) + calculate_single_values(year))

    return {'First pinnacle':first_pinn,
            'Second pinnacle':second_pinn,
            'Third pinnacle':third_pinn,
            'Fourth pinnacle':fourth_pinn
            }

def calculate_pinnacle_endings(life_path):
    first = 36 - life_path
    second = 9 + first
    third = 9 + second
    return {'First pinnacle':first,
            'Second pinnacle':second,
            'Third pinnacle':third,
            'Fourth pinnacle':'[until your life ends]'
            }

print('Enter your birthdate: [DDmmYYYY]')
birthdate = input()

life_path = reduce(calculate_single_values(birthdate))
print(f'Life path number: {life_path}')
pinnacles = calculate_pinnacles(birthdate, life_path)
endings = calculate_pinnacle_endings(life_path)
for pinnacle in pinnacles:
    print(f'{pinnacle}: {pinnacles[pinnacle]}')
    print(f'-- {pinnacle} ending: {endings[pinnacle]}')
