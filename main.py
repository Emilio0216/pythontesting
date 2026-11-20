#nothing
import math, time, random, sys, os, settings, data
from time import sleep
from data import Saved_Player, Knight, Archer, Wolf, Saved_Status_Effects, Status_Effects, Evil_Knight
#Helper functions
def Question(Answer_Type, Question_Text = "I NEED TO RESET THIS TEXT", Fail_Text = "That is not a valid answer. Please try again.", Text_Time = 0.02):
    Text_Scroll_Effect(Question_Text, Text_Time, True)
    while True:
        Answer = input()
        #probably a better way to do this but im lazy
        try:
            Correct = Answer_Type(Answer)
            break
        except ValueError:
            Text_Scroll_Effect(Fail_Text, .01)
    print('')
    return Correct
def Text_Scroll_Effect(Text, Time, Question = False):
    for char in Text:
        print(char, end='')
        sys.stdout.flush()
        sleep(Time)
    if Question == False:
        print('')
def Confirmation():
    Question(str,'enter anything to continue: ', 'if you get this secret text congrats', Text_Time)
def Clear_Terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def Ability(User, Text_Time):
    if User == 1:
        if Player.Ability == 1:
            Parry = True

def Turn_Order():
    Same = True
    while Same == True:
        Player_Roll = random.randint(1,20)
        Enemy_Roll = random.randint(1,20)
        Outcome = (Player_Roll + Player.Speed) - (Enemy_Roll + Enemy.Speed)
        if Outcome > 0:
            Result = 1
            Same = False
        if Outcome < 0:
            Result = 2
            Same = False
    return Result
def Attack(Attacker, Text_Time):
    Attack_Roll = random.randint(1,20)
    Advantage_Roll = random.randint(1,20)
    if Attacker == 1:
        #Seeing if the player has advantage or disadvantage
        if Player_Effects.Advantage == 0:
            Landed_Hit = Attack_Roll + Player.Damage_Bonus
        elif Player_Effects.Advantage == 1:
            if Attack_Roll > Advantage_Roll:
                Landed_Hit = Attack_Roll + Player.Damage_Bonus
            else:
                Landed_Hit = Advantage_Roll + Player.Damage_Bonus
        elif Player_Effects.Advantage == 2:
            if Attack_Roll > Advantage_Roll:
                Landed_Hit = Advantage_Roll + Player.Damage_Bonus
            else:
                Landed_Hit = Attack_Roll + Player.Damage_Bonus

        #seeing if that attack was strong enough to break the Enemy's defense and if it was if the enemy dodged it with speed
        if Landed_Hit >= Enemy.Defense/2:
            Dodge_Roll = random.randint(1,100)
            Dodge_Chance = Enemy.Speed
            if Dodge_Chance > 50:
                Dodge_Chance = 50
            if Dodge_Chance > Dodge_Roll:
                Text_Scroll_Effect('The ' + str(Enemy.Enemy_Type) + ' Dodged your attack', Text_Time)
            else:
                crit = random.randint(1,100)
                Damage = int(round((Player.Damage * (Landed_Hit/100 + 1)) /(Enemy.Defense/100 + 1),0))
                if crit <= Player.Crit_Chance:
                    Text_Scroll_Effect('CRIT!',Text_Time)
                    Damage *= 2
                Enemy.Health -= Damage
                if Enemy.Health < 0:
                    Enemy.Health = 0

                Text_Scroll_Effect('You hit the ' + str(Enemy.Enemy_Type) + ' For ' + str(Damage) + ' damage bringing its health down to ' + str(Enemy.Health), Text_Time)
        else:
            Text_Scroll_Effect('The ' + str(Enemy.Enemy_Type) + ' blocked your attack', Text_Time)
        
        if Player_Effects.Advantage != 0:
            Player_Effects.Advantage_Duration -= 1
    if Attacker == 2:
        #Seeing if the player has advantage or disadvantage
        if Enemy_Effects.Advantage == 0:
            Landed_Hit = Attack_Roll + Enemy.Damage_Bonus
        elif Enemy_Effects.Advantage == 1:
            if Attack_Roll > Advantage_Roll:
                Landed_Hit = Attack_Roll + Enemy.Damage_Bonus
            else:
                Landed_Hit = Advantage_Roll + Enemy.Damage_Bonus
        elif Enemy_Effects.Advantage == 2:
            if Attack_Roll > Advantage_Roll:
                Landed_Hit = Advantage_Roll + Enemy.Damage_Bonus
            else:
                Landed_Hit = Attack_Roll + Enemy.Damage_Bonus

        #seeing if that attack was strong enough to break the Enemy's defense and if it was if the enemy dodged it with speed
        if Landed_Hit > Player.Defense/2:
            Dodge_Roll = random.randint(1,100)
            Dodge_Chance = Player.Speed
            if Dodge_Chance > 50:
                Dodge_Chance = 50
            if Dodge_Chance > Dodge_Roll:
                Text_Scroll_Effect('You Dodged the attack', Text_Time)
            else:
                crit = random.randint(1,100)
                Damage = int(round((Enemy.Damage * (Landed_Hit/100 + 1)) /(Player.Defense/100 + 1),0))
                if crit <= Enemy.Crit_Chance:
                    Text_Scroll_Effect('CRIT!',Text_Time)
                    Damage *= 2
                Player.Health -= Damage
                if Player.Health < 0:
                    Player.Health = 0

                Text_Scroll_Effect(str(Enemy.Enemy_Type) + ' hit you for ' + str(Damage) + ' damage bringing your health down to ' + str(Player.Health), Text_Time)
        else:
            Text_Scroll_Effect('You blocked the attack', Text_Time)
        
        if Enemy_Effects.Advantage != 0:
            Enemy_Effects.Advantage_Duration -= 1
