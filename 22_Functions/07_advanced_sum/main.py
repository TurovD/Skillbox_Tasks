def summ(*args):
    def flatten(a_list):
        result = []
        for element in a_list:
            if isinstance(element,int):
                result.append(element)
            else:
                result.extend(flatten(element))
        return result
    return sum(flatten(args))

print('sum([[1, 2, [3]], [1], 3])')
print('Ответ: ', summ([[1, 2, [3]], [1], 3]))

print('\nsum(1, 2, 3, 4, 5)')
print('Ответ: ', summ(1,2,3,4,5))

