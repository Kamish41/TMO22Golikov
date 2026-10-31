#6 вариант

def tasks_per_hour(tasks, hours):
    if hours == 0: return 'На ноль делить нельзя'
    assert (tasks != 18 and hours != 3), "Такой пример уже был"
    assert hours != 0, "На ноль делить нельзя"
    assert hours < 10, "Иди поспи"
    return tasks/hours

print(tasks_per_hour(int(input('Введите количество решенных задач: ')), int(input('Введите количество затраченных часов: '))))

input("Нажмите Enter чтобы продолжить")

words = ["мяч", "ракетка", "велосипед"]

print(sorted(words, key=lambda word: len(word)))