def Player_Turn(Text_Time):
    Confirm = False
    while Confirm == False:
        Player_Choice = Question(int, 'Players turn\n1. Attack\n2. Use a Spell\n3. Use an item(Unfinished)\n4. Use Active Ability\nWhat would you like to do?: ', 'Try again', Text_Time)
        if Player_Choice == 1:
            Attack(1, Text_Time)
            Confirm = True
        elif Player_Choice == 2:
            Spell_Confirm = False
            while Spell_Confirm == False:
                Spell_Choice = Question(int, 'You have '+ str(Player.Mana) + '/' + str(Player.Max_Mana) + ' Mana\n0. Cancle\n1. FireBall-5MP\n2. Heal-4MP\nWhat would you like to do?: ', 'Not a Valid Option',Text_Time)
                if Spell_Choice == 0:
                    Text_Scroll_Effect('You decide a spell wouldnt be wise\n', Text_Time)
                    Spell_Confirm = True
                if Spell_Choice == 1:
                    if Player.Mana >= 5:
                        Magic_Damage = int(round((random.randint(1,50)/100 + 1) * Player.Max_Mana))
                        Player.Mana -= 5
                        Enemy.Health -= Magic_Damage
                        if Enemy.Health < 0:
                            Enemy.Health = 0
                        Text_Scroll_Effect('You cast fireball dealing ' + str(Magic_Damage) + ' to the ' + str(Enemy.Enemy_Type) + ' bringing its health down to ' + str(Enemy.Health), Text_Time)
                        Spell_Confirm = True
                        Confirm = True
                    else:
                        Text_Scroll_Effect('You tried to cast fireball but you didnt have enough mana', Text_Time)
                elif Spell_Choice == 2:
                    if Player.Mana >= 4:
                        Healing = int(round(Player.Max_Health/5 + Player.Max_Mana/4,0))
                        Player.Health += Healing
                        if Player.Health > Player.Max_Health:
                            Player.Health = Player.Max_Health
                        Player.Mana -= 4
                        Text_Scroll_Effect('You healed ' + str(Healing) + ' health bringing you health up to ' + str(Player.Health), Text_Time)
                        Spell_Confirm = True
                        Confirm = True
                    else:
                        Text_Scroll_Effect('You didnt have enough mana to cast heal',Text_Time)
        elif Player_Choice == 3:
            Text_Scroll_Effect('It said Unfinished and you still thought it would work?', Text_Time)
        elif Player_Choice == 4:
            if Player.Ability_On_CoolDown == 0:
                Player.Ability_Active = True
                Player.Ability_On_CoolDown = Player.Ability_CoolDown
                Ability(1, Text_Time)
            else:
                Text_Scroll_Effect('Ability still on cooldown for ' + str(Player.Ability_On_CoolDown) + ' More turns',Text_Time)
            Confirm = True
    Player.Mana += Player.Mana_Bonus
    Player.Ability_On_CoolDown -= 1
    if Player.Mana > Player.Max_Mana:
        Player.Mana = Player.Max_Mana
    if Player.Ability_On_CoolDown < 0:
        Player.Ability_On_CoolDown = 0
    Confirmation()


