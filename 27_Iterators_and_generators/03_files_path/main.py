# TODO здесь писать код
import os
from _collections_abc import Iterable


def gen_files_path(link: str, search: str) -> Iterable[str]:
    for link, dirs, files in list(os.walk(link)):
        for file in files:
            yield link + '\\' + file
            if link.split('\\')[-1] == search:
                return


gen_squad = gen_files_path(input('Введите название папки: '),input('Введите путь: '))
for i_value in gen_squad:
    print(i_value, end = ' ')
