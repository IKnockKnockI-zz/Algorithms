def anagram(word_1, word_2):
    """Выполняет проверку являются ли слова
    анаграммами друг друга. Возвращает True
    или False."""
    word_1 = word_1.lower()
    word_2 = word_2.lower()
    return sorted(word_1) == sorted(word_2)