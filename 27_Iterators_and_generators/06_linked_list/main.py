class LinkedList:
    class __Unit:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self, *args):
        length = len(args)
        self.__length = length
        self.__head = self.__Unit(args[0]) if length > 0 else None
        self.__tail = self.__head
        for i in range(1, length):
            self.__tail.next = self.__Unit(args[i])
            self.__tail = self.__tail.next

    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current.value
            current = current.next

    def __str__(self):
        return f"[{' '.join(str(i) for i in self)}]"

    def __len__(self):
        return self.__length

    def __index_check(self, index):
        if not 0 <= index < self.__length:
            raise IndexError

    def append(self, value):
        if self.__length > 0:
            self.__tail.next = self.__Unit(value)
            self.__tail = self.__tail.next
        else:
            self.__head = self.__tail = self.__Unit(value)
        self.__length += 1

    def get(self, index):
        self.__index_check(index)
        current = self.__head
        for _ in range(index):
            current = current.next
        return current.value

    def remove(self, index):
        self.__index_check(index)
        if self.__length == 1:
            self.__head = self.__tail = None
        elif index == 0:
            self.__head = self.__head.next
        else:
            current = self.__head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
            if index == self.__length - 1:
                self.__tail = current
        self.__length -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)