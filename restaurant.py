class Restaurant:
    def __init__(self, restaurant_name,  cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    
    def describe_restaurant(self):
        print(f'Nome do restaurante {self.restaurant_name}')
        print(f'Tipo de cozinha: {self.cuisine_type}')
        print(f'Numero servido: {self.number_served}')
    
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    
    def open_restaurant(self):
        print('O restaurante está aberto')


restaurante = Restaurant('Cozinha lá de casa', 'Caseira')
restaurante.describe_restaurant()
restaurante.open_restaurant()
restaurante.set_number_served(3)
restaurante.describe_restaurant()
