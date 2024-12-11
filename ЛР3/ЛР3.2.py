def find_common_participants(group1, group2, delimiter=","):
    # Разделяем строки участников по указанному разделителю
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Находим пересечение двух множеств
    common_participants = participants1 & participants2

    # Возвращаем отсортированный список
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group)
print(result)
