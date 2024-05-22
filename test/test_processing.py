from Src import processing


def test_filter_of_bank_operation(
    example_list_of_operations: list, ex_passed_list_of_operation: list, can_passed_list_of_operation: list
) -> None:
    assert processing.filter_of_bank_operation(example_list_of_operations, "EXECUTED") == ex_passed_list_of_operation
    assert processing.filter_of_bank_operation(example_list_of_operations, "CANCELED") == can_passed_list_of_operation
    assert processing.filter_of_bank_operation(example_list_of_operations, "executed") == ex_passed_list_of_operation
    assert processing.filter_of_bank_operation(example_list_of_operations, "canceled") == can_passed_list_of_operation
    assert processing.filter_of_bank_operation([], "EXECUTED") == []
    assert processing.filter_of_bank_operation([], "CANCELED") == []


def test_operation_date_sorting(
    example_list_of_operations: list,
    passed_sorting_list_of_operation: list,
    reversed_passed_sorting_list_of_operation: list,
) -> None:
    assert processing.operation_date_sorting(example_list_of_operations, False) == passed_sorting_list_of_operation
    assert (
        processing.operation_date_sorting(example_list_of_operations, True)
        == reversed_passed_sorting_list_of_operation
    )
    assert processing.operation_date_sorting([], True) == []
    assert processing.operation_date_sorting([], False) == []
