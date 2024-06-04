import pytest

from Src import generators


@pytest.mark.parametrize(
    "valuta, expect, id_of_operation",
    [
        ("USD", 939719570, 0),
        ("USD", 142264268, 1),
        ("USD", 895315941, 3),
        ("USD", "Банковские операции более не найдены", 7),
        ("RUB", 873106923, 2),
        ("RUB", 594226727, 4),
        ("RUB", "Банковские операции более не найдены", 7),
    ],
)
def test_generator_of_filtered_bank_operation(
    bank_operation_example_list: list, valuta: str, expect: int, id_of_operation: int
) -> None:
    generator = generators.generator_of_filtered_bank_operation(bank_operation_example_list[id_of_operation:], valuta)
    if next(generator) == dict:
        assert next(generator)["id"] == expect
    elif next(generator) == str:
        assert next(generator) == expect


def test_generator_of_description_of_operation(
    bank_operation_example_list: list, list_of_renamed_exceptions: list, description_example_list: list
) -> None:
    generator_description = generators.generator_of_description_of_operation(bank_operation_example_list)
    assert next(generator_description) == description_example_list[0]
    assert next(generator_description) == description_example_list[1]
    assert next(generator_description) == description_example_list[1]
    assert next(generator_description) == description_example_list[2]
    assert next(generator_description) == description_example_list[0]
    assert next(generator_description) == list_of_renamed_exceptions[0]


def test_generator_card_number(list_of_renamed_exceptions: list) -> None:
    generator_card_number = generators.generator_card_number(1, 5)
    generator_card_number_two = generators.generator_card_number(99, 94)
    generator_card_number_three = generators.generator_card_number(9999999999999999, 99999999999999992)
    generator_card_number_four = generators.generator_card_number(0, 0)
    assert next(generator_card_number) == "0000 0000 0000 0001"
    assert next(generator_card_number) == "0000 0000 0000 0002"
    assert next(generator_card_number) == "0000 0000 0000 0003"
    assert next(generator_card_number) == "0000 0000 0000 0004"
    assert next(generator_card_number) == list_of_renamed_exceptions[1]
    assert next(generator_card_number_two) == list_of_renamed_exceptions[2]
    assert next(generator_card_number_three) == list_of_renamed_exceptions[2]
    assert next(generator_card_number_four) == list_of_renamed_exceptions[2]
