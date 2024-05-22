import pytest
from Src import mask

@pytest.mark.parametrize("card_number, mask_card_number", [
    ("6475867563758697", "6475 86** **** 8697"),
    ("64758e7563h5869z", "Неверно указан номер карты"),
    ("64758675", "Неверно указан номер карты"),
    ("", "Неверно указан номер карты")
])
def test_mask_number_of_card(card_number, mask_card_number):
    assert mask.mask_number_of_card(card_number) == mask_card_number


@pytest.mark.parametrize("check_number, mask_check_number", [
    ("64686473678894779589", "**9589"),
    ("646864736f889a7795b9", "Неверно указан номер счета"),
    ("6468647", "Неверно указан номер счета"),
    ("", "Неверно указан номер счета"),
])
def test_mask_check(check_number, mask_check_number):
    assert mask.mask_check(check_number) == mask_check_number