


from carr import PetrolCar, DieselCar, ElectricCar, HybridCar




print 'Welcome to Aungier Car rental - we have 40 cars available in a wide variety of makes'

class Dealership(object):

    def __init__(self):
		self.petrol_cars = []
		self.diesel_cars = []
		self.electric_cars = []        
		self.hybrid_cars = []

    def create_current_stock(self):
	for i in range(20):
		self.petrol_cars.append(PetrolCar())
	for i in range(8):
		self.diesel_cars.append(DieselCar())
	for i in range(4):
		self.electric_cars.append(ElectricCar())
	for i in range(8):
		self.hybrid_cars.append(HybridCar())
		   
		   
    def stock_count(self):
	print 'petrol cars in stock ' + str(len(self.petrol_cars))
	print 'diesel cars in stock ' + str(len(self.diesel_cars))
	print 'electric cars in stock ' + str(len(self.electric_cars))
	print 'hybrid cars in stock ' + str(len(self.hybrid_cars))
		
		
    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print 'Sorry nothing to rent please try again'
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1
		   
    def return_item(self, car_list, amount):
        if len(car_list) < amount:
            print 'Sorry nothing to rent please try again'
            return
        total = 0
        while total < amount:
			if car_list == self.petrol_cars
				self.petrol_cars.append(PetrolCar())
			else 'no car list'
			total = total + 1		   

    def process_rental(self):
        answer = raw_input('would you like to rent a car? y/n')
        if answer == 'y':
            answer = raw_input('what type would you like? P/D/E/H')
            amount = int(raw_input('how many would you like?'))
            if answer == 'P':
                self.rent(self.petrol_cars, amount)
            elif answer == 'D':
                self.rent(self.diesel_cars, amount)
            elif answer == 'E':
                self.rent(self.electric_cars, amount)	
            elif answer == 'H':
                self.rent(self.hybrid_cars, amount)					
            else:
				print 'should not get here'
		else 
		    answer = raw_input('would you like to return a car')
	        if answer == 'y':
				answer = raw_input('what type would you like? P/D/E/H')
				amount = int(raw_input('how many would you like?'))
				if answer == 'P':
					self.return_item(self.petrol_cars, amount)				
				else:
					print 'should not get here'
        self.stock_count()

dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('continue? y/n')

dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('continue? y/n')