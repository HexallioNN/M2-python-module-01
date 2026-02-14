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
        print(self.name, ": ", self.height, "cm, ", self.age,
                                            " days old", sep="")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    start_height = rose.height
    for day in range(6):
        rose.age_method()
        rose.grow()
    print("=== Day", day + 2, "===")
    end_height = start_height + day
    rose.get_info()
    print("Growth this time: +", end_height+1 - start_height, "cm", sep="")
