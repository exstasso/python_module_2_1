#Статистика посещений сайта
site = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}
visit = ["user1", "user2", "user3", "user1", "user3", "user4"]
site["Общее количество"] = len(visit)
site["Уникальные посещения"] = len(set(visit))
print("Статистика посещений: ", site)
