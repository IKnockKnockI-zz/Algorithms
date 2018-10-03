def count_characters(string):
    """Возвращает словарь, где в виде ключа выступает символ,
    а в качестве значения количество его повторений в переданной 
    в аргумент строке."""
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)
