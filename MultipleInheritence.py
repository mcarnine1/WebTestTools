class Cat:
    def __init__(self, number_of_legs, makes_sound):
        self.number_of_legs = number_of_legs
        self.makes_sound = makes_sound

    def get_number_of_legs(self):
        return self.number_of_legs

    def get_sound(self):
        return self.makes_sound


class Dog:
    def __init__(self, hair_type, has_tail):
        self.hair_type = hair_type
        self.has_tail = has_tail

    def get_hair_type(self):
        return self.hair_type

    def get_has_tail(self):
        return self.has_tail


class Lizard:
    def __init__(self, skin_type, food_preference):
        self.skin_type = skin_type
        self.food_preference = food_preference

    def get_skin_type(self):
        return self.skin_type

    def get_food_preference(self):
        return self.food_preference


class A(Cat, Dog):
    def __init__(self, number_of_legs, makes_sound):
        super().__init__(number_of_legs, makes_sound)
        print(cat.get_number_of_legs())
        print(cat.get_sound())
        print(dog.get_hair_type())
        print(dog.get_has_tail())


class B(Dog, Lizard):
    def __init__(self, hair_type, has_tail):
        super().__init__(hair_type, has_tail)
        print(dog.get_hair_type())
        print(dog.get_has_tail())
        print(lizard.get_skin_type())
        print(lizard.get_food_preference())


class M(B, A, Lizard):
    def __init__(self, skin_type, food_preference):
        super().__init__(skin_type, food_preference)
        print(a.get_number_of_legs())
        print(a.get_sound())
        print(b.get_hair_type())
        print(b.get_has_tail())
        print(dog.get_hair_type())
        print(dog.get_has_tail())
        print(lizard.get_skin_type())
        print(lizard.get_food_preference())


cat = Cat(4, "meow")
dog = Dog("long", True)
lizard = Lizard("rough", "veggies")
a = A(1, 2)
b = B(3, 4)
m = M(5, 6)

