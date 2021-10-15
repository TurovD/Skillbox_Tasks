# TODO здесь писать код
containers = (int(input('Кол-во контейнеров: ')))
weight_containers,index = [],1
for _ in range(1,containers+1):
    weight_cont = (int(input('Введите вес контейнера: ')))
    weight_containers.append(weight_cont)
new_containers = int(input('Введите вес нового контейнера: '))
for i in range (len(weight_containers)):
    if int(weight_containers[i])>=new_containers:
        index+=1
print('Номер, куда встанет новый контейнер: ',index)