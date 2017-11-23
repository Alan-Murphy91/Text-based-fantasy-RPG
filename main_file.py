import time
import random
import game_functions
from prettytable import PrettyTable


########################################################

def race_select():
    race = raw_input('What race are you? (human,elf,dwarf) \n')
    if(race == 'human'):
        return 'human'
    elif(race == 'elf'):
        return 'elf'
    elif(race == 'dwarf'):
        return 'dwarf'
    else:
        race_select()

def class_select():
    job = raw_input('What is your profession in this world? (knight,mage,thief)\n')
    if(job == 'knight'):
        return 'knight'
    elif(job == 'mage'):
        return 'mage'
    elif(job == 'thief'):
        return 'thief'
    else:
        race_select()

def buffer_time():
    print('...')
    time.sleep(1)


########################################################

class Human:
    def __init__(self):
        self.level = 1;
        self.hp = 1;
        self.mp = 1;
        self.speed = 1;
        self.accuracy = 1;
        self.defence = 1;
        self.mgkdef = 1;
        self.luck = 1;
    


########################################################

player_inventory = {
    'milk of the poppy': [2, 'Restores 50 HP'],
    'dagger': [1, 'a short blunt knife', 'unequipped'],
    'shoes': [1, 'worn shoes', 'equipped'],
    'gold': [0, 'currency used throughout Starheim'],
}


dungeon = {
                        (0,0,1): ['1',False], (1,0,1): ['2',False],                       (3,0,1): ['9',False],
                        
                        
(-1,1,1): ['3',False], (0,1,1): ['4',False], (1,1,1):['5',False], (2,1,1): ['7',False], (3,1,1): ['8',False],
                        
                                             (1,2,1):['6',False],
                        
 (-1,2,1):['13',False], (0,2,1):['12',False],                       (2,2,1):['15',False],
                        
                       (0,3,1):['11',False], (1,3,1):['10',False], (2,3,1):['14',False], (3,3,1):['15',False],
                        
                        

                                                                   (2,4,1):['17',False],(3,4,1):['16',False], (4,4,1):['18',False]
                                             
}

dungeon_items = ['milk of the poppy', random.randint(1,100), 'rusty shield', 'mana potion']

########################################################
def inventory_check():
    game_functions.buffer_time()
    x = PrettyTable(['Item Name', 'Amount', 'Item Description'])
    for key, value in player_inventory.iteritems():
        x.add_row([key,value[0],value[1]])
    print(x)

def status_check():
    game_functions.buffer_time()
    print('test')

def dungeon_move(n,s,l):
    rand = random.randint(1,9)
    if(dungeon[(n,s,l)][0] == '2'):
        game_functions.buffer_time()
        if(rand <= 3):
            print('Torchlight streams in from the west')
        elif(rand >=7):
            print('There is a corridor west of here, flickers of light illuminate the puddles')
        else:
            print('Low light and a dead end, there is a path west of here')
            
        action = raw_input('west,examine,inventory,status \n')
        if(action == 'west'):
            game_functions.buffer_time()
            print('..Moving westward, torches brighten the next area\n the air is thick with rot')
            game_functions.buffer_time()
            return dungeon_move((n-1),s,l)
        elif(action == 'examine'):
            examine(n,s,l)
            return dungeon_move(n,s,l)
        elif(action == 'inventory'):
            inventory_check()
            return dungeon_move(n,s,l)
        elif(action == 'status'):
            status_check()
            return dungeon_move(n,s,l)
        else:
            return dungeon_move(n,s,l)

    elif(dungeon[(n,s,l)][0] == '1'):
        game_functions.buffer_time()
        if(rand <= 3):
            print('To the south you hear the sound of sewers')
        elif(rand >=7):
            print('No path west, sewers south and the dark passageway to the cell east')
        else:
            print('Rats scuttle away as you enter, there is the sound \nof running sewers to the south')
            
        action = raw_input('south,east,examine,inventory,status \n')
        if(action == 'south'):
            game_functions.buffer_time()
            print('..Moving southward, a cross-bridge over sewers comes into view')
            game_functions.buffer_time()
            return dungeon_move(n,(s+1),l)
        elif(action == 'east'):
            game_functions.buffer_time()
            print('..Moving eastward, the path becomes black as night but \nfor the faint flicker of light behind you')
            game_functions.buffer_time()
            return dungeon_move((n+1),s,l)            
        elif(action == 'examine'):
            examine(n,s,l)
            return dungeon_move(n,s,l)
        elif(action == 'inventory'):
            inventory_check()
            return dungeon_move(n,s,l)
        elif(action == 'status'):
            status_check()
            return dungeon_move(n,s,l)
        else:
            return dungeon_move(n,s,l)

        

def examine(n,s,l):
    if(l == 1):
        if(dungeon[(n,s,l)][1] == True):
            print('Nothing here..')
            return dungeon_move(n,s,l)
        
        elif(dungeon[(n,s,l)][1] == False):
            dungeon[(n,s,l)][1] = True
            chance = random.randint(1,10)
            chance2 = random.randint(1,10)
            if(chance == chance2):
                select = random.randint(0,3)
                new_item = dungeon_items[select]
                if(select == 1):
                    player_inventory['gold'][0] += random.randint(1,50)
                    print('Some gold coins')
                    return dungeon_move(n,s,l)
                elif(new_item == 'milk of the poppy'):
                    if(new_item in player_inventory):
                        player_inventory[new_item][0] += 1
                        print('some milk of the poppy')
                        return dungeon_move(n,s,l)
                    else:
                        player_inventory[new_item] = [1, 'Restores 50HP']
                        print('some milk of the poppy')
                        return dungeon_move(n,s,l)
                elif(new_item == 'rusty shield'):
                    if(new_item in player_inventory):
                        player_inventory[new_item][0] += 1
                        print('a shield, albeit worse for wear')
                        return dungeon_move(n,s,l)
                    else:
                        player_inventory[new_item] = [1, 'a tattered wooden shield']
                        print('some milk of the poppy')
                        return dungeon_move(n,s,l)
                
                
            
            
    
    

########################################################


print('The year is 324 of the starlight age. \nThe kingdom of Rogdolf is under siege by the dark forces of nymerium. \nYou are a forgotten soul with an unknown destiny and have awoken \nin the dungeon cells under castle ravencroft')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
race = game_functions.race_select()
job = game_functions.class_select()
time.sleep(1)
print('...')
time.sleep(1)
final = raw_input('You are a %s and a %s. Is this correct? (y/n) \n' % (race,job))
if (final == 'n'):
    game_functions.race_select()
    game_functions.class_select()

game_functions.buffer_time()

print('You awake to a dripping noise and the sound of a rat \nscurrying across the floor. A torch illuminates the rusty iron bars of \nthe cell. The door is ajar.')
dungeon_move(1,0,1)








