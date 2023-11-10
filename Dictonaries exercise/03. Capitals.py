countries = input().split(", ")
capitals = input().split(", ")
countries_and_capitals = {}
for capital in capitals:
    for country in countries:
        if country not in countries_and_capitals:
            countries_and_capitals[country] = capital
            break
for country, capital in countries_and_capitals.items():
    print(f"{country} -> {capital}")
