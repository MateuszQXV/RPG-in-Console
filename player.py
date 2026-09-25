class Player:

    def __init__(self):

        self.hp = 0

        self.attack = 0

        self.mana = 0

        self.player_class = ""

        self.inventory = []

    def set_warrior(self):

        self.player_class = "Warrior"

        self.hp = 120

        self.attack = 15

        self.mana = 0

        self.inventory = [
            "Old Sword",
            "Old Helmet",
            "Old Breastplate",
            "Old Pants",
            "Old Boots"
        ]

    def set_mage(self):

        self.player_class = "Mage"

        self.hp = 80

        self.attack = 20

        self.mana = 50

        self.inventory = [
            "Old Mage Staff",
            "Old Hat",
            "Old Robe",
            "Old Boots"
        ]

    def set_archer(self):

        self.player_class = "Archer"

        self.hp = 100

        self.attack = 17

        self.mana = 10

        self.inventory = [
            "Old Bow",
            "Old Helmet",
            "Old Pants",
            "Old Boots"
        ]

    def show_stats(self):

        print("\nStats:")

        print(f"\tClass:  {self.player_class}")

        print(f"\tHP:     {self.hp}")

        print(f"\tAttack: {self.attack}")

        print(f"\tMana:   {self.mana}")

        print("\nInventory:")

        for item in self.inventory:

            print(f"  - {item}")

