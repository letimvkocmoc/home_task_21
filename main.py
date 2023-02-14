from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import CourierError, RequestError


store = Store(items=[])
shop = Shop(items=[])

store.items = {
    'печенька': 25,
    'собачка': 25,
    'елка': 25,
    'пончик': 3,
    'зонт': 5,
    'ноутбук': 1,
}

shop.items = {
     'печенька': 2,
     'собачка': 2,
     'елка': 1,
     'зонт': 1,
     'пончик': 1,
}

storages = {
    'магазин': shop,
    'склад': store
}


def main():
    print('\nДобрый день!\n')

    while True:
        # вывод содержимого складов
        for storage in storages:
            print(f'Сейчас в {storage}:\n {storages[storage].items}')

        # запрашиваем ввод от пользователя
        user_input = input(
            'Введите запрос в формате "Достать 3 печеньки из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )

        if user_input in ('stop', 'стоп'):
            break

        # разбираем ввод пользователя
        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as e:
            print(e.message)
            continue

        # доставляем товар
        courier = Courier(request=request, storages=storages)
        try:
            courier.move()
        except CourierError as e:
            print(e.message)


if __name__ == '__main__':
    main()