def Enemy_Turn(Text_Time):
    """
    Mentality 1 is Agressive attacking unless healing is needed very minimal magic or buffs and no items just raw attacks
    """
    if Enemy.Mentality == 1:
        Smart = random.randint(1,2)
        if Smart == 1:
            if Enemy.Health < Enemy.Max_Health/2 and Enemy.Mana >= 4:
                Enemy_Choice = 2
                Spell_Choice = 2
            elif Enemy.Ability != 0 and Enemy.Ability_On_CoolDown == 0:
                Enemy_Choice = 4
            elif Enemy.Mana >= 5 and Enemy.Mana == Enemy.Max_Mana:
                Enemy_Choice = 2
                Spell_Choice = 1
            else:
                Enemy_Choice = 1
        else:
            Enemy_Choice = 1


    if Enemy_Choice == 1:
        Attack(2, Text_Time)
    elif Enemy_Choice == 2:
        if Spell_Choice == 1:
            Magic_Damage = int(round((random.randint(1,50)/100 + 1) * Enemy.Max_Mana))
            Enemy.Mana -= 5
            Player.Health -= Magic_Damage
            if Player.Health < 0:
                Player.Health = 0
            Text_Scroll_Effect(str(Enemy.Enemy_Type) + ' casts fireball dealing ' + str(Magic_Damage) + ' to you bringing your health down to ' + str(Player.Health), Text_Time)
        elif Spell_Choice == 2:
            Healing = int(round(Enemy.Max_Health/5 + Enemy.Max_Mana/4,0))
            Enemy.Health += Healing
            if Enemy.Health > Enemy.Max_Health:
                Enemy.Health = Enemy.Max_Health
            Enemy.Mana -= 4
            Text_Scroll_Effect(str(Enemy.Enemy_Type) +' healed ' + str(Healing) + ' health bringing its health up to ' + str(Enemy.Health), Text_Time)

        elif Enemy_Choice == 3:
            Text_Scroll_Effect('It said Unfinished and you still thought it would work?', Text_Time)
        elif Enemy_Choice == 4:
            Enemy.Ability_Active = True
            Enemy.Ability_On_CoolDown = Enemy.Ability_CoolDown
            Ability(2, Text_Time)
    Enemy.Mana += Enemy.Mana_Bonus
    Enemy.Ability_On_CoolDown -= 1
    if Enemy.Mana > Enemy.Max_Mana:
        Enemy.Mana = Enemy.Max_Mana
    if Enemy.Ability_On_CoolDown < 0:
            Enemy.Ability_On_CoolDown = 0
    Confirmation()

