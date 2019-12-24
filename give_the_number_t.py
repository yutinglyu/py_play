import random
import matplotlib.pyplot as plt
 
 
def give_the_number():
    roll = random.randint(1,100)
 
    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True
 
 
def a_smart_fool(funds,initial_wager,game_count):
    wager = initial_wager
    x = []
    y = []
    current_game_count = 1
 
    previous_game = 'win'
    previous_game_wager = initial_wager
 
    while current_game_count <= game_count:
        if previous_game == 'win':
            print('The fool win the last game˜yeah˜˜˜')
            if give_the_number():
                funds += wager
                print(funds)
                x.append(current_game_count)
                y.append(funds)
            else:
                funds -= wager  
                previous_game = 'loss'
                print(funds)
                previous_game_wager = wager
                x.append(current_game_count)
                y.append(funds)
                if funds < 0:
                    print ('The fool went broke in'+
                           str(current_game_count)+'games')
                    break
                 
        elif previous_game == 'loss':
            print("we lost the last one, but the fool will double up˜")
            if give_the_number():
                wager = previous_game_wager * 2
                print ('we won'+str(wager))
                funds += wager
                print (funds)
                wager = initial_wager
                previous_game = 'win'
                x.append(current_game_count)
                y.append(funds)
            else:
                wager = previous_game_wager * 2
                print ('we lost'+str(wager))
                funds -= wager
                if funds < 0:
                    print('The fool went broke in'
                          +str(current_game_count)+'games')
                    break
                print(funds)
                previous_game = 'loss'
                previous_game_wager = wager
                x.append(current_game_count)
                y.append(funds)
                if funds < 0:
                    print('went broke aftesr'+str(current_game_count)+'bets')
                    break
 
        current_game_count += 1
 
    print(funds)
    plt.plot(x,y)
 
 
n=0
while n<10:
    a_smart_fool(10000,1000,100)
    n+=1
 
 
 
plt.xlabel("How many games does the fool played")
plt.ylabel("Funds")
plt.show()