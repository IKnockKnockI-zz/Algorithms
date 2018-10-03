def ss(numbers:list, n:int):
    """Проверяет наличие n в списке numbers.
    Возвращает True или False соответственно."""
    found = False
    for i in numbers:
        if i == n:
            found = True
            break
    return found