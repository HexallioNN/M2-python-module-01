class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height = self.height + 1

    def age_method(self):
        self.age = self.age + 1

    def get_info(self):
        print(self.name, ": ", self.height, "cm", sep="", end=" ")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        super().get_info()
        print(self.color, "flowers (blooming),", end=" ")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 points: int, ) -> None:
        super().__init__(name, height, age, color)
        self.points = points

    def get_info(self):
        super().get_info()
        print("Prize points:", self.points, end=" ")


class Garden:
    def __init__(self, name: str):
        self.name = name
        self.plants = []
        self.plant_count = 0
        self.total_growth = 0

    def add_plant(self, plant: Plant):
        if isinstance(plant, Plant):
            self.plants.append(plant)
            self.plant_count += 1
            print("Added ", plant.name, " to ", self.name, "'s garden", sep="")

    def grow_all(self):
        print(self.name, "is helping all plants grow...")
        for x in self.plants:
            x.grow()
            self.total_growth += 1
            print(x.name, "grew 1cm")

    def type_count(self):
        self.default_count = 0
        self.flowering_count = 0
        self.prize_count = 0
        for x in self.plants:
            if isinstance(x, PrizeFlower):
                self.prize_count += 1
            elif isinstance(x, FloweringPlant):
                self.flowering_count += 1
            elif isinstance(x, Plant):
                self.default_count += 1

    def garden_info(self):
        print("=== ", self.name, "'s Garden Report ===", sep="")
        print("Plants in garden:")
        for x in self.plants:
            print("-", end=" ")
            x.get_info()
            print()
        print()


class GardenManager:
    def __init__(self):
        self.gardens = []

    def add_garden(self, garden: Garden):
        self.gardens.append(garden)

    @classmethod
    def create_garden_network(cls):
        manager = cls()
        alice = Garden("Alice")
        bob = Garden("Bob")
        manager.add_garden(alice)
        manager.add_garden(bob)
        return manager

    @staticmethod
    def height_validation(gardens):
        for garden in gardens:
            for plant in garden.plants:
                if plant.height < 0:
                    return False
        return True

    def total_gardens(self):
        return len(self.gardens)

    class GardenStats:
        def __init__(self, garden: Garden):
            self.garden = garden

        def type_count(self):
            default_count = 0
            flowering_count = 0
            prize_count = 0
            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize_count += 1
                elif isinstance(plant, FloweringPlant):
                    flowering_count += 1
                elif isinstance(plant, Plant):
                    default_count += 1
            return default_count, flowering_count, prize_count

        def calculate_score(self):
            score = 0
            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    score += plant.height + plant.points * 4
                else:
                    score += plant.height
            return score

        def print_garden_stats(self):
            print("Plants added:", self.garden.plant_count,
                  ", Total growth:", self.garden.total_growth, "cm")
            default_count, flowering_count, prize_count = self.type_count()
            print("Plant type:", default_count, "regular", flowering_count,
                  "flowering", prize_count, "prize flowers")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    plant = Plant("Oak Tree", 100, 240)
    flowering = FloweringPlant("Rose", 25, 67, "red")
    prize = PrizeFlower("Sunflower", 50, 104, "yellow", 10)

    test = Plant("Test Tree", 92, 123)
    bob = Garden("Bob")
    bob.add_plant(test)

    alice = Garden("Alice")
    alice.add_plant(plant)
    alice.add_plant(flowering)
    alice.add_plant(prize)
    print()
    alice.grow_all()
    print()
    alice.garden_info()

    manager = GardenManager()
    manager.add_garden(alice)
    manager.add_garden(bob)
    stats = manager.GardenStats(alice)
    stats.print_garden_stats()

    valid = GardenManager.height_validation(manager.gardens)
    print("\nHeight validation test:", valid)

    print("Garden scores -", end=" ")
    for garden in manager.gardens:
        score = manager.GardenStats(garden).calculate_score()
        print(f"{garden.name}: {score}", end=", ")
    print("\nTotal gardens managed:", manager.total_gardens())
