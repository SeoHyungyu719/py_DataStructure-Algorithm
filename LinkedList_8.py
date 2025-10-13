# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 09:44:17 2025

@author: miso4
"""

class SNode:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
        
class SList:
     def __init__(self):
         self.head = None
        
    
     def insert_front(self, item):
          snode = SNode(item, self.head)
          self.head = snode
          return
  
     def print_list(self):
         p = self.head
         while p:
             if p.next != None:
                 print(p.item, '->', end='')
             else:
                 print(p.item)
             p = p.next
    
     def delete_front(self):
         first = self.head
         if first != None:
             self.head = first.next
             del(first)
         
     def search(self,item):
        if(self.head == None):
            return False
        cur = self.head
        while cur != None:
            if item == cur.item:
                return True
            cur = cur.next
        return False