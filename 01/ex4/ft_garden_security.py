class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0
        self._age = 0

        if height >= 0:
            self._height = height
        else:
            print(f"{self.name}: Error, height can't be negative")

        if age >= 0:
            self._age = age
        else:
            print(f"{self.name}: Error, age can't be negative")

    def show(self):
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def set_height(self, new_height):
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {new_height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {new_age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age
    
def main():
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    rose.set_age(-10)
    print()

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()