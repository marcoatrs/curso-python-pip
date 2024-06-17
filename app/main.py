import charts
import read
import utils


def run():
    data = read.read_csv("./data.csv")
    country = input("Type Country => ")

    result = utils.population_by_country(data, country)

    if len(result) <= 0:
        print("No se encontro el pais")
        return

    country = result[0]
    keys, values = utils.get_population(country)
    charts.generate_bar_chart(country["Country/Territory"], keys, values)

    labels, values = utils.get_wpp(data)
    charts.generate_pie_chart(labels, values)


if __name__ == "__main__":
    run()
