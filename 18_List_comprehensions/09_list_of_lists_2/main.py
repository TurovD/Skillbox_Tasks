nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

clean_list = [number for nested_list in nice_list for nested_number in nested_list for number in nested_number]

print(clean_list)
