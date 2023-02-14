from typing import Dict
from entity.storage_abstract import AbstractStorage
from exceptions import *


class BaseStorage(AbstractStorage):

    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, amount):
        # проверяем, достаточно ли места
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        # добавляем товар
        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name, amount):
        # проверяем, есть ли такой товар и хватает ли его
        if name not in self.__items or self.__items[name] < amount:
            raise NotEnoughProduct

        # вычитаем необходимое количество товара. если товара станет 0 - удаляем товар из списка
        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self):
        # считаем сумму значений в словаре с товарами, вычитаем ее из вместимости склада
        return self.__capacity - sum(self.__items.values())

    @property
    # геттер
    def items(self):
        return self.__items

    @items.setter
    # сеттер
    def items(self, new_data):
        self.__items = new_data

    def get_unique_items_count(self):
        # получаем количество уникальных товаров
        return len(self.__items)


