
from carr import PetrolCar
from carr import DieselCar
from carr import ElectricCar
from carr import HybridCar

petrol_car = PetrolCar()


print 'Make ' + petrol_car.getMake()

petrol_car.setMake('Petrol')

print 'Make ' + petrol_car.getMake()

print('Getting a paint job - the new colour is ' + petrol_car.paint('petrol green'))

print 'Colour ' + petrol_car.getColour()

print 'Engine Size ' + petrol_car.engineSize
petrol_car.engineSize = '1.2'
print 'Engine Size ' + petrol_car.engineSize

diesel_car = DieselCar()


print 'Make ' + diesel_car.getMake()

diesel_car.setMake('diesel')

print 'Make ' + diesel_car.getMake()

print('Getting a paint job - the new colour is ' + diesel_car.paint('jet Black'))

print 'Colour ' + diesel_car.getColour()

print 'Engine Size ' + diesel_car.engineSize
diesel_car.engineSize = '1.7tdi'
print 'Engine Size ' + diesel_car.engineSize

print 'Make ' + diesel_car.getMake()

electric_car = ElectricCar()
electric_car.setMake('electric')

print 'Make ' + electric_car.getMake()

print('Getting a paint job - the new colour is ' + electric_car.paint('enviromental green'))

print 'Colour ' + electric_car.getColour()

print 'Engine Size ' + electric_car.engineSize
electric_car.engineSize = '1.21 gigawatts of power'
print 'Engine Size ' + electric_car.engineSize

hybrid_car = HybridCar()
hybrid_car.setMake('hybrid')

print 'Make ' + hybrid_car.getMake()

print('Getting a paint job - the new colour is ' + hybrid_car.paint('ocean blue'))

print 'Colour ' + hybrid_car.getColour()

print 'Engine Size ' + hybrid_car.engineSize
hybrid_car.engineSize = '1.21 gigawatts of power and olive oil 1.7 tdi'
print 'Engine Size ' + hybrid_car.engineSize
