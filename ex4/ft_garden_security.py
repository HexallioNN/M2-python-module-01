class SecurePlant:
    def set_height(self: type, new_height: int):
        if new_height < 0:
            print("Invalid operation attempted: height ", new_height,
                  "cm [REJECTED]", sep="")
            print("Security: Negative height rejected")
            print()
        else:
            self.__height = new_height
            print("Height updated: ", new_height, "cm [OK]", sep="")

    def set_age(self: type, new_age: int):
        if new_age < 0:
            print("Invalid operation attempted: age ", new_age,
                  " days [REJECTED]", sep="")
            print("Security: Negative age rejected")
            print()
        else:
            self.__age = new_age
            print("Age updated:", new_age, "days [OK]")

    def get_age(self: type):
        return self.__age

    def get_height(self: type):
        return self.__height

    def __init__(self: type, name: str, height: int, age: int) -> None:
        self.__name = name
        print("Plant created:", self.__name)
        self.set_height(height)
        self.set_age(age)
        print()

    def get_info(self: type):
        print("Current plant: ", self.__name, " (", self.__height, "cm, ",
              self.__age, " days)", sep="")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    rose.get_info()
