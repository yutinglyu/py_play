# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:56:54 2019
    Three Face Game
    游戏人数：4（一庄三闲）
    游戏规则：1.切牌逆时针选庄；
             2.庄家切牌，选择第一个抽牌的玩家；
             3.下注；
             4.逆时针抽牌，每人一次性抽三张；
             5.亮牌，分别与庄家进行比较（赢、输、平）,结算；
             6.选出牌型最大的玩家切牌，选择第一个抽牌的玩家；
             7.将玩家手中卡牌和下注金额归零
             8.从第3步重新开始。
             9.两副牌以后换庄，所有人都做过一次庄为一轮。
    比较大小：1.两鬼13，6倍
             2.大三公12，6倍
             3.混三公11，4倍
             4.9点，3倍
             5.8点，2倍
             6.765432点，1倍
             6.0点、1点平则庄家赢
@author: user
"""
import random

class Comparator:
    @staticmethod
    def compare_cards(bookmaker_cards, oppo_cards):
        bookmaker_result = Comparator.give_rank(bookmaker_cards)
        oppo_result = Comparator.give_rank(oppo_cards)
        if bookmaker_result[0] > oppo_result[0]:
            return ('win', bookmaker_result[1])
        elif bookmaker_result[0] < oppo_result[0]:
            return ('lose', -oppo_result[1])
        else:
            if bookmaker_result[0] == 0 or bookmaker_result[0] == 1:
                return ('win', bookmaker_result[1])
            else:
                return ('even', 0)
    
    def give_rank(card_list):
        if sum(['BJ' in x for x in card_list]) and sum(['RJ' in x for x in card_list]): # 两鬼
            return (13,6)
        elif card_list[0][1] == card_list[1][1] == card_list[2][1]: # 大三公 KKK 333
            return (12,6)
        elif ((sum(['BJ' in x for x in card_list]) + sum(['RJ' in x for x in card_list]) == 1))\
             and (card_list[0][1] == card_list[1][1] != card_list[2][1] or\
                   card_list[1][1] == card_list[2][1] != card_list[0][1] or\
                    card_list[2][1] == card_list[0][1] != card_list[1][1]): # 大三公 KKJo 33Jo
            return (12,6)
        elif (sum(['J' in x for x in card_list]) + sum(['Q' in x for x in card_list]) +\
              sum(['K' in x for x in card_list])) == 3: # 混三公 KKQ KKJ KQJ 已经排除掉了大三公
            return (11,4)
        elif (card_list[0][3] + card_list[1][3] + card_list[2][3]) % 10 == 9:
            return (9,3)
        elif (card_list[0][3] + card_list[1][3] + card_list[2][3]) % 10 == 8:
            return (8,2)
        else:
            return ((card_list[0][3] + card_list[1][3] + card_list[2][3]) % 10 ,1)
    

class Player:
    """
    定义一个玩家
    """
    def __init__(self, name, seat_index, funds, bottom_wager, 
                 is_bookmaker = False):
        self.name = name
        self.seat_index = seat_index
        self.funds = funds
        self.bottom_wager = bottom_wager
        self.is_bookmaker = is_bookmaker
    # 属性
    is_bookmaker = False
    name = ''
    seat_index = 0
    funds = 0
    bottom_wager = 0
    self_cards = []   
    wager = 0
    # 自我评估手牌大小，下注
    def put_wager(self):
        self.wager = self.bottom_wager
        return self.wager
    # 切牌
    def cut_card(self, pokerDealer_obj):
        choosed_number = random.sample(pokerDealer_obj.card_list, 1)[0][2]
        return (self.seat_index + choosed_number) % pokerDealer_obj.number_of_player    
    
class PokerDealer:
    """
    定义一个发牌器
    """    
    def __init__(self, seats_order, number_of_player = 4,
                 if_joker = True):
        suits = sorted(['spade','heart','diamond','club']*13)
        ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.card_list = list(zip(suits*13,ranks*4,list(range(1,14))*4,(list(range(1,10))+[0]*4)*4))
        self.seats_order = seats_order
        self.bookmaker_name = seats_order[0]
        if if_joker:
            self.card_list.append(('Black_Joker','BJ',0,0))
            self.card_list.append(('Red_Joker','RJ',0,0))   
    # 属性
    if_joker = True
    number_of_player = 4
    card_list = []
    seats_order = []
    bookmaker_name = ''
    bookmaker_index = 0
    rank_list = []
    # 重置牌池
    def reset_card_list(self):
        suits = sorted(['spade','heart','diamond','club']*13)
        ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.card_list = list(zip(suits*13,ranks*4,list(range(1,14))*4,(list(range(1,10))+[0]*4)*4))
        if self.if_joker:
            self.card_list.append(('Black_Joker','BJ',0,0))
            self.card_list.append(('Red_Joker','RJ',0,0)) 
    # 切牌选庄
    def choose_bookmaker(self):
        choosed_start_seat = random.randint(0, self.number_of_player-1)
        choosed_number = random.sample(self.card_list, 1)[0][2]
        bm_index = (choosed_start_seat + choosed_number) % self.number_of_player
        bm_name = self.seats_order[bm_index]
        return (bm_name, bm_index)
    # 发牌
    def distribute_cards(self):
        if len(self.card_list) < 3 * self.number_of_player:
            return []
        drawn_cards_list = random.sample(self.card_list, 3 * self.number_of_player)
        self.card_list = [x for x in self.card_list if x not in drawn_cards_list]
        return [drawn_cards_list[i:i+3] for i in range(0,len(drawn_cards_list),3)]

    # 二人结算
    def deal_2player(self, bookmaker_obj, oppo_player_obj):
        bookmaker_result = Comparator.compare_cards(bookmaker_obj.self_cards, 
                                                    oppo_player_obj.self_cards)
        bookmaker_obj.funds += oppo_player_obj.wager * bookmaker_result[1]
        oppo_player_obj.funds -= oppo_player_obj.wager * bookmaker_result[1]


def main():
    how_many_packs = 2
    player1 = Player('Tim', 0, 100, 5)
    player2 = Player('Zhu', 1, 100, 5)
    player3 = Player('Lin', 2, 100, 5)
    player4 = Player('Hui', 3, 100, 5)
    player_list = [player1, player2, player3, player4]
    pokerDealer = PokerDealer([player1.name, player2.name, player3.name,
                               player4.name]) # 实例化发牌器
    for i in range(pokerDealer.number_of_player):
        print(player_list[i].name, player_list[i].funds)
    print('\n')
    # 1.切牌逆时针选庄；
    first_bookmaker_info = pokerDealer.choose_bookmaker()
    pokerDealer.bookmaker_name = first_bookmaker_info[0]
    pokerDealer.bookmaker_index = first_bookmaker_info[1]
    player_list[first_bookmaker_info[1]].is_bookmaker = True
    # 轮庄循环
    for bookmaker_change in range(pokerDealer.number_of_player):        
        if bookmaker_change != 0:
            pokerDealer.bookmaker_index = (first_bookmaker_info[1] + bookmaker_change)\
                                            % pokerDealer.number_of_player
            pokerDealer.bookmaker_name = player_list[pokerDealer.bookmaker_index].name
            for i in range(pokerDealer.number_of_player):
                player_list[i].is_bookmaker = False
            player_list[pokerDealer.bookmaker_index].is_bookmaker = True
            
        print(pokerDealer.bookmaker_name)
        # 2.庄家切牌，选择第一个抽牌的玩家；
        first_draw_index = player_list[pokerDealer.bookmaker_index].cut_card(pokerDealer)  
        for which_pack in range(how_many_packs):
            pokerDealer.reset_card_list() # 洗牌
            # 一副牌循环   
            while len(pokerDealer.card_list) >= 3 * pokerDealer.number_of_player:
                # 3.下注；
                for i in range(pokerDealer.number_of_player):
                    final_i = (first_draw_index + i) % pokerDealer.number_of_player
                    player_list[final_i].put_wager()
                # 4.逆时针抽牌，每人一次性抽三张；
                drawn_cards = pokerDealer.distribute_cards()
                for i in range(pokerDealer.number_of_player):
                    final_i = (first_draw_index + i) % pokerDealer.number_of_player
                    player_list[final_i].self_cards = drawn_cards[i]
                # 5.亮牌，分别与庄家进行比较（赢、输、平）,结算；
                for i in range(pokerDealer.number_of_player):
                    if i != pokerDealer.bookmaker_index:
                        pokerDealer.deal_2player(player_list[pokerDealer.bookmaker_index], 
                                                 player_list[i])
                    pokerDealer.rank_list.append(Comparator.give_rank(player_list[i].self_cards))
                # 6.选出牌型最大的玩家切牌，选择第一个抽牌的玩家；
                first_draw_index = pokerDealer.bookmaker_index
                max_rank = pokerDealer.rank_list[pokerDealer.bookmaker_index]
                for i in range(pokerDealer.number_of_player - 1): 
                    final_i = (pokerDealer.bookmaker_index + i + 1) % pokerDealer.number_of_player
                    if max_rank < pokerDealer.rank_list[final_i]:
                        first_draw_index = final_i
                        max_rank = pokerDealer.rank_list[final_i]
                # 7.将玩家手中卡牌和下注金额归零
                for i in range(pokerDealer.number_of_player): 
                    player_list[i].self_cards = []
                    player_list[i].wager = 0
                    print(player_list[i].name, player_list[i].funds)#
                pokerDealer.rank_list = []
                print('\n')#
    

    
    
    
    
    

if __name__ == '__main__':
    main()


#    print(pokerDealer.bookmaker_name)
#    for i in range(pokerDealer.number_of_player):
#        print(player_list[i].name, player_list[i].funds, player_list[i].wager, 
#              player_list[i].self_cards)

#    for i in range(pokerDealer.number_of_player):
#        print(player_list[i].name, player_list[i].funds, player_list[i].wager)
    


















