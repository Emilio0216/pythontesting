#nothing
import math, time, random, sys, os, settings, data
from time import sleep
from data import Saved_Player, Knight, Archer
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
def Clear_Terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
#Main script I HATE EMILIO >:), From Ruben that you will never get my calc 
for i in range(1): #data in a range loop for space
    Character_Unlocks = data.Characters_Unlocked()
    Text_Time = settings.Text_Speed()
    Difficulty = settings.Difficulty()
    High_Score = data.High_Score()
Clear_Terminal()
Text_Scroll_Effect("Welcome to ____ as you'll come to find i'm really lazy and not very creative exactly why this 'game' doesnt have a name\nI'm not totally sure what im going for in this game so everything is subject to change", Text_Time)
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
        #Stat applying
        if Character_Select == 'knight':
            Player = Knight()
        if Character_Select == 'archer':
            Player = Archer()


        


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
    new_line = '    Max_health = ' + str(Player.Max_Health) + '\n     Health = ' + str(Player.Health) + '\n     Damage = ' + str(Player.Damage) + '\n     Damage_Bonus = ' + str(Player.Damage_Bonus) + '\n     Crit_Chance = ' + str(Player.Crit_Chance) + '\n     Defense = ' + str(Player.Defense) + '\n     Max_Mana = ' + str(Player.Max_Mana) + '\n     Mana = ' + str(Player.Mana) + '\n     Mana_Bonus = ' + str(Player.Mana_Bonus) + '\n     Speed = ' + str(Player.Speed) + '\n     Ability = ' + str(Player.Ability) + '\n     Passive = ' + str(Player.Passive) + '\n     Armor = ' + str(Player.Armor) + '\n     Weapon = ' + str(Player.Weapon) + '\n     Money = ' + str(Player.Money) + '\n     Level = ' + str(Player.Level) + '\n     Experience = ' + str(Player.Experience)
    new_file = '\n'.join(lines[:9] + [new_line] + lines[24:])
with open('data.py', 'w') as f:
    f.write(new_file)
Text_Scroll_Effect('...', 1)
print('Something went wrong or you quit')