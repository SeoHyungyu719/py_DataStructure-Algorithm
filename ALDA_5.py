# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 21:47:35 2025

@author: miso4
"""

def merge_sort(list) :
    length = len(list)
    if(length == 1):
        return list
    start1 = 0
    start2 = length // 2
    
    list1 = list[start1 : start2]
    list2 = list[start2 : length]
    list1 = merge_sort(list1)
    list2 = merge_sort(list2)
    result = merge(list1, list2)
    return result

def merge(list1, list2):
    result = []
    while (len(list1) > 0 and len(list2) > 0):
        if(list1[0] > list2[0]):
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
            
    while (len(list1) > 0):
        result.append(list1.pop(0))
        
    while (len(list2) > 0):
        result.append(list2.pop(0))
        
        
    return result
        
            
'''
merge() 함수의 연산의 횟수가 두 리스트의 원소의 개수에 비례해서 증가한다.
merge_sort()에서 나눠 계산하므로 logn 

logn이 N에 비례해서 시간복잡도가 늘어나므로 최악의 시간 복잡도는 O(NlogN)이다
'''

def fibo(num):
    dict = {}
    return fibo_dict(num, dict)

def fibo_dict(num, dict):
    if (num == 0 or num == 1):
        return num
    if(num in dict):
        return dict[num]
    else:
        dict[num] = fibo_dict(num-1, dict) + fibo_dict(num-2,dict)
        return dict[num]
    
'''
분할 정복에서 중요한건 데이터를 중간에 저장해놓는 것이다.
이를 통해 fibo()함수의 시간복잡도는 O(n)이 나온다.

'''
    