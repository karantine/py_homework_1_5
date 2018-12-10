class Animal:

    name = ''
    weight = 0 #kg
    voice = ''
    feed_status = 'не кормили'
    raw = 0

    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice
        print("Имя животного: {}\nВес животного: {}\nГолос животного: {}".format(self.name, self.weight, self.voice))

    def feed(self):
        self.feed_status = 'да'
        print("Животное по имени {} кормили: {}".format(self.name, self.feed_status))
        return self.feed_status

    def collect_something(self, value):
        self.raw += value
        print('Животное {} дало сырья: {} ед.\n'.format(self.name, self.raw))
        return self.raw

class Milky(Animal):

    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

    def collect_something(self, value):
        self.raw += value
        print('Животное {} дало молока: {} л.\n'.format(self.name, self.raw))
        return self.raw

class EggLaying(Animal):

    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

    def collect_something(self, value):
        self.raw += value
        print('Птица {} дала яиц: {} шт.\n'.format(self.name, self.raw))
        return self.raw

class Wooly(Animal):

    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

    def collect_something(self, value):
        self.raw += value
        print('Животное {} дало шерстви: {} кг.\n'.format(self.name, self.raw))
        return self.raw


cow_manka = Milky('Манька', 530, 'му')
cow_manka.feed()
cow_manka.collect_something(5)

goat_roga = Milky('Рога', 35, 'мее')
goat_roga.feed()
goat_roga.collect_something(2)
goat_kopyta = Milky('Копыта', 40, 'мее')
goat_kopyta.feed()
goat_kopyta.collect_something(2.5)

duck_kryakva = EggLaying('Кряква', 2.1, 'га-га')
duck_kryakva.feed()
duck_kryakva.collect_something(2)

chicken_koko = EggLaying('Коко', 1.2, 'ко-ко')
chicken_koko.feed()
chicken_koko.collect_something(2)
chicken_kukareku = EggLaying('Кукареку', 1.65, 'кукареку')
chicken_kukareku.feed()
chicken_kukareku.collect_something(0)

goose_sery = EggLaying('Серый', 5.3, 'гу-гу')
goose_sery.feed()
goose_sery.collect_something(0)
goose_bely = EggLaying('Белый', 5.7, 'гу-гу')
goose_bely.feed()
goose_bely.collect_something(0)

sheep_barashek = Wooly('Барашек', 138, 'бее')
sheep_barashek.feed()
sheep_barashek.collect_something(0.7)
sheep_kudryavy = Wooly('Кудрявый', 122, 'бее')
sheep_kudryavy.feed()
sheep_kudryavy.collect_something(0.6)

animals_list = [cow_manka, goat_roga, goat_kopyta, sheep_barashek, sheep_kudryavy, duck_kryakva, chicken_koko, chicken_kukareku, goose_bely, goose_sery]

weight_sum = 0
weight_max = 0

for animal in animals_list:
  weight_sum += animal.weight
  if animal.weight > weight_max:
    weight_max = animal.weight
    heaviest_animal = animal.name 

print('Суммарный вес животных {} кг.'.format(weight_sum))
print('Животное с наибольшим весом: {}, {} кг'.format(heaviest_animal, weight_max))
