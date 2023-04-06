import re
text = input()
pattern = r"(#|\|)(?P<item_name>[A-Za-z\s]+)\1(?P<Date>\d{2}/\d{2}/\d{2})\1(?P<Calories>[0-9]{1,4}|10000)\1"
total_calories = 0
valid_data = [obj.groupdict() for obj in re.finditer(pattern, text)]
for item in valid_data:
    total_calories += int(item["Calories"])

day_to_last = total_calories // 2000
print(f"You have food to last you for: {day_to_last} days!")
for item in valid_data:
    print(f"Item: {item['item_name']}, Best before: {item['Date']}, Nutrition: {item['Calories']}")