def Combat_Normal(Text_Time):
    Text_Scroll_Effect('You See a ' + Enemy.Enemy_Type + '!\n', Text_Time)
    Combat = True
    while Combat == True and Enemy.Health > 0 and Player.Health > 0:
        Text_Scroll_Effect('Player Health = ' + str(Player.Health) + '/' + str(Player.Max_Health) + ' Enemy Health = '+ str(Enemy.Health) + '/' + str(Enemy.Max_Health),Text_Time)
        Confirmation()
        Order = Turn_Order()
        if Order == 1:
            Player_Turn(Text_Time)
            if Enemy.Health > 0:
                Enemy_Turn(Text_Time)
        elif Order == 2:
            Enemy_Turn(Text_Time)
            if Player.Health > 0:
                Player_Turn(Text_Time)
    if Player.Health > 0:
        Text_Scroll_Effect('You gained ' + str(Enemy.Experience) + ' XP', Text_Time)
        Player.Experience += Enemy.Experience
        Level_Up = True
        while Level_Up == True:
            if Player.Experience > Player.Level:
                Multi_Level = True
                Points_Gained = 0
                while Player.Experience > Player.Level:
                    Text_Scroll_Effect('You leveled up!',Text_Time)
                    Player.Experience -= Player.Level
                    Player.Level *= 1.2
                    Player.Level = int(round(Player.Level))
                    Points_Gained += 1
                Text_Scroll_Effect('Next level costs ' + str(Player.Level) + ' Experience and you have ' + str(Player.Experience) + ' Experience leftover', Text_Time)
                Player.Points += Points_Gained*5
            elif Player.Experience < Player.Level:
                Level_Up = False
def Level_Up(Text_Time):
    Investing = True
    while Investing == True:
        Upgrade_Choice = Question(int, 'You have ' + str(Player.Points) + ' XP left to spend\n1. Health\n2. Damage\n3. Hit Chance\n4. Crit Chance\n5. Defense\n6. Mana\n7. Mana regen\n8. Speed\n9. Save for later\nWhat would you like to spend your XP on?: ', 'Invalid', Text_Time)
        Allowed = False
        if Upgrade_Choice == 1:
            while Allowed == False:
                Mass = Question(int, '2 health per 1 XP spent\nHow many would you like to buy?: ', 'i hate you', Text_Time)
                if Player.Points < Mass:
                    Text_Scroll_Effect('You dont have enough XP', Text_Time)
                else:
                    Prev_Health = Player.Max_Health
                    Player.Max_Health += Mass*2
                    Player.Health = int(round((Player.Health/Prev_Health) * Player.Max_Health))
                    Allowed = True
                    Player.Points -= Mass
        elif Upgrade_Choice == 2:
            while Allowed == False:
                Mass = Question(int, '1 Damage per 1 XP spent\nHow many would you like to buy?: ', 'i hate you', Text_Time)
                if Player.Points < Mass:
                    Text_Scroll_Effect('You dont have enough XP', Text_Time)
                else:
                    Player.Damage += Mass
                    Allowed = True
                    Player.Points -= Mass
        elif Upgrade_Choice == 3:
            while Allowed == False:
                Mass = Question(int, '1 Damage Bonus per 3 XP spent\nHow many would you like to buy?: ', 'i hate you', Text_Time)
                if Player.Points < Mass*3:
                    Text_Scroll_Effect('You dont have enough XP', Text_Time)
                else:
                    Player.Damage_Bonus += Mass
                    Allowed = True
                    Player.Points -= Mass*3
        elif Upgrade_Choice == 4:
            while Allowed == False:
                Mass = Question(int, '1 Crit Chance per 2 XP spent\nHow many would you like to buy', 'i hate you', Text_Time)
                if Player.Points < Mass*2:
                    Text_Scroll_Effect('You dont have enough XP', Text_Time)
                else:
                    Player.Crit_Chance += Mass
                    Allowed = True
                    Player.Points -= Mass*2
        elif Upgrade_Choice == 5:
            while Allowed == False:
                Mass = Question(int, '1 Defense per 2 XP spent\nHow many would you like to buy?: ', 'i hate you', Text_Time)
                if Player.Points < Mass*2:
                    Text_Scroll_Effect('You dont have enough XP', Text_Time)
                else:
                    Player.Defense += Mass
                    Allowed = True
                    Player.Points -= Mass*2
        elif Upgrade_Choice == 6:
            while Allowed == False:
                Mass = Question(int, '1 Mana per 2 XP spent\nHow many would you like to buy?: ', 'i hate you', Text_Time)
                if Player.Points < Mass*2:
                    Text_Scroll_Effect('You dont have enough XP', Text_Time)
                else:
                    Prev_Mana = Player.Max_Mana
                    Player.Max_Mana += Mass*2
                    Player.Mana = int(round((Player.Mana/Prev_Mana) * Player.Max_Mana))
                    Allowed = True
                    Player.Points -= Mass
        elif Upgrade_Choice == 7:
            while Allowed == False:
                Mass = Question(int, '1 Mana regen per 4 XP spent\nHow many would you like to buy?: ', 'i hate you', Text_Time)
                if Player.Points < Mass*4:
                    Text_Scroll_Effect('You dont have enough XP', Text_Time)
                else:
                    Player.Mana_Bonus += Mass
                    Allowed = True
                    Player.Points -= Mass*4
        elif Upgrade_Choice == 8:
            while Allowed == False:
                Mass = Question(int, '1 Speed per 1 XP spent\nHow many would you like to buy?: ', 'i hate you', Text_Time)
                if Player.Points < Mass:
                    Text_Scroll_Effect('You dont have enough XP', Text_Time)
                else:
                    Player.Speed += Mass
                    Allowed = True
                    Player.Points -= Mass
        elif Upgrade_Choice == 9:
            Investing = False
        if Player.Points == 0:
            Investing = False




