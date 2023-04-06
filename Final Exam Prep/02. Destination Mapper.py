import re
map_str = input()  # Input the string representing the map


valid_loc_pattern = r"([=/])([A-Z][a-zA-Z]{2,})(\1)"


valid_locs = re.findall(valid_loc_pattern, map_str)


destinations = []
travel_points = 0
for loc in valid_locs:
    dest = loc[1]
    travel_points += len(dest)
    destinations.append(dest)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")