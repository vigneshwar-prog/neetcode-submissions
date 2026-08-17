class StoreItem:
    def __init__(self,name: str,price: str):
        self.name = name
        self.price = price

        pass  # Add: name, price

    def displayStoreItem(self):
        print(self.name)
        print(self.price)

chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them
chips.displayStoreItem()


