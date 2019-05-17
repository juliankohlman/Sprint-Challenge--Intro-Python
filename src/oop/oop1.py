# Write classes for the following class hierarchy:
#
class Vehicle:
  #base vehicle class
  pass

class FlightVehicle(Vehicle):
  pass

class Starship(FlightVehicle):
  pass
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
class GroundVehicle(Vehicle):
  pass

class Car(GroundVehicle):
  pass

class Motorcycle(GroundVehicle):
  pass

class Airplane(FlightVehicle):
  pass
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
