import re

pattern = r'(?P<symbols>[=/])(?P<location>[A-Z][a-zA-Z]{2,})\1'

text = input()

locations = []
travel_points = 0

# if re.search(pattern, text) is not None:
#     matches = re.finditer(pattern, text)
matches = re.findall(pattern, text)
for match in matches:
    location = match[1]

    locations.append(location)
    travel_points += len(location)

print(f"Destinations: {', '.join(locations)}")
print(f"Travel Points: {travel_points}")