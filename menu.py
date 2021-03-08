import pickle

class Menu():
    def __init__(self,name,price,info="",category="Pizza"):
        self.id = self.getId('.\pkl\menus.pkl')
        self.name = name
        self.price = price
        self.info = info
        self.category = category

    def saveMenu(self):
        print(self)
        with open('.\pkl\menus.pkl','ab') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

    def getId(self,filename):
        length = 0
        try:
            with open(filename,'rb') as output:
                while True:
                    try:
                        pickle.load(output)
                        length += 1
                    except EOFError:
                        break
        except FileNotFoundError:
            return 1
        return length+1

    def loadMenu():
        # list container of all menus
        menuLoaded = []

        # load all objects in pkl\menus.pkl
        with open('.\pkl\menus.pkl','rb') as input:
            while True:
                try:
                    menu = pickle.load(input)
                    menu.id = "P" + str(menu.id)
                except EOFError:
                    break
                menuLoaded.append(menu)

        # load all objects in ./pkl/toppings.pkl
        with open('./pkl/toppings.pkl','rb') as input:
            while True:
                try:
                    topping = pickle.load(input)
                    topping.id = "T" + str(topping.id)
                except EOFError:
                    break
                menuLoaded.append(topping)

        # load all objects in .\pkl\drinks.pkl
        with open('.\pkl\drinks.pkl','rb') as input:
            while True:
                try:
                    drink = pickle.load(input)
                    drink.id = "D" + str(drink.id)
                except EOFError:
                    break
                menuLoaded.append(drink)
                
        return menuLoaded
