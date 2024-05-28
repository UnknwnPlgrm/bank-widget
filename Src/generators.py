from collections.abc import Generator


def generator_of_filtered_bank_operation(operation_list: list, currency: str) -> Generator[dict, str, None]:
    """Функция-генератор принимает на вход список банковских операций и тип валюты для сортировки.
    Возвращает, по вызову, отфильтрованную по типу валюты, банковскую операцию"""

    for operation in operation_list:
        if operation["operationAmount"]["currency"]["code"] == currency:
            yield operation
    while True:
        yield "Банковские операции более не найдены"


def generator_of_description_of_operation(operation_list: list) -> Generator[str, int, None]:
    """Функция-генератор принимает на вход список банковских операций.
    Возвращает, по вызову, описание банковской операции"""

    for operation in operation_list:
        yield operation["description"]
    while True:
        yield "Банковские операции более не найдены"


def generator_card_number(start: int, stop: int) -> Generator[str, int, None]:
    """Функция-генератор принимает на вход диапазон чисел для генерации номера карты.
    Возвращает, по вызову, сгенерированный номер карты по заданному диапазону"""
    if start < stop < 10000000000000000 and stop != 0:
        for x in range(start, stop):
            quantity_of_numbers_add = 16 - len(str(x))
            unformated_card_number = ("0" * quantity_of_numbers_add) + str(x)
            card_number = (
                unformated_card_number[0:4]
                + " "
                + unformated_card_number[4:8]
                + " "
                + unformated_card_number[8:12]
                + " "
                + unformated_card_number[12:16]
            )
            yield card_number
        while True:
            yield "Генерация вышла за пределы заданного диапазона"
    yield "Неверно указан диапазон"
