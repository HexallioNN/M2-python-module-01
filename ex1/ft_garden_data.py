class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print(rose.name, ": ", rose.height, "cm, ", rose.age, " days old", sep="")
    print(sunflower.name, ": ", sunflower.height, "cm, ", sunflower.age,
          " days old", sep="")
    print(cactus.name, ": ", cactus.height, "cm, ", cactus.age, " days old",
                                                                sep="")
