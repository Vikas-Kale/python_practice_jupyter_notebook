class Mobile:
    def set_colour(self,color):
        self.color=color
    
    def set_cost(self,cost):
        self.cost=cost

    def show_colour(self):
        print(self.color)

    def show_cost(self):
        print(self.cost)

m1=Mobile()

m1.set_colour('Orange')
m1.set_cost(250)

m1.show_colour()
m1.show_cost()
