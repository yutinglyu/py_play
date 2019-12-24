# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:56:54 2019
    Three Face Game
    游戏人数：4（一庄三闲）
    游戏规则：1.切牌逆时针选庄；
             2.庄家切牌，选择第一个抽牌的玩家；
             3.逆时针抽牌，每人一次性抽三张；
             4.个人行为：评估手牌大小，下注；
             5.亮牌，分别与庄家进行比较（赢、输、平）；
             6.结算；
             7.选出牌型最大的玩家切牌，选择第一个抽牌的玩家；
             8.从第3步重新开始。
             9.两副牌以后换庄，所有人都做过一次庄为一轮。
    比较大小：1.两鬼，6倍
             2.大三公，6倍
             3.混三公，4倍
             4.9点，3倍
             5.8点，2倍
             6.0点、1点平则庄家赢
@author: user
"""
import random


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
    def assess_put_wager(self):
        self.wager = self.bottom_wager
        return self.wager
    # 切牌
    def cut_card(self, pokerDealer_obj):
        choosed_number = random.sample(pokerDealer_obj.card_list, 1)[0][1]
        return (self.seat_index + choosed_number) % pokerDealer_obj.number_of_player    
    
class PokerDealer:
    """
    定义一个发牌器
    """    
    def __init__(self, seats_order, number_of_player = 4,
                 if_joker = True):
        suits = ['spade','heart','diamond','club']
        ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        single_cards = [(i+'_'+j) for i in suits for j in ranks]
        self.card_list = list(zip(single_cards,list(range(1,14))*4))
        self.seats_order = seats_order
        self.bookmaker_name = seats_order[0]
        if if_joker:
            self.card_list.append(('Black_Joker',0))
            self.card_list.append(('Red_Joker',0))   
    # 属性
    if_joker = True
    number_of_player = 4
    card_list = []
    seats_order = []
    bookmaker_name = ''
    bookmaker_index = 0
    # 切牌选庄
    def choose_bookmaker(self):
        choosed_start_seat = random.randint(0, self.number_of_player-1)
        choosed_number = random.sample(self.card_list, 1)[0][1]
        self.bookmaker_index = (choosed_start_seat + choosed_number) % self.number_of_player
        self.bookmaker_name = self.seats_order[self.bookmaker_index]
        return (self.bookmaker_name, self.bookmaker_index)
    # 发牌
    def distribute_cards(self):
        if len(self.card_list) < 3 * self.number_of_player:
            return []
        drawn_cards_list = random.sample(self.card_list, 3 * self.number_of_player)
        self.card_list = [x for x in self.card_list if x not in drawn_cards_list]
        return [drawn_cards_list[i:i+3] for i in range(0,len(drawn_cards_list),3)]
    #　比较
    @staticmethod
    def compare_cards(self_cards, oppo_cards):
        return 'win' 
    # 二人结算
    def deal_2player():
        pass    
    # 4人结算
    def deal_4player():
        pass



def main():
    player1 = Player('Tim', 0, 100, 2)
    player2 = Player('Zhu', 1, 100, 2)
    player3 = Player('Lin', 2, 100, 2)
    player4 = Player('Hui', 3, 100, 2)
    player_list = [player1, player2, player3, player4]
    pokerDealer = PokerDealer([player1.name, player2.name, player3.name,
                               player4.name]) # 实例化发牌器
    # 1.切牌逆时针选庄；
    bookmaker_info = pokerDealer.choose_bookmaker()
    player_list[bookmaker_info[1]].is_bookmaker = True
    # 2.庄家切牌，选择第一个抽牌的玩家；
    first_draw_index = player_list[pokerDealer.bookmaker_index].cut_card(pokerDealer)
    # 3.逆时针抽牌，每人一次性抽三张，评估手牌大小，下注；
    drawn_cards = pokerDealer.distribute_cards()
#    if drawn_cards == []:
    for i in range(pokerDealer.number_of_player):
        final_i = (first_draw_index + i) % pokerDealer.number_of_player
        player_list[final_i].self_cards = drawn_cards[i]
        player_list[final_i].assess_put_wager()
    # 5.亮牌，分别与庄家进行比较（赢、输、平）,结算；
    # 6.；
    # 7.选出牌型最大的玩家切牌，选择第一个抽牌的玩家；
    # 8.从第3步重新开始。
    # 9.两副牌以后换庄，所有人都做过一次庄为一轮。    
    
    
    
    
    

if __name__ == '__main__':
    main()























