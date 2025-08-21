import pandas

import numpy

# lists to hold ticket details
all_flowers = ['Rose', 'Tulip', 'Sunflower', 'Lily', 'Daisy', 'Orchid', 'Lavender', 'Marigold', 'Rose', 'Daffodil']
all_flower_costs = [15, 8, 6, 12, 4, 18, 5, 7, 16, 9]

flower_dict = {
    'Flower Name': all_flowers,
    'Flower Price': all_flower_costs,
}

# create dataframe / table from dictionary
planty_plants_frame = pandas.DataFrame(flower_dict)

# Rearranging index
planty_plants_frame.index = numpy.arange(1, len(planty_plants_frame) + 1)

print(planty_plants_frame)
print()