travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(country_visits, times_visits, cities_visits):
    new_country = {}
    new_country["country"] = country_visits
    new_country["visits"] = times_visits
    new_country["cities"] = cities_visits
    travel_log.append(new_country)
    # or
    # new_country = {"country": country_visits, "visits": times_visits, "cities": cities_visits}
    # travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
