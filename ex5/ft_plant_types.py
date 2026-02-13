class Plant:
    def __init__(self: type, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self: type):
        self.height = self.height + 1

    def age_method(self: type):
        self.age = self.age + 1

    def get_info(self: type):
        print(self.height, "cm, ", self.age,
              " days,", sep="", end=" ")


class Flower(Plant):
    def __init__(self: type, name: str, height: int, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self: type):
        print(self.name, "(Flower):", end=" ")
        super().get_info()
        print(self.color, "color")

    def bloom(self: type):
        print(self.name, "is blooming beautifully!")


class Tree(Plant):
    def __init__(self: type, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self: type):
        print(self.name, "(Tree):", end=" ")
        super().get_info()
        print(self.trunk_diameter, "cm diameter", sep="")

    def produce_shade(self: type):
        print(self.name, "provides", int(self.trunk_diameter / 0.64),
              "square meters of shade")


class Vegetable(Plant):
    def __init__(self: type, name: str, height: int, age: int,
                 harvest_season: str, nutrition_value: str) -> None:
        super().__init__(name, height, age)
        self.nutrition = nutrition_value
        self.harvest = harvest_season

    def get_info(self: type):
        print(self.name, "(Vegetable):", end=" ")
        super().get_info()
        print(self.harvest, " harvest", sep="")
        print(self.name, "is rich in", self.nutrition)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "red")
    rose.get_info()
    rose.bloom()
    print()
    hibiscus = Flower("Hibiscus", 15, 50, "red")
    hibiscus.get_info()
    hibiscus.bloom()
    print()
    Oak = Tree("Oak", 500, 1825, 50)
    Oak.get_info()
    Oak.produce_shade()
    print()
    Spruce = Tree("Spruce", 4000, 9125, 100)
    Spruce.get_info()
    Spruce.produce_shade()
    print()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    tomato.get_info()
    print()
    avocado = Vegetable("Avocado", 100, 528, "fall - spring", "vitamin K")
    avocado.get_info()
