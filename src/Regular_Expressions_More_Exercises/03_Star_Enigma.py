import re

n = int(input())

key_pattern = r'[starSTAR]'
pattern = r'@(?P<planet_name>[a-zA-Z]+)[^@:!\->]*:(?P<planet_population>[0-9]+)[^@:!\->]*' \
          r'!(?P<attack_type>[AD])![^@:!\->]*->(?P<soldier_count>[0-9]+)'

attacked_planets = []
destroyed_planets = []

for _ in range(n):
    text = input()
    decrypted_message = ''
    matches = re.findall(key_pattern, text)
    star_count = len(matches)
    for s in text:
        decrypted_message += chr(ord(s) - star_count)

    messages = re.finditer(pattern, decrypted_message)
    for message in messages:
        if message.group('attack_type') == 'A':
            attacked_planets.append(message.group('planet_name'))
        else:
            destroyed_planets.append(message.group('planet_name'))

sorted_attacked = sorted(attacked_planets)
sorted_destroyed = sorted(destroyed_planets)

print(f"Attacked planets: {len(sorted_attacked)}")
for planet in sorted_attacked:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(sorted_destroyed)}")
for planet in sorted_destroyed:
    print(f"-> {planet}")
