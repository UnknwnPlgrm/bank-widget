from Src import generators


def test_generator_of_filtered_bank_operation(bank_operation_example_list: list) -> None:
    generator_USD = generators.generator_of_filtered_bank_operation(bank_operation_example_list, "USD")
    generator_RUB = generators.generator_of_filtered_bank_operation(bank_operation_example_list, "RUB")
    assert next(generator_USD)["id"] == 939719570
    assert next(generator_USD)["id"] == 142264268
    assert next(generator_USD)["id"] == 895315941
    assert next(generator_USD) == "Банковские операции более не найдены"
    assert next(generator_RUB)["id"] == 873106923
    assert next(generator_RUB)["id"] == 594226727
    assert next(generator_RUB) == "Банковские операции более не найдены"


def test_generator_of_description_of_operation(bank_operation_example_list: list) -> None:
    generator_description = generators.generator_of_description_of_operation(bank_operation_example_list)
    assert next(generator_description) == "Перевод организации"
    assert next(generator_description) == "Перевод со счета на счет"
    assert next(generator_description) == "Перевод со счета на счет"
    assert next(generator_description) == "Перевод с карты на карту"
    assert next(generator_description) == "Перевод организации"
    assert next(generator_description) == "Банковские операции более не найдены"


def test_generator_card_number() -> None:
    generator_card_number = generators.generator_card_number(1, 5)
    generator_card_number_two = generators.generator_card_number(99, 94)
    generator_card_number_three = generators.generator_card_number(9999999999999999, 99999999999999992)
    generator_card_number_four = generators.generator_card_number(0, 0)
    assert next(generator_card_number) == "0000 0000 0000 0001"
    assert next(generator_card_number) == "0000 0000 0000 0002"
    assert next(generator_card_number) == "0000 0000 0000 0003"
    assert next(generator_card_number) == "0000 0000 0000 0004"
    assert next(generator_card_number) == "Генерация вышла за пределы заданного диапазона"
    assert next(generator_card_number_two) == "Неверно указан диапазон"
    assert next(generator_card_number_three) == "Неверно указан диапазон"
    assert next(generator_card_number_four) == "Неверно указан диапазон"
