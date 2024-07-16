my_dict = {
    'Alice': 1990,
    'Bob': 1985,
    'Charlie': 1992
}
print("Словарь my_dict:", my_dict)
print("Год рождения Alice:", my_dict.get('Alice'))
print("Год рождения Eve:", my_dict.get('Eve', 'Ключ не найден'))
my_dict['David'] = 1988
my_dict['Eve'] = 1995
print("Обновленный словарь my_dict:", my_dict)
removed_value = my_dict.pop('Bob', 'Ключ не найден')
print("Удаленное значение:", removed_value)
print("Словарь my_dict после удаления:", my_dict)
my_set = {1, 'строка', 3.14, True, 'строка', 1}
print("Множество my_set:", my_set)
my_set.add('новый элемент')
my_set.add(42)
print("Множество my_set после добавления элементов:", my_set)
my_set.remove(3.14)
print("Множество my_set после удаления элемента:", my_set)