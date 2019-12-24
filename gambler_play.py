import random
import matplotlib.pyplot as plt

def gamble_onetime():
    number = random.randint(1, 100)
    if number <= 51:
        return False
    else:
        return True

def gambler(funds, initial_wager, gambler_times):
    
    x=[]
    y=[]
    
    wager = initial_wager
    previous_game = 'win'
    previous_game_wager = initial_wager
    
    gamble_counter = 1
    while gamble_counter <= gambler_times:
        if previous_game == 'win':
            wager = initial_wager
            if gamble_onetime():
                funds += wager
#                previous_game_wager = wager
            else:
                funds -= wager
                previous_game = 'lose'
#                previous_game_wager = wager
        elif previous_game == 'lose':
            wager = previous_game_wager * 2
            if gamble_onetime():
                funds += wager
                previous_game = 'win'
                previous_game_wager = initial_wager
            else:
                funds -= wager
                previous_game_wager = wager
                if funds <= 0:
                    break
        x.append(gamble_counter)
        y.append(funds)
        gamble_counter += 1
    
    plt.plot(x,y)

gambler_num = 100
initial_funds = 10000
initial_wager = 1000
play_times = 100
for i in range(gambler_num):
    gambler(initial_funds, initial_wager,play_times)

plt.show()
        