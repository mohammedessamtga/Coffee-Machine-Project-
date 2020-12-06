# Write your code here
class Machine : 
    def __init__(self, water=400, milk=540, coffee_beans=120, disposable_cups=9, money = 550):
        self.water = water
        self.milk  = milk 
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money
        
    def status(self):
     print("The coffee machine has:")
     print(str(self.water)+" of water")
     print(str(self.milk)+" of milk")
     print(str(self.coffee_beans)+" of coffee beans")
     print(str(self.disposable_cups)+" of disposable cups")
     print(str(self.money)+" of money")
     return 
    def take(self):
        print("I gave you $"+str(self.money))
        self.money=0
        return  
    def fill(self,water,money,coffee,milk,cups):
        self.water += water 
        self.money += money 
        self.coffee_beans += coffee 
        self.milk += milk 
        self.disposable_cups += cups 
        return 
    def handle_input(self,str_input,choice='',water=0,milk=0,coffee=0,cups=0):
        if str_input == 'remaining':
            self.status()   
        elif str_input =='buy':
            try:
               choice = int(choice)
            except ValueError:
               return (self.water,self.money,self.coffee_beans,self.milk,self.disposable_cups)
            self.buy(choice)  
        elif str_input =='take':
            self.take()
        elif str_input =='fill' :  
            self.fill(water,0,coffee,milk,cups)
        
    def buy(self,choice): 
        if choice == 1 : 
            if self.water > 249 and self.coffee_beans > 15 and self.disposable_cups > 0 : 
               self.water-=250
               self.coffee_beans-=16
               self.money+=4
               self.disposable_cups-=1
            else :
                txt = ''
                if self.water <= 249 : 
                    txt='water'
                elif self.coffee_beans <=15 : 
                    txt = 'coffee beans'
                elif self.disposable_cups == 0 : 
                    txt = 'disposable cups'
                print('Sorry, not enough {}!'.format(txt))
                           
        elif choice==2:
            if self.water > 349 and self.milk > 74 and self.coffee_beans > 19 and self.disposable_cups > 0 :
               self.water-=350 
               self.milk-=75
               self.coffee_beans-=20
               self.money+=7
               self.disposable_cups-=1
            else :
                txt = ' '
                if self.water <= 349 : 
                    txt='water'
                elif self.coffee_beans <=19 : 
                    txt = 'coffee beans'
                elif self.milk <=74 : 
                    txt = 'milk'
                elif self.disposable_cups == 0 : 
                    txt = 'disposable cups'
                print('Sorry, not enough {}!'.format(txt))
        elif choice == 3:
            if self.water > 199 and self.milk > 99 and self.coffee_beans > 11 and self.disposable_cups > 0 : 
               self.water-=200
               self.milk -=100
               self.coffee_beans-=12
               self.money+=6
               self.disposable_cups-=1
            else :
                txt = ''
                if self.water <= 199 : 
                    txt='water'
                elif self.coffee_beans <=11 : 
                    txt = 'coffee beans'
                elif self.milk <=99 : 
                    txt = 'milk'
                elif self.disposable_cups == 0 : 
                    txt = 'disposable cups'
                print('Sorry, not enough {}!'.format(txt))
        return
   




machine = Machine()
while(True):
    str_input = input("Write action (buy, fill, take, remaining, exit):")
    if str_input =="exit": 
        break
    elif str_input == 'buy':
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if choice != 'back' :
            machine.handle_input(str_input,choice)
    elif str_input == 'fill':
        tmp = []
        tmp.append(int(input("Write how many ml of water do you want to add:")))
        tmp.append(int(input("Write how many ml of milk do you want to add:")))
        tmp.append(int(input("Write how many grams of coffee do you want to add:")))
        tmp.append(int(input("Write how many disposable cups of coffee do you want to add:")))
        machine.handle_input(str_input,tmp[0],tmp[1],tmp[2],tmp[3])
        
        
    else : 
        machine.handle_input(str_input)
    
        
        
    