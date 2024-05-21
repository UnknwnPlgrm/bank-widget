def filter_of_bank_operation(operation_list: list, operation_status: str = "EXECUTED") -> list:
    """Функция принимает на вход список банковских операций и параметр успешности операции.
    Возвращает отсортированный список операций по критерию успешности проведения операции"""

    filtered_operation_list = []
    for dict in operation_list:
        if dict["state"] == operation_status.upper():
            filtered_operation_list.append(dict)
    return filtered_operation_list


def operation_date_sorting(operation_list: list, reverse_parameter: bool = True) -> list:
    """Функция принимает на вход список банковских операций и параметр порядка сортировки.
    Возвращает отсортированный список операций по дате проведения"""

    return sorted(operation_list, key=lambda words: words["date"], reverse=reverse_parameter)
