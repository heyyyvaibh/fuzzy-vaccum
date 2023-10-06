import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
# Input variables
dirtiness = ctrl.Antecedent(np.arange(0, 11, 1), 'dirtiness')
distance_from_Surface = ctrl.Antecedent(np.arange(0, 11, 1), 'distance_from_Surface')
# Output variable
speed = ctrl.Consequent(np.arange(0, 11, 1), 'speed')
# Membership functions
dirtiness.automf(3)
distance_from_Surface.automf(3) # Corrected variable name here
# Custom membership functions for speed
speed['slow'] = fuzz.trimf(speed.universe, [0, 0, 5])
speed['medium'] = fuzz.trimf(speed.universe, [0, 5, 10])
speed['fast'] = fuzz.trimf(speed.universe, [5, 10, 10])
# Fuzzy rules
rule1 = ctrl.Rule(dirtiness['poor'] & distance_from_Surface['poor'], speed['slow']) #
Corrected variable name here
rule2 = ctrl.Rule(dirtiness['average'] & distance_from_Surface['average'], speed['medium']) #
Corrected variable name here
rule3 = ctrl.Rule(dirtiness['good'] & distance_from_Surface['good'], speed['fast']) #
Corrected variable name here
# Control system
speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
vacuum_cleaner = ctrl.ControlSystemSimulation(speed_ctrl)
# Take input from the user for dirtiness level
while True:
try:
dirtiness_level = int(input("Enter the dirtiness level (from 1 to 10): "))
if 1 <= dirtiness_level <= 10:
break
else:
print("Please enter a valid number between 1 and 10.")
except ValueError:
print("Invalid input. Please enter a valid number.")
# Take input from the user for distance from surface
while True:
try:
distance_from_surface_level = int(input("Enter the distance from surface (from 1 to 10):
"))
if 1 <= distance_from_surface_level <= 10:
break
else:
print("Please enter a valid number between 1 and 10.")
except ValueError:
print("Invalid input. Please enter a valid number.")
# Set inputs and compute
vacuum_cleaner.input['dirtiness'] = dirtiness_level
vacuum_cleaner.input['distance_from_Surface'] = distance_from_surface_level # #Corrected
variable name here
vacuum_cleaner.compute()
# Print the results
print("Vacuum Cleaner Speed:", vacuum_cleaner.output['speed'])
