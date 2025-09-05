# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 20:05:56 2025

@author: miso4
"""

#문자열 개수를 세는 알고리즘_문자열에서 a의 개수를 출력하시오.
string = "There is an apple in the table."

def countA(String):
    count = 0
    for i in String:
        if(i == 'a'):
            count += 1
    return count

#print(countA(string))
'''
최악의 시간 복잡도는?
for문이 N만큼 반복됨 
따라서 O(N)
'''

#선택 정렬_N개의 숫자를 저장한 리스트를 내림차순으로 정렬하시오
'''
최댓값 또는 최솟값을 정하여 오름차순 또는 내림차순으로 정렬하는 알고리즘
'''
list = [3, 2, 7, 1, 5]
def selection_sort(list):
    sorted_arr = []
    while list :
        max_arr = list[0]
        for i in range(len(list)):
           if(max_arr < list[i]):
               max_arr = list[i]
        sorted_arr.append(max_arr)    
        list.remove(max_arr)
    return sorted_arr

#print(selection_sort(list))
'''
while이 n번 있는 동안 for 문이 n, n-1, n-2, ... 둘이 더하면 n(n+1)/2만큼 반복 
따라서 시간복잡도는 O(N^2)
'''
            
#최근접 거리_2차원 평면상에 n개의 점이 있다. 가장 인접한 쌍의 거리를 구하라
points=[((2,3), (3,5), (8,10), (11,-1))]
def calc_dist(p1,p2):
    x_dist = (p1[0] - p2[0])**2
    y_dist = (p1[1] - p2[1])**2
    dist = (x_dist + y_dist) **0.5
    return dist

def min_dist(points):
    min = float("inf")
    for i in range (len(points)-1):
       for j in range (i+1, len(points)):
           dist = calc_dist(points[i], points[j])
           if (dist < min):
               min = dist
    return min            
               
