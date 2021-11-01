first_class,second_class = list(range(160,177,2)), list(range(162, 181, 3))
two_classes = sorted(first_class+second_class)
print(*two_classes,end='')