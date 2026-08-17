class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        self.hunger -=1
        print("Fluffy has been fed.")
        pass
    def get_hunger_level(self):
        print(f"Fluffy's hunger level: {self.hunger}")
    
    def feed_multiple(self,count=1):
        for _ in range(count):
            self.feed()
            self.get_hunger_level()


# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
my_pet.feed_multiple(3)

