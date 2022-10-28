from collections import Counter


class TrackOrders:
    def __init__(self):
        self._data = {}

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        if customer not in self._data:
            self._data[customer] = [(order, day)]
        else:
            self._data[customer].append((order, day))

    def get_most_ordered_dish_per_customer(self, customer):
        first = self._data[customer][0][0]
        frequency = {}
        for order, _ in self._data[customer]:
            if order in frequency:
                frequency[order] += 1
            else:
                frequency[order] = 1
            if frequency[order] > frequency[first]:
                first = order
        return first

    def get_never_ordered_per_customer(self, customer):
        customer_orders = set(order for order, _ in self._data[customer])
        all_orders = set(
            order[0] for client in self._data.values() for order in client
        )
        not_ordered = all_orders - customer_orders
        return not_ordered

    def get_days_never_visited_per_customer(self, customer):
        customer_days = set(day for _, day in self._data[customer])
        all_days = set(
            day[1] for client in self._data.values() for day in client
        )
        not_attended = all_days - customer_days
        return not_attended

    def get_busiest_day(self):
        all_days = Counter(
            day[1] for client in self._data.values() for day in client
        )
        busiest = all_days.most_common()[0][0]
        return busiest

    def get_least_busy_day(self):
        all_days = Counter(
            day[1] for client in self._data.values() for day in client
        )
        busiest = all_days.most_common()[-1][0]
        return busiest

    def get_how_many_times(self, customer, order):
        customer_orders = set(order for order, _ in self._data[customer])
        quantity = 0
        for food in customer_orders:
            if food == order:
                quantity += 1
        return quantity
