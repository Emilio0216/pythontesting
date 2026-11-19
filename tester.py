def change(amount):
    Player.Health -= amount
class smt:
    Max_Health = 35
    Health = 35
    Damage = 6
    Damage_Bonus = 5
    Crit_Chance = 5
    Defense = 16
    Max_Mana = 5
    Mana = 5
    Mana_Bonus = 3
    Speed = 3
    Level = 0
    Experience = 0
class smtelse:
    Max_Health = 55
    Health = 55
    Damage = 6
    Damage_Bonus = 5
    Crit_Chance = 5
    Defense = 16
    Max_Mana = 5
    Mana = 5
    Mana_Bonus = 3
    Speed = 3
    Level = 0
    Experience = 0
Player = smt()
print(Player.Health)
change(10)
print(Player.Health)
Player = smtelse()
print(Player.Health)