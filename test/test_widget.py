import pytest
from Src import widget


@pytest.mark.parametrize("card_or_check_data, masked_card_or_check_data", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("64686473678894779589", "Неверно указаны данные карты/счета"),
    ("1596837868705199", "Неверно указаны данные карты/счета"),
    ("", "Неверно указаны данные карты/счета")
])
def test_mask_multifunction(card_or_check_data, masked_card_or_check_data):
    assert widget.mask_multifunction(card_or_check_data) == masked_card_or_check_data


@pytest.mark.parametrize("input_data, formatted_data", [
    ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ("2018-07-11T02:26:", "Неверно указаны данные операции"),
    ("", "Неверно указаны данные операции"),

])
def test_formatting_data_string(input_data, formatted_data):
    assert widget.formatting_data_string(input_data) == formatted_data