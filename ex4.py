# assigns the value of 100 to "cars"
cars = 100
# assigns the value of 4.0 as a floating number to space_in_a_car
space_in_a_car = 4.0
# assigns the value 30 to drivers
drivers = 30
# assigns the value 90 to the variable passengers
passengers = 90
# assigns the variable cars_not_driven a value of the solution to cars - drivers
cars_not_driven = cars - drivers
# assigns the variable cars_driven to the value of drivers which is assigned the value of 30.
cars_driven = drivers
# assigns the variable carpool_capacity the value of the solution of the equation cars_driven multiplied by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# assigns the variable average_passengers_per_car the value of the solution of the equation passengers divded by cars_driven.
average_passengers_per_car = passengers / cars_driven

# this will print "there are" 100 "cars available" becuase we set the variable "cars" to 100 above.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
# Study notes:  Car_pool_capacity is not defined means that you did not give a value to that variable for the program to solve it.  It happened to me with "cars" becuase I had it capitalized instead of lowercase.
# If you drop the .0 from 4 in space_in_a_car then it removes the .0 from 120 when the program solves carpool_capacity.  This is called a floating point number (a number with a decimal point)
