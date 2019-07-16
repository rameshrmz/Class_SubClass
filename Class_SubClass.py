class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        """ initializtion definition"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("Restaurant Name:" + self.restaurant_name)
        print("Cuisine Type:" + self.cuisine_type)
        
    def open_restaurant(self):
        print ("Restaurant " + self.restaurant_name + " is open")
  
# commented
"""       
my_restaurant = Restaurant('BBQ', 'Multi Cuisine')
my_restaurant.describe_restaurant()

friend_restaurant = Restaurant('ABS', 'Multi Cuisine')
friend_restaurant.open_restaurant()
"""

class veg_restaurant(Restaurant):
    """Inheritance - Sub class/ Child class!!!"""
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)

my_restaurant = veg_restaurant("A2B", "Multi Cuisine")
my_restaurant.describe_restaurant()