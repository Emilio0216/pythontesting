def High_Score():
    a = 0
    return a

def Characters_Unlocked():
    Unlocked = ['Knight']
    return Unlocked
#Players
class Saved_Player:
    Max_Health = 21
    Health = 16
    Damage = 4
    Damage_Bonus = 3
    Crit_Chance = 3
    Defense = 10
    Max_Mana = 5
    Mana = 5
    Mana_Bonus = 1
    Speed = 2
    Ability = 1
    Ability_Active = False
    Passive = 1
    Armor = 1
    Weapon = 1
    Money = 0
    Level = 5
    Experience = 0
    Points = 0

class Saved_Status_Effects:
    Advantage = 0 
    Advantage_Duration = 0



class Status_Effects:
    Advantage = 0 #0 = none 1 = Advantage 2 = Disadvantage
    Advantage_Duration = 0 #how long it lasts
    Burn = 0 #how much damage per turn
    Burn_Duration = 0 # how long it lasts


class Knight:
    Max_Health = 21
    Health = 16
    Damage = 4
    Damage_Bonus = 3
    Crit_Chance = 3
    Defense = 10
    Max_Mana = 5
    Mana = 5
    Mana_Bonus = 1
    Speed = 2
    Ability = 1
    Ability_Active = False
    Ability_CoolDown = 4
    Ability_On_CoolDown = 0
    Passive = 1
    Armor = 1
    Weapon = 1
    Money = 0
    Level = 5
    Experience = 0
    Points = 0

class Archer:
    Max_Health = 0
    Health = 0
    Damage = 0
    Damage_Bonus = 0
    Crit_Chance = 0
    Defense = 0
    Max_Mana = 0
    Mana = 0
    Mana_Bonus = 0
    Speed = 0
    Ability = 6
    Passive = 4
    Armor = 1
    Weapon = 1
    Money = 0
    Level = 0
    Experience = 0
class Evil_Knight:
    Max_Health = 1
    Health = 1
    Damage = 1
    Damage_Bonus = 0
    Crit_Chance = 0
    Defense = 0
    Max_Mana = 1
    Mana = 0
    Mana_Bonus = 0
    Speed = 1000
    Ability = 2
    Passive = 2
    Armor = 1
    Weapon = 1
    Money = 0
    Level = 0
    Experience = 0
#Bosses
class Osman:
    Max_Health = 50
    Health = 50
    Damage = 1000
    Damage_Bonus = 100
    Crit_Chance = 100
    Defense = 0
    Max_Mana = 20
    Mana = 0
    Mana_Bonus = 1
    Speed = 0
    Ability = 3
    Passive = 3
    Armor = 0
    Weapon = 0
    Money = 40
    Level = 0
    Experience = 40
#Enemies
class Wolf:
    Enemy_Type = "Wolf"
    Mentality = 1
    Max_Health = 8
    Health = 8
    Damage = 4
    Damage_Bonus = 3
    Crit_Chance = 8
    Defense = 2
    Max_Mana = 2
    Mana = 2
    Mana_Bonus = 1
    Speed = 10
    Ability = 0
    Ability_Active = False
    Ability_CoolDown = 0
    Ability_On_CoolDown = 0
    Passive = 0
    Armor = 0
    Weapon = 0
    Money = 4
    Level = 0
    Experience = 500
class Turtle:
    Enemy_Type = "Turtle"
    Max_Health = 20
    Health = 20
    Damage = 2
    Damage_Bonus = -4
    Crit_Chance = 1
    Defense = 6
    Max_Mana = 0
    Mana = 0
    Mana_Bonus = 0
    Speed = 1
    Ability = 5
    Passive = 0
    Armor = 0
    Weapon = 0
    Money = 5
    Level = 0
    Experience = 5
import random
#Maps
def Maps(Area):
    Random = random.randint(1,5)
    if Area == 1:
        if Random == 1:
            Map = 'Nightengale'
        elif Random == 2:
            Map = 'TownTwo'
        elif Random == 3:
            Map = 'Holden'
        elif Random == 4:
            Map = 'Cobalt'
        elif Random == 5:
            Map = 'Walden'
    if Area == 2:
        if Random == 1:
            Map = 'Forest'
        elif Random == 2:
            Map = 'Swamp'
        elif Random == 3:
            Map = 'Cave'
        elif Random == 4:
            Map = 'Ruins'
        elif Random == 5:
            Map = 'Cove'
    if Area == 3:
        if Random == 1:
            Map = 'castle of evil'
    return Map
