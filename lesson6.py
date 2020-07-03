class Animal:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        return ('Кормить')


"""Дочерние классы, с присущеми их действиям"""


class Bird(Animal):
    def eggs(self):
        return ('яйца')


"""Унаследование к классу Birds"""


class Goose(Bird):
    nickname = 'гусь'
    sound = 'га-га-га'


class Chicken(Bird):
    nickname = 'кура'
    sound = 'ко-ко-ко'


class Duck(Bird):
    nickname = 'утка'
    sound = 'кря-кря'


class Cattle(Animal):
    def milk(self):
        return ('молоко')


"""Унаследование к классу Cattle"""


class Caw(Cattle):
    nickname = 'корова'
    sound = 'му-му'


class Coat(Cattle):
    nickname = 'коза'
    sound = 'ме-ме'


class Sheep(Animal):
    nickname = 'овца'
    sound = 'бе-бе'

    def wool(self):
        return ('стричь')


"""Объекты"""
all_weight_1 = []
all_weight_2 = {}

"""Для каждого животного экземпляр класса"""

goose_gray = Goose('серый', 6)
print(
    f'{goose_gray.nickname} {goose_gray.name}, издает звук: {goose_gray.sound}, весит {goose_gray.weight} кг. Соберем {goose_gray.eggs()} и надо его по {goose_gray.eat()}')
all_weight_1.append(goose_gray.weight)
all_weight_2[goose_gray.name] = goose_gray.weight
print()

goose_white = Goose('белый', 7)
print(
    f'{goose_white.nickname} {goose_white.name}, издает звук: {goose_white.sound}, весит {goose_white.weight} кг. Собирем {goose_white.eggs()} и надо его по {goose_white.eat()}')
all_weight_1.append(goose_white.weight)
all_weight_2[goose_white.name] = goose_white.weight
print()

chicken_1 = Chicken('КО-КО', 3)
print(
    f'{chicken_1.nickname} {chicken_1.name}, издает звук: {chicken_1.sound}, весит {chicken_1.weight} кг. Собирем {chicken_1.eggs()} и надо ее по {chicken_1.eat()}')
all_weight_1.append(chicken_1.weight)
all_weight_2[chicken_1.name] = chicken_1.weight
print()

chicken_2 = Chicken('Кукареку', 5)
print(
    f'{chicken_2.nickname} {chicken_2.name}, издает звук: {chicken_2.sound}, весит {chicken_2.weight} кг. Собирем {chicken_2.eggs()} и надо ее по {chicken_2.eat()}')
all_weight_1.append(chicken_2.weight)
all_weight_2[chicken_2.name] = chicken_2.weight
print()

duck = Duck('Кряква', 5)
print(
    f'{duck.nickname} {duck.name}, издает звук: {duck.sound}, весит {duck.weight} кг. Собирем {duck.eggs()} и надо ее по {duck.eat()}')
all_weight_1.append(duck.weight)
all_weight_2[duck.name] = duck.weight
print()

сow = Caw('Манька', 160)
print(
    f'{сow.nickname} {сow.name}, издает звук: {сow.sound}, весит {сow.weight} кг. Подоить {сow.milk()} и надо ее по {сow.eat()}')
all_weight_1.append(сow.weight)
all_weight_2[сow.name] = сow.weight
print()

goat = Coat('Рога', 65)
print(
    f'{goat.nickname} {goat.name}, издает звук: {goat.sound}, весит {goat.weight} кг. Подоить {goat.milk()} и надо ее по {goat.eat()}')
all_weight_1.append(goat.weight)
all_weight_2[goat.name] = goat.weight
print()

goat_1 = Coat('Копыта', 75)
print(
    f'{goat_1.nickname} {goat_1.name}, издает звук: {goat_1.sound}, весит {goat_1.weight} кг. Подоить {goat_1.milk()} и надо ее по {goat_1.eat()}')
all_weight_1.append(goat_1.weight)
all_weight_2[goat_1.name] = goat_1.weight
print()

lamb = Sheep('Барашек', 90)
print(
    f'{lamb.nickname} {lamb.name}, издает звук: {lamb.sound}, весит {lamb.weight} кг. Мы ее должны {lamb.wool()} и надо ее по {lamb.eat()}')
all_weight_1.append(lamb.weight)
all_weight_2[lamb.name] = lamb.weight
print()

lamb_1 = Sheep('Кудрявый', 110)
print(
    f'{lamb_1.nickname} {lamb_1.name}, издает звук: {lamb_1.sound}, весит {lamb_1.weight} кг. Мы ее должны {lamb_1.wool()} и надо ее по {lamb_1.eat()}')
all_weight_1.append(lamb_1.weight)
all_weight_2[lamb_1.name] = lamb_1.weight
print()

"""Считаем общий вес всех животных(экземпляров класса)"""

print(sum(all_weight_1))

"""Выводим название самого тяжелого животного(экземпляров класса)"""
print(all_weight_2)
print()

big_animal = [(value, key) for key, value in all_weight_2.items()]
print(f'Общий вес животных: {sum(all_weight_1)} кг. Самое тяжелое животное: {max(big_animal)[1]}')