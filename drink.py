from menu import Menu
import pickle

class Drink(Menu):
    def __init__(self,name,price,info="",category="Drink"):
        super().__init__(name,price,info,category)
        self.id = self.getId('.\pkl\drinks.pkl')


    def saveDrink(self):
        print(self)
        with open('.\pkl\drinks.pkl','ab') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
