def reads(path):
    file = open(path, 'r')
    print("\nСодержимое файла:",path,"\n", file.read())
    file.close()

start = "input.txt"
finish = "output.txt"
line = open("input.txt", "r").read().lower()
file_change = {}
amount = 0
for count in line:
   if ord('a') <= ord(count) <= ord('z'):
       change_number = file_change.get(count, 0)
       file_change[count] = change_number + 1
       amount += 1
lout = [(number, "{:5.3f}".format(file_change[number]/amount)) for number in file_change.keys()]
lout.sort(key = lambda change_number: change_number[0])
lout.sort(key = lambda change_number: change_number[1], reverse = True)
sout = "\n".join([i[0] + " " + i[1] for i in lout])
open("output.txt","w").write(sout)


reads(start)
reads(finish)
