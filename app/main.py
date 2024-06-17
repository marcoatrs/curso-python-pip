import charts
import read
import utils

import pandas as pd


def run():
    # data = read.read_csv("./data.csv")
    # labels, values = utils.get_wpp(data)

    # result = utils.population_by_country(data, country)

    # if len(result) <= 0:
    #     print("No se encontro el pais")
    #     return

    # country = result[0]
    # keys, values = utils.get_population(country)
    # charts.generate_bar_chart(country["Country/Territory"], keys, values)

    df = pd.read_csv("./data.csv")
    df = df[df["Continent"] == "South America"]

    labels = df["Country/Territory"].values
    values = df["World Population Percentage"].values
    charts.generate_pie_chart(labels, values)

    country = input("Type Country => ")
    df = df[df["Country/Territory"] == country]

    keys, values = utils.get_population(df)
    charts.generate_bar_chart(df["Country/Territory"].values[0], keys, values)


if __name__ == "__main__":
    run()
