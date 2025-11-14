# Skypro HW project
## New functions
**filter_by_state**
Фильтрует список словарей по значению ключа 'state'.
Args:
- dict_list (list[dict]): Список словарей для фильтрации
- state (str): Значение для фильтрации (по умолчанию 'EXECUTED')
Returns:
- list[dict]: Новый список словарей, где state соответствует указанному значению
Examples:
```
        >>> transactions = [
        ...     {'id': 1, 'state': 'EXECUTED', 'amount': 100},
        ...     {'id': 2, 'state': 'PENDING', 'amount': 200},
        ...     {'id': 3, 'state': 'EXECUTED', 'amount': 300}
        ... ]
        >>> filter_by_state(transactions)
        [{'id': 1, 'state': 'EXECUTED', 'amount': 100}, {'id': 3, 'state': 'EXECUTED', 'amount': 300}]
        >>> filter_by_state(transactions, 'PENDING')
        [{'id': 2, 'state': 'PENDING', 'amount': 200}]
```
**sort_by_date**
Сортирует список словарей по дате.
Args:
- transactions (list[dict]): Список словарей с транзакциями
- descending (bool): Порядок сортировки: True - по убыванию, False - по возрастанию
Returns:
- list[dict]: Новый отсортированный список
Examples:
```
        >>> transactions = [
        ...     {'date': '2024-01-15', 'amount': 100},
        ...     {'date': '2024-01-10', 'amount': 200},
        ...     {'date': '2024-01-20', 'amount': 300}
        ... ]
        >>> sort_by_date(transactions)
        [{'date': '2024-01-20', 'amount': 300}, {'date': '2024-01-15', 'amount': 100}, {'date': '2024-01-10', 'amount': 200}]
        >>> sort_by_date(transactions, False)
        [{'date': '2024-01-10', 'amount': 200}, {'date': '2024-01-15', 'amount': 100}, {'date': '2024-01-20', 'amount': 300}]
```