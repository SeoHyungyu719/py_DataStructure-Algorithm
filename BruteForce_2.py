# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 18:15:00 2025

@author: miso4
"""

#합계를 구하는 알고리즘
def calc_sum(N):
    sum = 0;

    for num in range(1,N+1):
        sum += num;
    return sum;

#최댓값, 최솟값을 구하는 알고리즘
def max_find(list):
    max = list[0];
    for num in list:
        if(max < num) :
            max = num;
    return max;

def min_find(list):
    min = list[0];
    for num in list:
        if(min > num):
            min = num
    return min;

#약수의 갯수
def count_devisor(N):
    count = 0;
    for i in range(1,N+1):
        if(N % i == 0):
            count += 1;
    return count;


    
    

    