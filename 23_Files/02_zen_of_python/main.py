with open('zen.txt') as zen:
    for revers_text in reversed(zen.readlines()):
        print(revers_text, end="")