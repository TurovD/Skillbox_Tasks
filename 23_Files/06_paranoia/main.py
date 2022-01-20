
def ceasar_encode(letter, shift):
    if letter.isalpha():
        number = ord(letter) + shift
        return chr(number)
    return letter

def reads(path):
    file = open(path, 'r')
    print("Содержимое файла:",path,"\n", file.read())
    file.close()

file_start,file_finish = 'text.txt',"output.txt"
reads(file_start)
files = open(file_finish, 'w')
shift_letter = 0
with open('text.txt') as text:
    for line in text:
        if shift_letter == 26:
            shift_letter = 0
        else:
            shift_letter += 1
        for letters in line:
            files.write(ceasar_encode(letters, shift_letter))
    files.close()
reads(file_finish)