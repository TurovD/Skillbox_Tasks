
math_operations = {
        '+':lambda a, b: a + b,
        '-':lambda a, b: a - b,
        '*':lambda a, b: a * b,
        '/':lambda a, b: a / b,
}

with open('calc.txt') as file_data:
    math_result = 0
    for string in file_data:
        try:
            for i in math_operations:
                if i in string:
                    string = string.split(f' {i} ')
                    math_result += math_operations[i](int(string[0]), int(string[1]))
                    break
        except (SyntaxError, TypeError):
            break
    print('Сумма всех результатов:', math_result)

