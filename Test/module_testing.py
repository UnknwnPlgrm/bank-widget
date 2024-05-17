from Src import processing

example_list_of_operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
filtering_parameter = "Canceled"
is_reverse = True

print(processing.filter_of_bank_operation(example_list_of_operations, filtering_parameter))
print(processing.operation_date_sorting(example_list_of_operations, is_reverse))
