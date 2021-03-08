from menu import Menu
import pickle

class Topping(Menu):
    def __init__(self,name,price,info="",category="Topping"):
        super().__init__(name,price,info,category)
        self.id = self.getId('./pkl/toppings.pkl')


    def saveTopping(self):
        print(self)
        with open('./pkl/toppings.pkl','ab') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
