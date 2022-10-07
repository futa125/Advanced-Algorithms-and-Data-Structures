person_data = {
    "Ana": 1995,
    "Zoran": 1978,
    "Lucija": 2001,
    "Anja": 1997,
}

for name, year in person_data.items():
    person_data[name] = year - 1

year_age = []

for year in person_data.values():
    year_age.append((year, 2022 - year))
