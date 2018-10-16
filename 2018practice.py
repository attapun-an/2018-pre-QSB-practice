print("helllo world")

# markdown is for formating text 

def main():
    string = "i this is a test"
    test = checkupper(string)
    if test: 
        print("the first letter is upper case")
    else:
        try: 
            x = int(string[0])
            print("the first character is a number")
        except ValueError:
            print("the first letter is lower case")
    num = userinput()
    
        
    

def checkupper(string):
    return string[0].isupper()

def userinput():
    invalid = True
    while invalid:
        try:
            num = int(input("please input a number"))
            if num > 0:
                invalid = False
            else:
                print("please enter a value above 0")
        except ValueError:
            print("please input a number")
            

class Animal:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    
    def grow(self):
        self.height +=1
        self.weight +=1
        
    def givedata(self):
        return {'height':self.height, 'weight': self.weight}
    

animal1 = Animal(2, 4)
animal1.grow()
data = animal1.givedata()
print(data)
print(data["height"])

def array_test():
    array = []
    for i in range(0,13):
        array.append("")
    
    
    premade_data = [23, 32, 32, 21, 15, 64, 435, 54, 54, 645, 6456, 876, 34]
    for i in range(len(premade_data)):
        array[i] = premade_data[i]
    
    
    array = []
    for i in premade_data:
        array.append(i)
    print(array)
    
