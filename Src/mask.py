def mask_number_of_card(card_number: str) -> str | None:
    """Принимает на вход номер карты. Возвращает отредактированный, замаскированный номер карты."""

    splited_card_number_list = []
    if len(card_number) == 16 and card_number.isdigit() is True:
        splited_card_number_list.append(card_number[0:4])
        splited_card_number_list.append(card_number[4:8])
        splited_card_number_list.append(card_number[8:12])
        splited_card_number_list.append(card_number[12:16])
        splited_card_number = " ".join(splited_card_number_list)
        masked_splited_card_number = splited_card_number[0:7] + "** ****" + splited_card_number[-5:]
    else:
        return "Неверно указан номер карты"
    return masked_splited_card_number


def mask_check(check_number: str) -> str:
    """Принимает на вход номер счета. Возвращает замаскированный номер счета."""
    if check_number.isdigit() is False:
        return "Неверно указан номер счет"
    return "**" + check_number[-4:]
