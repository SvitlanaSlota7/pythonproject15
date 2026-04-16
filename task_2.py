class Dog:
    age_factor = 7

    def __init__(self, dog_age: int):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor

if __name__ == "__main__":
    my_dog = Dog(3)
    result = my_dog.human_age()

    print(f"Dog's age in years: {my_dog.dog_age}")
    print(f"Human equivalent: {result} years old")