#Main script I HATE EMILIO >:), From Ruben that you will never get my calc 
for i in range(1): #data in a range loop for space
    Character_Unlocks = data.Characters_Unlocked()
    Text_Time = settings.Text_Speed()
    Difficulty = settings.Difficulty()
    High_Score = data.High_Score()
    Player = Saved_Player()
    Player_Effects = Saved_Status_Effects()
Clear_Terminal()
Text_Scroll_Effect("Welcome to Dungeons and Damage (Python Single Player Edition)", Text_Time)
Question(str,'enter anything to continue: ', 'if you get this secret text congrats', Text_Time)
while(True):
    Clear_Terminal()
    Default_Variable_Text = "Default text speed: " + str(Text_Time) + ", Difficulty: " + str(Difficulty) + ", High score: " + str(High_Score) + ", Characters unlocked: " + str(Character_Unlocks) 
    Text_Scroll_Effect(Default_Variable_Text, Text_Time)
    Text_Scroll_Effect("0. Settings\n1. Start\n2. Quit", Text_Time)
    Menu_Choice = Question(int, "What would you like to do?: ", "Please choose a whole number 0-7", Text_Time)
    if Menu_Choice == 0:
        Clear_Terminal()
        Options = Question(int,"0. Cancel\n1. Text Speed\n2. Difficulty\n3. Reset data\n4. Unlock everything\nWhat would you like?: ", "a number please", Text_Time)
        if Options == 1:
            Text_Time = Question(float, "How fast do you want the text scroll speed: " , "Number from .04 to 0" ,Text_Time)
            with open('settings.py', 'r') as f:
                lines = f.read().split('\n')
                new_line = '    a = ' + str(Text_Time)
                new_file = '\n'.join(lines[:1] + [new_line] + lines[2:])
            with open('settings.py', 'w') as f:
                f.write(new_file)
        elif Options == 2:
            Difficulty = Question(int, "1 = easy\n2 = normal\n3 = hard\nWhat Difficulty?: " , "not a decimal or text" ,Text_Time)
            with open('settings.py', 'r') as f:
                lines = f.read().split('\n')
                new_line = '    b = ' + str(Difficulty)
                new_file = '\n'.join(lines[:5] + [new_line] + lines[6:])
            with open('settings.py', 'w') as f:
                f.write(new_file)
        elif Options == 3:
            YoN = Question(int,"1. yes\n2. no\nAre you SURE you want to reset all of your data (unlocks, highscore, money, wtv else i make up)?: ", "give a non decimal number pls", Text_Time)
            if YoN == 1:
                with open('data.py', 'r') as f:
                    lines = f.read().split('\n')
                    new_line = '    a = ' + "0"
                    new_file = '\n'.join(lines[:1] + [new_line] + lines[2:])
                with open('data.py', 'w') as f:
                    f.write(new_file)
                Character_Unlocks = ['Knight']
                High_Score = 0
                with open('data.py', 'r') as f:
                    lines = f.read().split('\n')
                    new_line = '    Max_health = 0\n    Health = 0\n    Damage = 0\n    Damage_Bonus = 0\n    Crit_Chance = 0\n    Defense = 0\n    Max_Mana = 0\n    Mana = 0\n    Mana_Bonus = 0\n    Speed = 0\n    Ability = ""\n    Passive = ""\n    Armor = ""\n    Weapon = ""\n    Money = 0\n    Level = 0\n    Experience = 0'
                    new_file = '\n'.join(lines[:9] + [new_line] + lines[27:])
                with open('data.py', 'w') as f:
                    f.write(new_file)

        elif Options == 4:
            Character_Unlocks = ['Knight', 'Archer']


