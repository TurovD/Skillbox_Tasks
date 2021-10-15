def sort_list(first_list):
    for list in range (len(first_list)-1):
        for compare_number in range(len(first_list)-1-list):
            if first_list[compare_number] > first_list[compare_number+1]:
                first_list[compare_number],first_list[compare_number+1]=first_list[compare_number+1],first_list[compare_number]
    return(first_list)


first_list = [int(i) for i in input('Введите числа для изначального списка через пробел: ').split()]
sort_list(first_list)
print('\nОтсортированный список: ',first_list)