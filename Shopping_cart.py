# -*- coding: utf-8 -*-
"""
Created on Wed May  1 08:30:20 2024

@author:Madhu
"""
class Shopping_cart:
    
    List1=[]
    def add_items(self,item):
        self.List1.append(item)
        print("+Item added to cart",item)
    def remove_item(self,target):
        if target in self.List1:
            self.List1.remove(target)
            print("-successfully deleted item=",target)
        else:
            print("Item not present in Cart")
        
    def display(self):
        if self.List1 is None:
            print("Cart is Empty")
        else:
            print("\nItems present in Cart.")
            for items in self.List1:
                print("->",items)
    def Buy(self,target):
        if target in self.List1:
            print("\n",target,"-successfully purchased")
            self.List1.remove(target)
            
        
        
sc=Shopping_cart()
sc.add_items("Apple plant-$120")
sc.add_items("Mango plant-$35")
sc.add_items("cherry plant-$90")
sc.add_items("Banana plant-$20")
sc.display()
sc.Buy("Apple plant-$120")
sc.remove_item("Banana plant-$20")
sc.display()


                
        