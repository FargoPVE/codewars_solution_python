def number(bus_stops):
    return sum(number_of_passenger_inside[0] for number_of_passenger_inside in bus_stops) \
           - sum(number_of_passenger_out_from_bus[1] for number_of_passenger_out_from_bus in bus_stops)
