
def pedigree(relative):
    if relative not in pedigree_tree:
        return 0
    else:
        return 1 + pedigree(pedigree_tree[relative])
pedigree_tree = {}
number_relatives = int(input('Введите количество человек: '))
for i in range(number_relatives - 1):
    child, parent = input('{} пара: '.format(i+1)).split()
    pedigree_tree[child] = parent
heights_relatives = {}
for relative in set(pedigree_tree.keys()).union(set(pedigree_tree.values())):
    heights_relatives[relative] = pedigree(relative)
print('\n"Высота” каждого члена семьи: ')
for relatives, count in sorted(heights_relatives.items()):
    print(relatives, ':', count)