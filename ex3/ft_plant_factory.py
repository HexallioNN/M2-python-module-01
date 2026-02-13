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
        print("Created: ", self.name, " (", self.height, "cm, ", self.age,
              " days)", sep="")


if __name__ == "__main__":
    count = 0
    plants = [Plant(name, height, age) for name, height, age in
              [("Rose", 25, 30), ("Oak", 200, 365), ("Cactus", 5, 90),
               ("Sunflower", 80, 45), ("Fern", 15, 120)]]
    print("=== Plant Factory Output ===")
    for obj in plants:
        count += 1
        obj.get_info()
    print()
    print("Total plants created:", count)
