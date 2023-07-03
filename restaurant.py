class Restaurant:
    def __init__(self, restaurant_name,  cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    
    def describe_restaurant(self):
        print(f'Nome do restaurante {self.restaurant_name}')
        print(f'Tipo de cozinha: {self.cuisine_type}')
    
    
    def open_restaurant(self):
        print('O restaurante está aberto')


restaurante = Restaurant('Cozinha lá de casa', 'Caseira')
restaurante.describe_restaurant()
restaurante.open_restaurant()