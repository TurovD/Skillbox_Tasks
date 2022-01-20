def reads(path):
    file = open(path, 'r')
    print("Содержимое файла:",path,"\n", file.read())
    file.close()


read_file = open("first_tour.txt", "r")
k = int(read_file.readline())
new_list = []
for line in read_file:
    new_line = line.split()
    if new_line != [] and int(new_line[-1]) > k:
        new_list.append(new_line)
read_file.close()
new_list.sort(key=lambda a: int(a[-1]))
new_list.reverse()
count = str(len(new_list))
out_lst = []
n = 1
for i in new_list:
    name_sim = str(i[1][0]) + '.'
    s_win = str(n) + ') ' + name_sim + ' ' + i[0] + ' ' + i[-1]
    out_lst.append(s_win)
    n += 1
with open("second_tour.txt", "w") as f_out:
    f_out.write(count + '\n')
    s = '\n'.join(out_lst)
    f_out.write(s)
fer = "first_tour.txt"
reads(fer)
sec = "second_tour.txt"
print('\n')
reads(sec)