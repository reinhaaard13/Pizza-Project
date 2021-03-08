import pickle

class Store():
    def __init__(self,name,address,city):
        self.id = getId()
        # self.id = 1
        # print(self.id)
        self.name = name
        self.address = address
        self.city = city

    def saveStore(self):
        print(self)
        with open('.\pkl\stores.pkl','ab') as output:
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

    def loadStore():
        storeLoaded = []
        with open('.\pkl\stores.pkl','rb') as input:
            while True:
                try:
                    store = pickle.load(input)
                except EOFError:
                    break
                storeLoaded.append(store)
            return storeLoaded


def getId():
    # Generate ID by looking for number of objects in pkl
    length = 0

    try:
        with open('.\pkl\stores.pkl','rb') as output:
            while True:
                try:
                    pickle.load(output)
                    length += 1
                except EOFError:
                    break
    except FileNotFoundError:
        return 1
    
    return length+1
    
