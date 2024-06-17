def get_population(country: dict) -> tuple[list, list]:
    population = {
        "2022": int(country["2022 Population"]),
        "2020": int(country["2020 Population"]),
        "2015": int(country["2015 Population"]),
        "2010": int(country["2010 Population"]),
        "2000": int(country["2000 Population"]),
        "1990": int(country["1990 Population"]),
        "1980": int(country["1980 Population"]),
        "1970": int(country["1970 Population"])
    }
    return population.keys(), population.values()


def population_by_country(data: list[dict], country: str):
    result = list(filter(lambda item: item["Country/Territory"] == country, data))
    return result


def get_wpp(data: list[dict]):
    country = "Country/Territory"
    wpp = "World Population Percentage"
    countries = {item[country]: item[wpp] for item in data}
    return countries.keys(), countries.values()
