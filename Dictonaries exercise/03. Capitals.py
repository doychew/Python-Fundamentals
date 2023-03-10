country = input().split(", ")
capital = input().split(", ")
dict = {country[index]: capital[index] for index in range(len(capital))}
for country, capital in dict.items():
    print(f"{country} -> {capital}")
