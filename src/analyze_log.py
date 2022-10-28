from src.track_orders import TrackOrders
import csv


def analyze_log(path_to_file):
    trackOrders = TrackOrders
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, encoding="utf8") as file:
            content = csv.reader(file, delimiter=",", quotechar='"')
            for customer, order, day in content:
                trackOrders.add_new_order(customer, order, day)
            most_ordered = trackOrders.get_most_ordered_dish_per_customer("maria")
            frequency = trackOrders.get_how_many_times("arnaldo", "hamburguer")
            never_ordered = trackOrders.get_never_ordered_per_customer("joao")
            never_visited = trackOrders.get_days_never_visited_per_customer("joao")

        with open("data/mkt_campaign.txt", "w") as file:
            file.write(
                f"{most_ordered}\n"
                f"{frequency}\n"
                f"{never_ordered}\n"
                f"{never_visited}\n"
            )
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
