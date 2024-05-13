import os


def get_directory_info(directory_path: str, recursion: bool = False) -> dict:
    """Принимает на вход адрес директории и значение параметра рекурсии.
    Возвращает словарь с количеством папок и файлов"""

    directory_info = {}
    files_counter = 0
    dir_counter = 0
    files_list = []
    dir_list = []
    if os.path.isdir(directory_path) is not True:
        temporary_path = os.getcwd()
        directory_path = os.path.join(temporary_path, "Src")
    print(directory_path)
    if recursion is False:
        with os.scandir(directory_path) as scan:
            for entry in scan:
                if entry.is_file():
                    files_counter += 1
                elif entry.is_dir():
                    dir_counter += 1
        directory_info["files"] = files_counter
        directory_info["folders"] = dir_counter
        return directory_info
    elif recursion:
        for root, dirs, files in os.walk(directory_path):
            files_list.extend(files)
            dir_list.extend(dirs)
        directory_info["files"] = len(files_list)
        directory_info["folders"] = len(dir_list)
        return directory_info
