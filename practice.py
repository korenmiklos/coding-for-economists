def convert_feet_to_meters(distance_feet):
    return 0.3048 * distance_feet

print('I am here.')
distance_meter = 10.0
print(distance_meter)
distance_meter = convert_feet_to_meters(200.0)
print(distance_meter)
print('Now I am done.')