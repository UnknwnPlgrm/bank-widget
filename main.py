from Src import directory_info, mask

card_number = input("Введите номер карты: ")
check_number = input("Введите номер счета: ")
recursion = False

print(f"Замаскированнй номер карты: {mask.mask_number_of_card(card_number)}")
print(f"Замаскированный номер счета: {mask.mask_check(check_number)}")

print("Дополнительное задание")

path = input("Введите путь к директории: ")
recursion_input = input("Запустить полное сканирование директории? (True/False): ")

if recursion_input == "True":
    recursion = True
elif recursion_input == "False":
    recursion = False

print(directory_info.get_directory_info(path, recursion))
