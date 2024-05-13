from Src import widget

card_or_check_data = input("Введите данные счета/карты: ")
unformated_operation_data = input("Введите дату проведенной операции: ")

print(widget.mask_multifunction(card_or_check_data))
print(widget.formatting_data_string(unformated_operation_data))
