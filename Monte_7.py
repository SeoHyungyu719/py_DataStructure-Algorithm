# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 19:58:00 2025

@author: miso4
"""

#주사위 확률
'''
Q. 주사위를 굴렀을 떄 1이 나올 확률은?

randomness에 기반
-해당 시뮬레이션을 충분히 많이 반복하고 1이 나온 회수를 계수한다
- (1이 나온 횟수) / (전체 시도 회수)를 1이 나올 확률로 추정한다.
'''
import random
import math

def rollDice():
    num = random.randint(1, 6) # 1에서 6사이 정수를 생성
    return num

def callDiceProb(tries, target):
    count = 0
    for i in range(tries):
        num = rollDice()
        if(num == target):
            count += 1
            
    return (count/tries)
 

#원주율 문제
'''
한변이 2인 정사각형안에 내접한 원의 반지름이 1인 원이 있다
원의 너비 는 pi. 즉, 정사각형에 내접한 반지름1의 너비는 원주율과 같다.

시간복잡도의 경우 for문이 N번만큼 반복되므로 O(N)이다
'''
def calPI(tries):
    insideCnt = 0
    for i in range(tries):
        x = random.random()
        y = random.random()
        dist = math.sqrt((x*x)+(y*y))
        if dist <= 1:
            insideCnt += 1
            
    return (4*(insideCnt/tries))
            

#적분
'''
y= x*x의 그래프에서 0~1까지 범위의 경우 
0 부터 1 이하인 점의 수만큼 더하면 해당 그래프의 너비가 나온다.

'''

def callIntergral(tries):
    insideCnt = 0
    for i in range(tries):
        x = random.random()
        y = random.random()
        if(y <= x*x):
            insideCnt += 1
    return (insideCnt/tries)

#몬테카를로 시뮬레이션을 적용한 knapsack 문제
'''
- 각 아이템의 포함 여부를 임의로 결정한다. (random 함수 활용)
- 단, 아이템을 포함했을 시, 최대 허용 무게를 초과하면 해당 아이템은 무조건 포함하지 않는다
-임의로 결정하므로 한 번만 시도해서는 최적값을 구할 수 없다.
-따라서 이러한 시뮬레이션을 충분히 많이 수행하고 그 중에서 최적의 케이스를 최적값으로 간주한다.
'''

class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

class Knapsack(object):
    def __init__(self, names, values, weights, max_weight):
        self.items = []
        self.max_weight = max_weight
        for i in range(len(names)):
            item = Item(names[i], values[i], weights[i])
            self.items.append(item)


    def findBestCaseMontecarlo(self, tries):
        max_value = 0
        best_chosen_items = []
        best_weight = 0
        
        for i in range(tries):
            (value, weight, chosen_items) = self.select_item()
            if(value > max_value):
                max_value = value
                best_weight = weight
                best_chosen_items = list(chosen_items)
                
            return (max_value, best_chosen_items, best_weight)
        
    def select_item(self):
        value = 0
        weight = 0
        chosen_items = []
        
        for item in self.items:
            if(weight + item.weight <= self.max_weight):
                roll = random.randint(1, 100)
                if(roll % 2 == 0):
                    chosen_items.append(item.name)
                    weight += item.weight
                    value += item.value
                    
        return (value, weight, chosen_items)
            