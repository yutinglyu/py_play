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


class Player:
    """
    定义一个玩家
    """
    def __init__(self, funds, bottom_wager, is_bookmaker = False):
        self.funds = funds
        self.bottom_wager = bottom_wager
        self.is_bookmaker = is_bookmaker
    # 属性
    is_bookmaker = False
    funds = 0
    bottom_wager = 0
    card_list = []    
    # 自我评估手牌大小
    def assess_cards():
        pass    
    # 下注
    def put_wager():
        pass
    # 切牌
    def cut_card():
        pass
    
    
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
        if if_joker:
            self.card_list.append(('Black_Joker',0))
            self.card_list.append(('Red_Joker',0))   
    # 属性
    if_joker = True
    number_of_player = 4
    card_list = []
    seats_order = []
    bookmaker_index = 0
    # 切牌选庄
    def choose_bookmaker(self):
        
        pass
    # 发牌
    def distribute_cards():
        pass    
    #　比较
    def compare_cards(self_cards, oppo_cards):
        return True    
    # 二人结算
    def deal_2player():
        pass    
    # 4人结算
    def deal_4player():
        pass



def main():
    pokerDealer = PokerDealer(['Tim','Zhu','Lin','Hui'])
    pokerDealer.choose_bookmaker()
    print(pokerDealer.bookmaker_index)
    
    print(pokerDealer.card_list.index(('spade_6', 6)))
    
    
    

if __name__ == '__main__':
    main()