#actual game
    elif Menu_Choice == 1:
        
        #Choosing Avilable character from unlocked characters
        Correct_Character = False
        while Correct_Character == False:
            Character_Select = str.lower(Question(str, str(Character_Unlocks) + "\nwho would you like to play?: "))
            for i in Character_Unlocks:
                if Character_Select == str.lower(i):
                    Correct_Character = True
                elif Character_Select == 'evil kirk':
                    Correct_Character = True
        #Stat applying
        if Character_Select == 'knight':
            Player = Knight()
        elif Character_Select == 'archer':
            Player = Archer()
        elif Character_Select == 'saved player':
            Player = Saved_Player()
        elif Character_Select == 'evil kirk':
            Player = Evil_Knight()
        Player_Effects = Status_Effects()
        Clear_Terminal()
        Campaign = Question(int,'1. Slaying of the king\nWhat Campaign would you like to play?: ', 'whole number', Text_Time)
        if Campaign == 1:
            Campaign_Text = ' You must journey to the kingdom of Evil land idk and slay the evilllll king'
        Town = data.Maps(1)
        Area = 1
        if Town == 'Nightengale':
            Expo_Text = 'Nightengale a rich and vibrant town bustling with movement. but soon the town falls silent a silence that has never came before.' + Campaign_Text
        else:
            Expo_Text = '... you have no recolection of your memorys and you dont know where you are and the only thing you know is that' + Campaign_Text
        Text_Scroll_Effect('You Start your journey in the town of ' + Expo_Text, Text_Time)
        Confirmation()
        Clear_Terminal()
        while True:
            Choices_Text = ''
            Traveling = False
            Trader = True
            while Traveling == False:
                Place_Choice = Question(int, '0. Travel\n1. Look at stats and inventory\n2. Use XP points\n3. Search around\n' + Choices_Text + '\nWhat would you like to do?: ', 'Number not decimal or text', Text_Time)
                if Place_Choice == 0:
                    Traveling = True
                    Area += 1
                elif Place_Choice == 1:
                    Text_Scroll_Effect('Health = ' + str(Player.Health) + '/' + str(Player.Max_Health) + ' Mana = ' + str(Player.Mana) + '/' + str(Player.Max_Mana) + ' Mana Regen = ' + str(Player.Mana_Bonus) + ' Damage = ' + str(Player.Damage) + ' Damage Bonus = ' + str(Player.Damage_Bonus) + ' Crit Chance = ' + str(Player.Crit_Chance) + ' Defense = ' + str(Player.Defense) + ' Speed = ' + str(Player.Speed) + ' Ability Cooldown = ' + str(Player.Ability_On_CoolDown), Text_Time)


