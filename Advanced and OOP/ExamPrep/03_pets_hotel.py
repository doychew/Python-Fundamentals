# def accommodate_new_pets(capacity, maximum_weight, *args):
#     number_of_pets = 0
#     message = ""
#     has_enough_capacity = True
#     pet_dict = {}
#     for element in args:
#         pet_type = element[0]
#         pet_weight = float(element[1])
#         if capacity > 0:
#             if pet_weight < maximum_weight:
#                 number_of_pets += 1
#                 capacity -= 1
#                 if pet_type not in pet_dict:
#                     pet_dict[pet_type] = 0
#                 pet_dict[pet_type] += 1
#         if capacity == 0:
#             has_enough_capacity = False
#             message += "You did not manage to accommodate all pets!\n"
#             break
#     if has_enough_capacity:
#         message += f"All pets are accommodated! Available capacity: {capacity}.\n"
#     message += "Accommodated pets:\n"
#     sorted_dict = sorted(pet_dict.items(), key=lambda x: x[0])
#     for pet, count in sorted_dict:
#         message += f"{pet}: {count}\n"
#     return message

def accommodate_new_pets(capacity, weight_limit, *args):
    result = []
    pets_map = {}

    for pet_type, pet_weight in args:
        if capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break
        if pet_weight > weight_limit:
            continue
        if pet_type not in pets_map:
            pets_map[pet_type] = 0
        pets_map[pet_type] += 1
        capacity -= 1
    else:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")

    result.append("Accommodated pets:")
    for pet_type, pet_count in sorted(pets_map.items()):
        result.append(f"{pet_type}: {pet_count}")
    return '\n'.join(result)

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
