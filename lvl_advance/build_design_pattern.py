"""
Application of the Builder Design Pattern
"""


class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.money = 10
        self.attack = 0
        self.defense = 0

    def __str__(self):
        return \
            f"Hero: {self.name} | " \
            f"💰{self.money} ⚔{self.attack} 🛡{self.defense}"


class HeroBuilder:
    def __init__(self, name):
        self.hero = Hero(name)

    def set_attack(self, attack):
        # if they send me a lower attack than the current one,
        # I preserve the one I already had
        self.hero.attack = max(attack, self.hero.attack)
        return self

    def set_defense(self, defense):
        # if they send me a lower defense than the current one,
        # I preserve the one I already had
        self.hero.defense = max(defense, self.hero.defense)
        return self

    def add_money(self, money):
        self.hero.money += max(money, 0)
        return self

    def get_hero(self):
        return self.hero


if __name__ == '__main__':
    builder = HeroBuilder("Tomas")
    builder.set_attack(-5).set_defense(10)
    builder.add_money(10).add_money(20).add_money(30)
    hero = builder.get_hero()

    print(hero)

class villan: 
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.power = 15
        self.attack = 0
        self.defense = 0

    def __str__(self) -> str:
         return \
            f"Villan: {self.name} | " \
            f"💰{self.power} ⚔{self.attack} 🛡{self.defense}"
    
class VillanBuilder:
    def __init__(self, name) -> None:
        self.villan = villan(name)
    
    def set_attack(self, attack):
        self.villan.attack = max(attack, self.villan.attack)
        return self
    
    def add_power(self, power):
        self.villan.power += power
        return self
    
    def set_defense(self, defense):
        self.villan.defense = max(defense, self.villan.defense)
    
    def get_villan(self):
        return self.villan
 

if __name__ == '__main__':
    vbuilder = VillanBuilder("ratund")
    vbuilder.set_attack(-5).set_defense(10)
    vbuilder.add_power(10).add_power(30)
    villan = vbuilder.get_villan()

    print(villan)