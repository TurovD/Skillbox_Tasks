def сhanging(number):
  start = True
  whole =''
  fraction = ''
  for symbol in number:
    if symbol == '.':
      start = False
    elif start:
      whole += symbol
    else:
      fraction += symbol
  reverse_number = str(revers(whole)) + '.' + str(revers(fraction))
  return reverse_number

def revers(number):
  revers_number = ''
  while int(number) > 0:
      revers_number += str(int(number) % 10)
      number = int(number) // 10
  return(revers_number)

def main_menu():
  first_number = (input("Введите первое число: "))
  second_number = (input("Введите второе число: "))
  print('\nПервое число наоборот: ', сhanging(first_number))
  print('Второе число наоборот: ', сhanging(second_number))
  print('Сумма: ', float(сhanging(first_number)) + float(сhanging(second_number)))

main_menu()


