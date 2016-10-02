# set the variiables
#
# assign cars = 100
cars = 100
# assign space_in_a_car = 4
space_in_a_car = 4

drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "cars:", cars
print "drivers:", drivers
print "cars_not_driven:", cars_not_driven
 
print " "
print "there are", cars, "cars available."
print "there are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transporti", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in every car."

print "space_in_a_car   =  ", space_in_a_car

