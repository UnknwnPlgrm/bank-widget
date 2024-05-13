from Src import mask


def mask_multifunction(input_data: str) -> str:
    """Функция принимает на вход необработанную строку с данными счета/карты.
    Возвращает отредактированные данные счета/карты с замаскированным номером"""

    splited_input_data = input_data.split()
    if splited_input_data[0] == "Счет":
        masked_check_number = mask.mask_check(splited_input_data[1])
        masked_check_result = splited_input_data[0] + f" {masked_check_number}"
        return masked_check_result
    else:
        masked_card_number = mask.mask_number_of_card(splited_input_data[-1])
        masked_card_list = []
        for word in splited_input_data:
            if word.isalpha():
                masked_card_list.append(word)
        masked_card_result = " ".join(masked_card_list) + f" {masked_card_number}"
        return masked_card_result


def formatting_data_string(input_data: str) -> str:
    """Функция принимает на вход неотформатированную строку с датой.
    Возвращает строку с датой в формате dd.MM.yyyy"""

    return f"{input_data[8:10]}.{input_data[5:7]}.{input_data[0:4]}"
