import random
import matplotlib
import matplotlib.pyplot as plt

def give_the_number():
    number=random.randint(1,100)
    
    if number <= 51:
#        print(number,'the number is 1-50. You lose. Play\
# again.')
        return False
    else:
#        print(number,'the number is 51-100. You win. Play more to\
# become Gaofushuai')
        return True

#x=0
#while x<100:
#    result=give_the_number()
#    print(result)
#    x+=1

def a_smart_fool(funds,initial_wager,game_count):
    wager=initial_wager
    x=[]
    y=[]
    current_game_count=1
    previous_game='win'
    previous_game_wager=initial_wager
    
    while current_game_count <= game_count:
        
        if previous_game=='win':
            
            if give_the_number():
                funds+=wager
            else:
                funds-=wager
                previous_game='lose'
                previous_game_wager=wager
                
        elif previous_game=='lose':
                
            if give_the_number():
                wager=previous_game_wager*2
                funds+=wager
                previous_game='win'
                wager=initial_wager
            else:
                wager=previous_game_wager*2
                funds-=wager
                previous_game_wager=wager
                if funds <= 0:
                    break
                
        x.append(current_game_count)
        y.append(funds)
        
        
        current_game_count+=1
    
    plt.plot(x,y)

n=0
while n < 100:
    a_smart_fool(10000,1000,100)
    n+=1
plt.xlabel('How many games does the fool played')
plt.ylabel('Funds')
plt.show()



















    
#def a_fool(funds,wager,game_count):
#    current_game_count=0
#    x=[]
#    y=[]
#    
#    while current_game_count < game_count:
#        if give_the_number():
#            funds+=wager
#        else:
#            funds-=wager
#        x.append(current_game_count+1)
#        y.append(funds)
##        if funds < 0:
##            funds='Pennyless' 
##            break
#        current_game_count+=1
#    plt.plot(x,y)
# 
##    print('How rich the fool is:', funds)
#
#n=0
#while n < 1000:
#    a_fool(1000000,100000,100)
#    n+=1
#plt.show()