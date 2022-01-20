with open('zen.txt') as text:
  lines = text.readlines()
  data = ''.join(lines)
  print('Строк: ',len(lines))
  print('Слов: ',len(data.split()))
  data = ''.join(data.split())
  print('Букв: ',len(data))

