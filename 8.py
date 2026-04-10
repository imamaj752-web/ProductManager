class Transport:
    def __init__(self, base_fare):
        self.base_fare = base_fare

    def calculate_fare(self, distance):
        return distance * self.base_fare


class Bus(Transport):
    def __init__(self):
        super().__init__(10)

    def calculate_fare(self, distance):
        return self.base_fare


class Taxi(Transport):
    def __init__(self):
        super().__init__(5)



class Train(Transport):
    def __init__(self):
        super().__init__(2.5)

    def calculate_fare(self, distance):
        fare = super().calculate_fare(distance)
        if distance > 100:
            fare *= 0.9  # Знижка 10%
        return fare