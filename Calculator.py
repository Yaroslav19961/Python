number_1 = input('Number - ')
operator = input('Operator - ')
number_2 = input('Number_2 - ')

n1 = int(number_1)
n2 = int(number_2)

if operator == '+':
    print(n1, '+', n2, '=', n1 + n2)
elif operator == '-':
    print(n1, '-', n2, '=', n1 - n2)
elif operator == '*':
    print(n1, '*', n2, '=', n1 * n2)
elif operator == '/' or operator == ':':
    if n2 != 0:
        print(n1, '/', n2, '=', n1 / n2)
    else:
        print("Division by zero is not allowed")
else:
    print('Not work')
