class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.0,
    ) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.growth_rate = growth_rate

        if height >= 0:
            self._height = height
        else:
            print(f"{self.name}: Error, height can't be negative")

        if age >= 0:
            self._age = age
        else:
            print(f"{self.name}: Error, age can't be negative")

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {new_height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {new_age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self) -> None:
        self._height += self.growth_rate

    def age(self) -> None:
        self._age += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self.get_height(), 1)}cm long and "
            f"{self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        growth_rate: float = 2.1,
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0.0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        if self.nutritional_value.is_integer():
            print(f"Nutritional value: {int(self.nutritional_value)}")
        else:
            print(f"Nutritional value: {round(self.nutritional_value, 1)}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()