def pallindrome(word):
    """Выполняет проверку является ли слово паллидромом.
    Возвращает True или False."""
    word = word.lower()
    return word[::-1] == word