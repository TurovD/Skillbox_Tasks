nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]




def deploy(nice_list):
    if nice_list == []:
        return nice_list
    if isinstance(nice_list[0], list):
        return(deploy(nice_list[0]) + deploy(nice_list[1:]))
    return(nice_list[:1] + deploy(nice_list[1:]))



print('Ответ: ', deploy(nice_list))