import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define the antecedents and consequents fuzzy variables
stellar_brightness = ctrl.Antecedent(np.arange(-30, 31, 1), 'stellar_brightness')
transit_depth = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'transit_depth')
exoplanet_presence = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'exoplanet_presence')

# Define the membership functions for the input variables
stellar_brightness['low'] = fuzz.trimf(stellar_brightness.universe, [-30, -30, 0])
stellar_brightness['medium'] = fuzz.trimf(stellar_brightness.universe, [-15, 0, 15])
stellar_brightness['high'] = fuzz.trimf(stellar_brightness.universe, [0, 30, 30])

transit_depth['shallow'] = fuzz.trimf(transit_depth.universe, [0, 0, 0.5])
transit_depth['moderate'] = fuzz.trimf(transit_depth.universe, [0, 0.5, 1])
transit_depth['deep'] = fuzz.trimf(transit_depth.universe, [0.5, 1, 1])

# Define the membership functions for the output variable
exoplanet_presence['low'] = fuzz.trimf(exoplanet_presence.universe, [0, 0, 0.5])
exoplanet_presence['medium'] = fuzz.trimf(exoplanet_presence.universe, [0, 0.5, 1])
exoplanet_presence['high'] = fuzz.trimf(exoplanet_presence.universe, [0.5, 1, 1])

# Define the fuzzy rules
rule1 = ctrl.Rule(stellar_brightness['low'] & transit_depth['shallow'], exoplanet_presence['low'])
rule2 = ctrl.Rule(stellar_brightness['low'] & transit_depth['moderate'], exoplanet_presence['low'])
rule3 = ctrl.Rule(stellar_brightness['low'] & transit_depth['deep'], exoplanet_presence['medium'])

rule4 = ctrl.Rule(stellar_brightness['medium'] & transit_depth['shallow'], exoplanet_presence['medium'])
rule5 = ctrl.Rule(stellar_brightness['medium'] & transit_depth['moderate'], exoplanet_presence['high'])
rule6 = ctrl.Rule(stellar_brightness['medium'] & transit_depth['deep'], exoplanet_presence['high'])

rule7 = ctrl.Rule(stellar_brightness['high'] & transit_depth['shallow'], exoplanet_presence['high'])
rule8 = ctrl.Rule(stellar_brightness['high'] & transit_depth['moderate'], exoplanet_presence['high'])
rule9 = ctrl.Rule(stellar_brightness['high'] & transit_depth['deep'], exoplanet_presence['high'])

# Create the fuzzy control system
exoplanet_detection = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
exoplanet_detection_simulation = ctrl.ControlSystemSimulation(exoplanet_detection)

# Set the input values (KEPLER-186F)
exoplanet_detection_simulation.input['stellar_brightness'] = 14.74
exoplanet_detection_simulation.input['transit_depth'] = 0.0071

# Crunch the numbers
exoplanet_detection_simulation.compute()

# Print the output
print('exoplanet_presence: {:.2f}%'.format(exoplanet_detection_simulation.output['exoplanet_presence'] * 100))

# Visualize the membership functions and the output
stellar_brightness.view(sim=exoplanet_detection_simulation)
transit_depth.view(sim=exoplanet_detection_simulation)
exoplanet_presence.view(sim=exoplanet_detection_simulation)

plt.show()