#DO THIS LATER OR NOW ^^^ 
                elif Place_Choice == 2:
                    Level_Up(Text_Time)

                elif Place_Choice == 3:
                    Encounter = random.randint(1,30)
                    if Encounter <= 5:
                        Text_Scroll_Effect('You found nothing',Text_Time)
                        Trader = False
                    elif Encounter <= 10 and Encounter > 5:
                        if Trader == True:
                            Text_Scroll_Effect('You found a merchant open to trading',Text_Time)
                            Choices_Text = '4. Merchant'
                        else:
                            Text_Scroll_Effect('You didnt find anything',Text_Time)
                    elif Encounter <= 30 and Encounter > 10:
                        Text_Scroll_Effect('You see Movement and prepare for a fight', Text_Time)
                        Confirmation()
                        Fight_Encounter = random.randint(1,1)
                        if Campaign == 1:
                            if Area == 1:
                                if Town == 'Nightengale':
                                    if Fight_Encounter == 1:
                                        Enemy = Wolf()
                                elif Town == 'TownTwo':
                                    if Fight_Encounter == 1:
                                        Enemy = Wolf()
                                elif Town == 'Holden':
                                    if Fight_Encounter == 1:
                                        Enemy = Wolf()
                                elif Town == 'Cobalt':
                                    if Fight_Encounter == 1:
                                        Enemy = Wolf()
                                elif Town == 'Walden':
                                    if Fight_Encounter == 1:
                                        Enemy = Wolf()
                        Enemy_Effects = Status_Effects()
                        Combat_Normal(Text_Time)

                elif Place_Choice == 4 and Choices_Text == '4. Merchant':
                    Text_Scroll_Effect('You got no money so why bother even coming here? idiot fr', Text_Time)
            if Area == 2:
                Midway = data.Maps(2)
            elif Area == 3:
                EndGame = data.Maps(3)
        


#quit
    elif Menu_Choice == 2:
        break

Clear_Terminal()
Text_Scroll_Effect('Saving data DO NOT QUIT', Text_Time)
with open('data.py', 'r') as f:
    lines = f.read().split('\n')
    new_line = '    Unlocked = ' + str(Character_Unlocks)
    new_file = '\n'.join(lines[:5] + [new_line] + lines[6:])
with open('data.py', 'w') as f:
    f.write(new_file)

with open('data.py', 'r') as f:
    lines = f.read().split('\n')
    new_line = '    Max_Health = ' + str(Player.Max_Health) + '\n    Health = ' + str(Player.Health) + '\n    Damage = ' + str(Player.Damage) + '\n    Damage_Bonus = ' + str(Player.Damage_Bonus) + '\n    Crit_Chance = ' + str(Player.Crit_Chance) + '\n    Defense = ' + str(Player.Defense) + '\n    Max_Mana = ' + str(Player.Max_Mana) + '\n    Mana = ' + str(Player.Mana) + '\n    Mana_Bonus = ' + str(Player.Mana_Bonus) + '\n    Speed = ' + str(Player.Speed) + '\n    Ability = "' + Player.Ability + '"\n    Passive = "' + Player.Passive + '"\n    Armor = ' + str(Player.Armor) + '\n    Weapon = ' + str(Player.Weapon) + '\n    Money = ' + str(Player.Money) + '\n    Level = ' + str(Player.Level) + '\n    Experience = ' + str(Player.Experience)
    new_file = '\n'.join(lines[:9] + [new_line] + lines[26:])
with open('data.py', 'w') as f:
    f.write(new_file)
Text_Scroll_Effect('...', 1)
print('Something went wrong or you quit')
