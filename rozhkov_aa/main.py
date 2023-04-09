import sys


# noinspection PyUnreachableCode
def main(args: list[str]):
    length_of_substring = 200
    file_name: str
    min_args = 3

    if len(args) < min_args:
        print(f"Not enough {len(args)=} required >= 3")
        return -1

    for bottom in range(len(args)):
        match args[bottom]:
            case '-f':
                file_name = args[bottom + 1]
            case '-n':
                try:
                    length_of_substring = int(args[bottom + 1])
                except AttributeError:
                    print("Error: invalid -n argument")
                    return 201

    if not file_name.endswith(".txt"):
        print("invalid file type require .txt file")
        return 505

    whole_file_str: str = read_file(file_name)

    if len(whole_file_str) == 0:
        print("Error: Empty file")

    split_strings(length_of_substring, whole_file_str)

    # разделение на подстроки и вывод (сделал как на си, т.к. пока не шарю за большинство фичей питона)

    return 0


# чтение файла


def read_file(file_name: str):
    try:
        with open(file_name, 'rt', encoding='utf-8') as file:
            return file.read()
    except SystemExit:
        print("file was not found")
        sys.exit(-1)


def print_substring(all_str: str, a: int, b: int, c: int) -> None:
    substring = all_str[a:b + 1]
    print("Substring #", c, ":")
    print(f"{substring}")


def split_strings(length_of_substring: int, all_str: str, ) -> None:
    size_of_file: int = len(all_str)
    count = 1
    bottom = 0
    string_print = False
    top_border: int = length_of_substring

    while bottom < size_of_file - 1:
        if top_border > size_of_file:
            top_border = size_of_file - 1
            string_print = True
        # проверяем не дошли ли мы до конца строки
        if not top_border == size_of_file - 1:
            temp = top_border - 1
            # проверяем куда попали
            if not all_str[top_border] == ' ' or all_str[top_border] == '\n':
                while not all_str[top_border] == ' ' and not all_str[top_border] == '\n':
                    top_border -= 1
                    if top_border == bottom:
                        break
                if top_border == bottom:
                    print("Error: parameter n < length of a part of the string in file")
                    break
                # проверяем, не находимся ли мы внутри индекса пользователя
                while not all_str[temp] == ' ':
                    temp -= 1
                    if temp == 0:
                        break
                if all_str[temp + 1] == '@':
                    top_border = temp
                    string_print = True
                else:
                    string_print = True
            else:
                # тоже проверка на индекс
                while not all_str[temp] == ' ':
                    temp -= 1
                if all_str[temp + 1] == '@':
                    top_border = temp
                    string_print = True
                else:
                    string_print = True
        # Вывод и смена границ подстроки
        if string_print:
            print_substring(all_str, bottom, top_border, count)
            bottom = top_border + 1
            top_border = top_border + length_of_substring
            count += 1
            string_print = False
        else:
            pass


if __name__ == '__main__':
    sys.exit(main(sys.argv))
