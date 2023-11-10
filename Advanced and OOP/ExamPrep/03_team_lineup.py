def team_lineup(*players):
    country_counts = {}

    for player in players:
        player_name, country = player
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1

    sorted_players = sorted(players, key=lambda x: (-country_counts[x[1]], (x[1])))

    output = ""
    current_country = None

    for player in sorted_players:
        player_name, country = player
        if country != current_country:
            output += f"{country}:\n"
            current_country = country
        output += f"  -{player_name}\n"

    return output

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))
